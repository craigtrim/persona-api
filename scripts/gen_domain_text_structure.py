#!/usr/bin/env python3
"""Generate content-addressable file structure for domain text summaries.

Creates JSON files for all possible facet score combinations.
Each domain has 5^3 = 125 score combinations.

Prerequisites:
    This script requires behavioral instruction files to exist.
    Run the following scripts first (in order):

    1. Generate behavioral instructions from OWL:
       $ poetry run python scripts/gen_behavioral_instructions.py --host <ollama-host>

    2. Reorganize into per-facet files:
       $ poetry run python scripts/reorganize_behavioral_instructions.py

Output structure:
    persona_api/data/text/{domain}/{score1}/{score2}/{score3}.json

Example output:
    {
        "_meta": {
            "domain": "conscientiousness",
            "facets": ["Organization", "Productiveness", "Responsibility"],
            "scores": [3, 2, 2]
        },
        "coherence": 2,
        "texts": {
            "I sometimes provide disorganized...": ["cluttered answers", "lacks structure"],
            "I sometimes offer somewhat...": ["keeps on topic", "occasional delays"],
            ...
        }
    }

Usage:
    poetry run python scripts/gen_domain_text_structure.py
    poetry run python scripts/gen_domain_text_structure.py --domain conscientiousness
    poetry run python scripts/gen_domain_text_structure.py --dry-run
"""

import json
import sys
from itertools import product
from pathlib import Path

from persona_api.data.facets import (
    AESTHETIC_SENSITIVITY,
    ANXIETY,
    ASSERTIVENESS,
    COMPASSION,
    CREATIVE_IMAGINATION,
    DEPRESSION,
    EMOTIONAL_VOLATILITY,
    ENERGY_LEVEL,
    INTELLECTUAL_CURIOSITY,
    ORGANIZATION,
    PRODUCTIVENESS,
    RESPECTFULNESS,
    RESPONSIBILITY,
    SOCIABILITY,
    TRUST,
)

# Domain -> ordered list of facet data
DOMAINS = {
    "extraversion": [SOCIABILITY, ASSERTIVENESS, ENERGY_LEVEL],
    "agreeableness": [COMPASSION, RESPECTFULNESS, TRUST],
    "conscientiousness": [ORGANIZATION, PRODUCTIVENESS, RESPONSIBILITY],
    "negative_emotionality": [ANXIETY, DEPRESSION, EMOTIONAL_VOLATILITY],
    "open_mindedness": [INTELLECTUAL_CURIOSITY, AESTHETIC_SENSITIVITY, CREATIVE_IMAGINATION],
}

# Domain -> ordered list of facet names (lowercase, matching behavioral file names)
DOMAIN_FACETS = {
    "extraversion": ["sociability", "assertiveness", "energy_level"],
    "agreeableness": ["compassion", "respectfulness", "trust"],
    "conscientiousness": ["organization", "productiveness", "responsibility"],
    "negative_emotionality": ["anxiety", "depression", "emotional_volatility"],
    "open_mindedness": ["intellectual_curiosity", "aesthetic_sensitivity", "creative_imagination"],
}

SCORES = range(1, 6)  # 1-5
TEXT_IDXS = range(4)  # 0-3 (4 survey items per facet)


def check_behavioral_files(behavioral_dir: Path) -> list[str]:
    """Check that all required behavioral files exist.

    Returns:
        List of missing facet names, empty if all exist.
    """
    missing = []
    all_facets = set()
    for facets in DOMAIN_FACETS.values():
        all_facets.update(facets)

    for facet in sorted(all_facets):
        file_path = behavioral_dir / f"{facet}.json"
        if not file_path.exists():
            missing.append(facet)

    return missing


def load_behavioral_data(behavioral_dir: Path) -> dict[str, dict]:
    """Load all behavioral instruction files.

    Returns:
        Dict mapping facet name -> behavioral data
    """
    data = {}
    all_facets = set()
    for facets in DOMAIN_FACETS.values():
        all_facets.update(facets)

    for facet in all_facets:
        file_path = behavioral_dir / f"{facet}.json"
        data[facet] = json.loads(file_path.read_text())

    return data


def print_dependency_error(missing_files: list[str], behavioral_dir: Path) -> None:
    """Print helpful error message about missing dependencies."""
    print("=" * 70)
    print("ERROR: Missing required behavioral instruction files")
    print("=" * 70)
    print()
    print(f"Expected location: {behavioral_dir}")
    print()
    print("Missing files:")
    for facet in missing_files:
        print(f"  - {facet}.json")
    print()
    print("-" * 70)
    print("HOW TO FIX")
    print("-" * 70)
    print()
    print("Run these scripts in order to generate the behavioral files:")
    print()
    print("  Step 1: Extract behavioral instructions from OWL using Ollama")
    print("  ---------------------------------------------------------------")
    print("  $ poetry run python scripts/gen_behavioral_instructions.py --host <ollama-host>")
    print()
    print("  This sends each BFI-2 rating sentence to Ollama to extract")
    print("  observable chatbot behaviors. Requires Ollama running with")
    print("  a model like qwen2.5:7b.")
    print()
    print("  Options:")
    print("    --host HOST    Ollama server address (default: 192.168.4.98)")
    print("    --model MODEL  Ollama model name (default: qwen2.5:7b)")
    print("    --dry-run      Preview sentences without querying Ollama")
    print("    --limit N      Process only first N sentences (for testing)")
    print()
    print("  Step 2: Reorganize into per-facet files")
    print("  ----------------------------------------")
    print("  $ poetry run python scripts/reorganize_behavioral_instructions.py")
    print()
    print("  This takes the flat output from Step 1 and organizes it into")
    print("  15 facet-specific JSON files in persona_api/data/behavioral/")
    print()
    print("=" * 70)


def rate_coherence(scores: tuple[int, int, int]) -> int:
    """Rate coherence of a score combination.

    Returns:
        1 = coherent (all same direction or within +/-1)
        2 = uncertain (moderate spread, +/-2)
        3 = contradictory (outlier >=3 points from others)
    """
    s1, s2, s3 = scores

    # All neutral
    if s1 == s2 == s3 == 3:
        return 1

    # Calculate spread
    min_s = min(scores)
    max_s = max(scores)
    spread = max_s - min_s

    # All same or within +/-1
    if spread <= 1:
        return 1

    # Moderate spread
    if spread <= 2:
        return 2

    # Large spread (>=3) - check if one is an outlier
    sorted_scores = sorted(scores)

    if sorted_scores[1] - sorted_scores[0] <= 1 and sorted_scores[2] - sorted_scores[1] >= 3:
        return 3
    if sorted_scores[2] - sorted_scores[1] <= 1 and sorted_scores[1] - sorted_scores[0] >= 3:
        return 3

    if spread >= 3:
        return 3

    return 2


def get_rating_text(facet_data: dict, score: int, text_idx: int) -> str | None:
    """Get rating text for a facet, score, and text index."""
    survey_items = facet_data.get("survey_items", [])
    if text_idx >= len(survey_items):
        return None

    ratings = survey_items[text_idx].get("ratings", {})
    return ratings.get(str(score))


def get_behavioral_instructions(
    behavioral_data: dict,
    facet_name: str,
    score: int,
    text_idx: int,
) -> list[str]:
    """Get behavioral instructions for a facet, score, and survey item index."""
    facet_data = behavioral_data.get(facet_name, {})
    survey_items = facet_data.get("survey_items", [])

    if text_idx >= len(survey_items):
        return []

    ratings = survey_items[text_idx].get("ratings", {})
    rating_data = ratings.get(str(score), {})

    return rating_data.get("instructions", [])


def get_file_path(base_dir: Path, domain: str, scores: tuple[int, int, int]) -> Path:
    """Get file path for a score combination."""
    return base_dir / domain / str(scores[0]) / str(scores[1]) / f"{scores[2]}.json"


def generate_file_content(
    domain: str,
    facet_data: list[dict],
    facet_names: list[str],
    behavioral_data: dict,
    scores: tuple[int, int, int],
) -> dict:
    """Generate JSON content with texts mapped to their behavioral instructions."""
    display_names = [f["name"] for f in facet_data]
    coherence = rate_coherence(scores)

    content = {
        "_meta": {
            "domain": domain,
            "facets": display_names,
            "scores": list(scores),
        },
        "coherence": coherence,
        "texts": {},
    }

    # Generate all 64 text_idx combinations (4^3)
    for text_idxs in product(TEXT_IDXS, repeat=3):
        texts = []
        text_instructions = set()

        for i, (score, text_idx) in enumerate(zip(scores, text_idxs)):
            # Skip neutral scores
            if score == 3:
                continue

            text = get_rating_text(facet_data[i], score, text_idx)
            if text:
                texts.append(text)

            # Collect behavioral instructions for THIS text combination
            instructions = get_behavioral_instructions(
                behavioral_data,
                facet_names[i],
                score,
                text_idx,
            )
            text_instructions.update(instructions)

        # Join with space, skip if all neutral
        if texts:
            combined = " ".join(texts)
            # If duplicate text, merge instructions
            if combined in content["texts"]:
                existing = set(content["texts"][combined])
                existing.update(text_instructions)
                content["texts"][combined] = sorted(existing)
            else:
                content["texts"][combined] = sorted(text_instructions)

    return content


def generate_coherence_index(base_dir: Path, domain: str) -> dict:
    """Generate coherence index for a domain."""
    index = {
        "1": [],  # coherent
        "2": [],  # uncertain
        "3": [],  # contradictory
    }

    for scores in product(SCORES, repeat=3):
        coherence = rate_coherence(scores)
        path = f"{scores[0]}/{scores[1]}/{scores[2]}.json"
        index[str(coherence)].append(path)

    return index


def generate_domain_files(
    base_dir: Path,
    domain: str,
    facet_data: list[dict],
    facet_names: list[str],
    behavioral_data: dict,
    dry_run: bool = False,
) -> int:
    """Generate all files for a domain."""
    count = 0

    for scores in product(SCORES, repeat=3):
        file_path = get_file_path(base_dir, domain, scores)

        if not dry_run:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            content = generate_file_content(
                domain,
                facet_data,
                facet_names,
                behavioral_data,
                scores,
            )
            file_path.write_text(json.dumps(content, indent=2))

        count += 1

    # Generate coherence index
    if not dry_run:
        index = generate_coherence_index(base_dir, domain)
        index_path = base_dir / domain / "coherence.json"
        index_path.write_text(json.dumps(index, indent=2))

    return count


def print_preface(base_dir: Path, behavioral_dir: Path, domain: str | None) -> None:
    """Print preface explaining what the script will do."""
    print("=" * 70)
    print("GENERATE DOMAIN TEXT STRUCTURE")
    print("=" * 70)
    print()
    print("This script generates content-addressable JSON files for all possible")
    print("BFI-2 facet score combinations. Each domain has 5^3 = 125 combinations.")
    print()
    print("-" * 70)
    print("CONFIGURATION")
    print("-" * 70)
    print(f"  Behavioral data:  {behavioral_dir}")
    print(f"  Output dir:       {base_dir}")
    if domain:
        print(f"  Domain:           {domain} (125 files)")
    else:
        print(f"  Domains:          {len(DOMAINS)} (625 total files)")
    print()
    print("-" * 70)
    print("OUTPUT STRUCTURE")
    print("-" * 70)
    print("  Each file contains:")
    print("    - _meta: domain, facets, scores")
    print("    - coherence: 1=coherent, 2=uncertain, 3=contradictory")
    print("    - texts: dict mapping sentences to their behavioral instructions")
    print()
    print("  Example path: conscientiousness/3/2/4.json")
    print("    Maps to: Organization(3), Productiveness(2), Responsibility(4)")
    print()
    print("-" * 70)
    print("PREREQUISITES")
    print("-" * 70)
    print("  Behavioral instruction files must exist in:")
    print(f"    {behavioral_dir}")
    print()
    print("  If missing, run these scripts first:")
    print("    $ poetry run python scripts/gen_behavioral_instructions.py --host <ollama>")
    print("    $ poetry run python scripts/reorganize_behavioral_instructions.py")
    print()


def print_summary(base_dir: Path, total: int, domains_processed: list[str]) -> None:
    """Print summary of what was done."""
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print(f"  Files generated:    {total}")
    print(f"  Domains processed:  {len(domains_processed)}")
    for domain in domains_processed:
        print(f"    - {domain}")
    print(f"  Output directory:   {base_dir}")
    print()
    print("-" * 70)
    print("NEXT STEPS")
    print("-" * 70)
    print()
    print("  The domain text files are now ready for use by the API.")
    print()
    print("  Usage example:")
    print("    from persona_api.services.domain_text_resolver import DomainTextResolver")
    print("    resolver = DomainTextResolver()")
    print("    result = resolver.resolve('conscientiousness', [3, 2, 4])")
    print()
    print("  To verify output:")
    print(f"    $ cat {base_dir}/conscientiousness/3/2/4.json")
    print()
    print("=" * 70)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate domain text file structure with behavioral instructions.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                              Generate all domains
  %(prog)s --domain conscientiousness   Generate single domain
  %(prog)s --dry-run                    Count files without creating
  %(prog)s -y                           Skip confirmation prompt

Prerequisites:
  Behavioral instruction files must exist in persona_api/data/behavioral/
  Run gen_behavioral_instructions.py and reorganize_behavioral_instructions.py first.
        """,
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Count files without creating them",
    )
    parser.add_argument(
        "--domain",
        type=str,
        choices=list(DOMAINS.keys()),
        help="Generate only for specified domain",
    )
    parser.add_argument(
        "-y", "--yes",
        action="store_true",
        help="Skip confirmation prompt",
    )
    args = parser.parse_args()

    base_dir = Path(__file__).parent.parent / "persona_api" / "data" / "text"
    behavioral_dir = Path(__file__).parent.parent / "persona_api" / "data" / "behavioral"

    # Check for required behavioral files
    missing = check_behavioral_files(behavioral_dir)
    if missing:
        print_dependency_error(missing, behavioral_dir)
        sys.exit(1)

    # Print preface (skip for dry run)
    if not args.dry_run:
        print_preface(base_dir, behavioral_dir, args.domain)

        # Confirmation
        if not args.yes:
            print("-" * 70)
            input("Press ENTER to continue, or Ctrl+C to cancel... ")
            print()

    # Load behavioral data
    print("Loading behavioral instruction files...")
    behavioral_data = load_behavioral_data(behavioral_dir)
    print(f"  Loaded {len(behavioral_data)} facet files\n")

    if args.dry_run:
        print("Dry run - counting files only\n")
    else:
        print(f"Generating files in {base_dir}\n")

    total = 0
    domains_processed = []
    domains_to_process = {args.domain: DOMAINS[args.domain]} if args.domain else DOMAINS

    for domain, facet_data in domains_to_process.items():
        facet_names = DOMAIN_FACETS[domain]
        count = generate_domain_files(
            base_dir,
            domain,
            facet_data,
            facet_names,
            behavioral_data,
            dry_run=args.dry_run,
        )
        print(f"  {domain}: {count} files")
        total += count
        domains_processed.append(domain)

    if args.dry_run:
        print(f"\nTotal: {total} files (dry run - no files created)")
    else:
        print_summary(base_dir, total, domains_processed)


if __name__ == "__main__":
    main()
