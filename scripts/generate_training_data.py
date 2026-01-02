#!/usr/bin/env python3
"""Generate training data for personality profile model fine-tuning.

Iterates through all 3,125 combinations of BFI-2 domain scores (A,C,E,O,N each 1-5),
generating 500 samples per combination (100 runs × 5 length tiers).

Output: One JSONL file per combination (training_data_0001.jsonl through training_data_3125.jsonl).
Resume support: Skips combos where output file already has expected line count.
"""

import argparse
import json
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import product
from pathlib import Path
from threading import Lock
from typing import Iterator

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from persona_api.services import DomainTextResolver, ProfileGenerator

# Hardcoded config (personal script, not runtime)
OLLAMA_HOST = "sparx"
OLLAMA_MODEL = "qwen2.5:7b"  # Better quality for training data than llama3.2

# Domain display order
DOMAIN_ORDER = ["agreeableness", "conscientiousness", "extraversion", "open_mindedness", "negative_emotionality"]
DOMAIN_PREFIX = {"agreeableness": "A", "conscientiousness": "C", "extraversion": "E", "open_mindedness": "O", "negative_emotionality": "N"}

# Emoji gradients (same as CLI)
DOMAIN_EMOJI_GRADIENT = {
    "negative_emotionality": {1: "😌", 2: "🙂", 3: "😐", 4: "😟", 5: "😰"},
    "extraversion": {1: "🌑", 2: "🌒", 3: "🌓", 4: "🌔", 5: "🌕"},
    "agreeableness": {1: "🧊", 2: "❄️", 3: "🌥️", 4: "🌤️", 5: "☀️"},
    "conscientiousness": {1: "🌀", 2: "😅", 3: "📝", 4: "📋", 5: "🎯"},
    "open_mindedness": {1: "📦", 2: "📐", 3: "🔍", 4: "🎨", 5: "🌈"},
}

# Length tiers (None = no constraint)
LENGTH_TIERS = [128, 256, None]
RUNS_PER_TIER = 5

# Total samples
TOTAL_COMBINATIONS = 5 ** 5  # 3125
SAMPLES_PER_COMBINATION = len(LENGTH_TIERS) * RUNS_PER_TIER  # 500
TOTAL_SAMPLES = TOTAL_COMBINATIONS * SAMPLES_PER_COMBINATION  # 1,562,500


def generate_combinations() -> Iterator[tuple[int, int, int, int, int]]:
    """Generate all (A, C, E, O, N) combinations in order."""
    for combo in product(range(1, 6), repeat=5):
        yield combo  # (A, C, E, O, N)


def combo_to_scores(combo: tuple[int, int, int, int, int]) -> dict[str, int]:
    """Convert combo tuple to domain scores dict."""
    return {
        "agreeableness": combo[0],
        "conscientiousness": combo[1],
        "extraversion": combo[2],
        "open_mindedness": combo[3],
        "negative_emotionality": combo[4],
    }


def scores_to_string(scores: dict[str, int]) -> str:
    """Format scores as 'A5,C5,E5,O5,N1'."""
    return ",".join(f"{DOMAIN_PREFIX[d]}{scores[d]}" for d in DOMAIN_ORDER)


def scores_to_emoji(scores: dict[str, int]) -> str:
    """Format scores as emoji string."""
    return "".join(DOMAIN_EMOJI_GRADIENT[d][scores[d]] for d in DOMAIN_ORDER)


def call_ollama(prompt: str, timeout: int = 120) -> str:
    """Call Ollama API via SSH to sparx."""
    import json
    import subprocess

    payload = json.dumps({
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    })

    cmd = ["ssh", OLLAMA_HOST, "curl -s http://localhost:11434/api/generate -d @-"]
    result = subprocess.run(cmd, input=payload, capture_output=True, text=True, timeout=timeout)

    if result.returncode != 0:
        raise RuntimeError(f"SSH/Ollama error: {result.stderr}")

    response = json.loads(result.stdout)
    return response.get("response", "").strip()


def generate_sample(
    scores: dict[str, int],
    length: int | None,
    seed: str,
) -> dict:
    """Generate a single training sample."""
    # Build facet scores (all facets same as domain score)
    facet_scores = {domain: (score, score, score) for domain, score in scores.items()}

    # Resolve behaviors
    resolver = DomainTextResolver(seed=seed)
    behaviors = resolver.resolve_all(facet_scores)

    # Slice traits
    profile_gen = ProfileGenerator(seed=seed)
    traits = profile_gen.slice_instructions(behaviors, count=5)

    if not traits:
        raise ValueError(f"No traits generated for {scores_to_string(scores)}")

    # Generate prompt
    prompt = profile_gen.generate_prompt(traits, length=length)

    # Call Ollama
    output = call_ollama(prompt)

    # Build record
    traits_text = ", ".join(t["trait"] for t in traits)

    return {
        "inputs": {
            "emoji": scores_to_emoji(scores),
            "scores": scores_to_string(scores),
            "traits": traits_text,
        },
        "output": output,
        "meta": {
            "A": scores["agreeableness"],
            "C": scores["conscientiousness"],
            "E": scores["extraversion"],
            "O": scores["open_mindedness"],
            "N": scores["negative_emotionality"],
            "length_target": length,
            "length_actual": len(output),
            "seed": seed,
        },
    }


class TrainingDataGenerator:
    """Orchestrates training data generation with one file per combo."""

    def __init__(
        self,
        output_dir: Path,
        workers: int,
    ):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.workers = workers
        self.error_path = output_dir / "errors.jsonl"

        self.write_lock = Lock()
        self.error_count = 0
        self.start_time = time.time()
        self.samples_generated = 0
        self.combos_completed = 0
        self.combos_skipped = 0

    def _get_combo_file(self, combo_idx: int) -> Path:
        """Get the output file path for a combo (1-indexed in filename)."""
        return self.output_dir / f"training_data_{combo_idx + 1:04d}.jsonl"

    def _is_combo_complete(self, combo_idx: int) -> bool:
        """Check if a combo file already exists (skip any existing file)."""
        combo_file = self._get_combo_file(combo_idx)
        return combo_file.exists()

    def _write_sample(self, combo_idx: int, sample: dict):
        """Write a sample to the combo's output file."""
        combo_file = self._get_combo_file(combo_idx)
        with self.write_lock:
            with open(combo_file, "a") as f:
                f.write(json.dumps(sample, ensure_ascii=False) + "\n")
            self.samples_generated += 1

    def _write_error(self, error_info: dict):
        """Write an error to the error file."""
        with self.write_lock:
            with open(self.error_path, "a") as f:
                f.write(json.dumps(error_info, ensure_ascii=False) + "\n")
            self.error_count += 1

    def _format_eta(self, seconds: float) -> str:
        """Format seconds as human-readable duration."""
        if seconds < 0:
            return "calculating..."
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        if hours > 0:
            return f"{hours}h {minutes}m"
        return f"{minutes}m"

    def _print_status(self, combo_idx: int, tier_idx: int, run_idx: int, scores: dict[str, int]):
        """Print current progress status."""
        completed = (self.combos_skipped * SAMPLES_PER_COMBINATION) + self.samples_generated
        elapsed = time.time() - self.start_time

        if self.samples_generated > 0:
            rate = self.samples_generated / elapsed
            remaining = TOTAL_SAMPLES - completed
            eta = remaining / rate if rate > 0 else -1
        else:
            rate = 0
            eta = -1

        pct = (completed / TOTAL_SAMPLES) * 100
        length_str = str(LENGTH_TIERS[tier_idx]) if LENGTH_TIERS[tier_idx] else "None"

        status = (
            f"\r[{pct:5.1f}%] {completed:,}/{TOTAL_SAMPLES:,} | "
            f"Combo {combo_idx+1}/{TOTAL_COMBINATIONS} {scores_to_string(scores)} | "
            f"len={length_str} run={run_idx+1}/{RUNS_PER_TIER} | "
            f"{rate:.1f}/s | ETA: {self._format_eta(eta)} | Errors: {self.error_count}"
        )

        # Pad to clear previous line
        print(f"{status:<120}", end="", flush=True)

    def _generate_single(
        self,
        combo_idx: int,
        tier_idx: int,
        run_idx: int,
        scores: dict[str, int],
    ) -> bool:
        """Generate a single sample. Returns True on success."""
        length = LENGTH_TIERS[tier_idx]
        seed = f"{combo_idx}_{tier_idx}_{run_idx}_{random.randint(0, 999999)}"

        try:
            sample = generate_sample(scores, length, seed)
            self._write_sample(combo_idx, sample)
            return True
        except Exception as e:
            self._write_error({
                "combo_idx": combo_idx,
                "tier_idx": tier_idx,
                "run_idx": run_idx,
                "scores": scores_to_string(scores),
                "length": length,
                "seed": seed,
                "error": str(e),
            })
            return False

    def _generate_combo(self, combo_idx: int, scores: dict[str, int]) -> int:
        """Generate all samples for a single combo. Returns count generated."""
        count = 0
        for tier_idx in range(len(LENGTH_TIERS)):
            for run_idx in range(RUNS_PER_TIER):
                self._print_status(combo_idx, tier_idx, run_idx, scores)
                if self._generate_single(combo_idx, tier_idx, run_idx, scores):
                    count += 1
        return count

    def run(self):
        """Run the generation process."""
        combos = list(generate_combinations())

        # Count already-completed combos
        for combo_idx in range(len(combos)):
            if self._is_combo_complete(combo_idx):
                self.combos_skipped += 1

        print(f"Generating {TOTAL_SAMPLES:,} training samples")
        print(f"Combinations: {TOTAL_COMBINATIONS:,} | Samples per combo: {SAMPLES_PER_COMBINATION}")
        print(f"Length tiers: {LENGTH_TIERS} | Runs per tier: {RUNS_PER_TIER}")
        print(f"Workers: {self.workers} | Model: {OLLAMA_MODEL} | Host: {OLLAMA_HOST}")
        print(f"Output dir: {self.output_dir}")
        if self.combos_skipped > 0:
            print(f"Resuming: {self.combos_skipped} combos already complete ({self.combos_skipped * SAMPLES_PER_COMBINATION:,} samples)")
        print()

        if self.workers == 1:
            self._run_sequential(combos)
        else:
            self._run_parallel(combos)

        print()
        print(f"Done! Generated {self.samples_generated:,} new samples with {self.error_count} errors")
        print(f"Total complete: {self.combos_skipped + self.combos_completed}/{TOTAL_COMBINATIONS} combos")

    def _run_sequential(self, combos: list):
        """Run generation sequentially, one combo at a time."""
        for combo_idx, combo in enumerate(combos):
            if self._is_combo_complete(combo_idx):
                continue

            scores = combo_to_scores(combo)
            self._generate_combo(combo_idx, scores)
            self.combos_completed += 1

    def _run_parallel(self, combos: list):
        """Run generation with parallel workers within each combo."""
        for combo_idx, combo in enumerate(combos):
            if self._is_combo_complete(combo_idx):
                continue

            scores = combo_to_scores(combo)

            # Build work for this combo
            work = []
            for tier_idx in range(len(LENGTH_TIERS)):
                for run_idx in range(RUNS_PER_TIER):
                    work.append((combo_idx, tier_idx, run_idx, scores))

            # Run this combo's work in parallel
            with ThreadPoolExecutor(max_workers=self.workers) as executor:
                futures = {}
                for combo_idx, tier_idx, run_idx, scores in work:
                    future = executor.submit(
                        self._generate_single, combo_idx, tier_idx, run_idx, scores
                    )
                    futures[future] = (combo_idx, tier_idx, run_idx, scores)

                for future in as_completed(futures):
                    combo_idx, tier_idx, run_idx, scores = futures[future]
                    self._print_status(combo_idx, tier_idx, run_idx, scores)

            self.combos_completed += 1


def main():
    parser = argparse.ArgumentParser(
        description="Generate training data for personality profile fine-tuning.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Config (hardcoded):
  Host: {OLLAMA_HOST}
  Model: {OLLAMA_MODEL}

Output:
  One file per combo: training_data_0001.jsonl through training_data_3125.jsonl
  Resume: automatically skips combos where file has {SAMPLES_PER_COMBINATION} lines

Examples:
  %(prog)s                              # Run with defaults
  %(prog)s --workers 4                  # Use 4 parallel workers
  %(prog)s --output-dir ./my_data       # Custom output directory
        """,
    )
    parser.add_argument(
        "--output-dir", "-o",
        type=Path,
        default=Path("training_data"),
        help="Output directory for JSONL files (default: training_data/)",
    )
    parser.add_argument(
        "--workers", "-w",
        type=int,
        default=1,
        help="Number of parallel workers (default: 1)",
    )

    args = parser.parse_args()

    generator = TrainingDataGenerator(
        output_dir=args.output_dir,
        workers=args.workers,
    )

    try:
        generator.run()
    except KeyboardInterrupt:
        print("\n\nInterrupted! Complete combos are preserved in output files.")
        sys.exit(1)


if __name__ == "__main__":
    main()
