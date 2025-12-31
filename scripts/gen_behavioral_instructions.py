#!/usr/bin/env python3
"""Extract behavioral instructions from BFI-2 rating sentences using Ollama.

This script sends each of the 300 BFI-2 rating sentences to a local Ollama
instance to extract observable chatbot behaviors. The output is used by
subsequent scripts to generate personality-driven system prompts.

Prerequisites:
    1. Ollama must be installed and running on the target host
    2. A suitable model must be pulled (e.g., qwen2.5:7b)
    3. Ollama must be configured to accept network connections (see below)

Ollama Network Configuration:
    By default, Ollama only listens on localhost. To enable LAN access:

    1. Edit the systemd service file:
       $ sudo nano /etc/systemd/system/ollama.service

    2. Add this line under [Service]:
       Environment="OLLAMA_HOST=0.0.0.0"

    3. Reload and restart:
       $ sudo systemctl daemon-reload
       $ sudo systemctl restart ollama

    4. Verify it's listening on all interfaces:
       $ curl http://<host-ip>:11434/api/tags

Model Selection:
    This script was developed using qwen2.5:7b which provides good results
    for behavioral extraction. Other models may work but output quality varies.

    To pull the model on your Ollama host:
       $ ollama pull qwen2.5:7b

Output:
    persona_api/data/behavioral_instructions.json (flat file, 300 entries)

Next Steps:
    After running this script, run reorganize_behavioral_instructions.py
    to organize the output into per-facet files.

Usage:
    poetry run python scripts/gen_behavioral_instructions.py --host 192.168.4.98
    poetry run python scripts/gen_behavioral_instructions.py --dry-run
    poetry run python scripts/gen_behavioral_instructions.py --limit 10  # test run
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path

import requests

PROMPT_TEMPLATE = """You are extracting behavioral instructions from personality sentences. Output short phrases describing observable chatbot behaviors. Non-grammatical fragments are acceptable.

Return only a JSON array of phrases. No explanation.

---

Example 1:
Sentence: "I am impatient and tend to rush through explanations."
Output: ["skips details", "brief responses", "moves on quickly", "minimal elaboration"]

Example 2:
Sentence: "I am overly cautious and always hedge my statements."
Output: ["uses 'maybe' and 'perhaps'", "avoids certainty", "qualifies everything", "disclaimers on answers"]

Example 3:
Sentence: "I get distracted easily and lose track of the original question."
Output: ["goes on tangents", "forgets user intent", "topic drift", "circles back late"]

Example 4:
Sentence: "I am enthusiastic but sometimes overwhelming in my responses."
Output: ["exclamation marks", "excessive detail", "eager tone", "info dumps"]

Example 5:
Sentence: "I tend to be pessimistic and focus on what could go wrong."
Output: ["emphasizes risks", "negative framing", "warns often", "downplays positives"]

Example 6:
Sentence: "I am formal and never use casual language."
Output: ["no contractions", "stiff phrasing", "avoids slang", "professional register"]

---

Now extract behavioral instructions from this sentence:

Sentence: "{sentence}"
Output:"""


def parse_owl_file(owl_path: Path) -> list[dict]:
    """Parse OWL file to extract survey items with their ratings."""
    content = owl_path.read_text()

    # Find all survey rating nodes (e.g., BFI_NO_25_01)
    # Pattern: ###  http://modai.ai/big5#BFI_XX_YY_ZZ followed by ns:survey "sentence"
    # IDs have format: BFI_NO_01_01 (4 segments: BFI, NO, question#, rating#)
    pattern = r'###\s+http://modai\.ai/big5#(BFI_\w+_\d{2}_\d{2})\s*\n.*?ns:survey\s+"([^"]+)"'
    matches = re.findall(pattern, content, re.DOTALL)

    items = []
    for item_id, sentence in matches:
        # Extract base survey ID (e.g., BFI_NO_25 from BFI_NO_25_01)
        base_id = "_".join(item_id.rsplit("_", 1)[:-1])
        rating = int(item_id.rsplit("_", 1)[-1])

        items.append({
            "id": item_id,
            "base_id": base_id,
            "rating": rating,
            "sentence": sentence.strip(),
        })

    return items


def check_ollama_connection(host: str, model: str) -> tuple[bool, str]:
    """Check if Ollama is reachable and model is available."""
    try:
        response = requests.get(f"http://{host}:11434/api/tags", timeout=10)
        response.raise_for_status()
        data = response.json()

        available_models = [m["name"] for m in data.get("models", [])]

        if model not in available_models and f"{model}:latest" not in available_models:
            # Check if it's a partial match
            matching = [m for m in available_models if model.split(":")[0] in m]
            if matching:
                return True, f"Model '{model}' not found, but similar models available: {matching}"
            return False, f"Model '{model}' not found. Available: {available_models}"

        return True, "OK"

    except requests.exceptions.ConnectionError:
        return False, f"Cannot connect to Ollama at {host}:11434"
    except requests.exceptions.Timeout:
        return False, f"Connection to {host}:11434 timed out"
    except Exception as e:
        return False, str(e)


def query_ollama(host: str, sentence: str, model: str = "qwen2.5:7b") -> list[str]:
    """Query Ollama API for behavioral instructions."""
    url = f"http://{host}:11434/api/generate"

    payload = {
        "model": model,
        "prompt": PROMPT_TEMPLATE.format(sentence=sentence),
        "stream": False,
        "options": {
            "temperature": 0.3,
        },
    }

    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status()

    result = response.json()
    text = result.get("response", "").strip()

    # Parse JSON array from response
    try:
        # Find JSON array in response
        match = re.search(r"\[.*?\]", text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except json.JSONDecodeError:
        pass

    return []


def print_preface(args, owl_path: Path, output_path: Path, item_count: int) -> None:
    """Print preface explaining what the script will do."""
    print("=" * 70)
    print("BEHAVIORAL INSTRUCTION EXTRACTION")
    print("=" * 70)
    print()
    print("This script extracts observable chatbot behaviors from BFI-2 personality")
    print("sentences using a local Ollama LLM instance.")
    print()
    print("-" * 70)
    print("CONFIGURATION")
    print("-" * 70)
    print(f"  Ollama Host:     {args.host}")
    print(f"  Model:           {args.model}")
    print(f"  Input (OWL):     {owl_path}")
    print(f"  Output (JSON):   {output_path}")
    print(f"  Sentences:       {item_count}")
    if args.limit:
        print(f"  Limit:           {args.limit} (testing mode)")
    print()
    print("-" * 70)
    print("PREREQUISITES")
    print("-" * 70)
    print("  1. Ollama running on target host with network access enabled")
    print("  2. Model pulled: ollama pull qwen2.5:7b")
    print("  3. big5.owl file present in project root")
    print()
    print("-" * 70)
    print("WHAT HAPPENS NEXT")
    print("-" * 70)
    print("  After this script completes, run:")
    print("  $ poetry run python scripts/reorganize_behavioral_instructions.py")
    print()
    print("  This reorganizes the flat output into per-facet files needed by")
    print("  gen_domain_text_structure.py")
    print()


def print_summary(results: dict, output_path: Path, elapsed: float) -> None:
    """Print summary of what was done."""
    total = len(results)
    success = sum(1 for r in results.values() if r.get("instructions"))
    failed = total - success
    total_instructions = sum(len(r.get("instructions", [])) for r in results.values())

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print(f"  Sentences processed:    {total}")
    print(f"  Successful extractions: {success}")
    print(f"  Failed extractions:     {failed}")
    print(f"  Total instructions:     {total_instructions}")
    print(f"  Avg per sentence:       {total_instructions / max(success, 1):.1f}")
    print(f"  Time elapsed:           {elapsed:.1f}s ({elapsed / max(total, 1):.2f}s per sentence)")
    print()
    print(f"  Output saved to: {output_path}")
    print()
    print("-" * 70)
    print("NEXT STEPS")
    print("-" * 70)
    print()
    print("  1. Review the output for quality:")
    print(f"     $ head -50 {output_path}")
    print()
    print("  2. Reorganize into per-facet files:")
    print("     $ poetry run python scripts/reorganize_behavioral_instructions.py")
    print()
    print("  3. Generate domain text structure:")
    print("     $ poetry run python scripts/gen_domain_text_structure.py")
    print()
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Extract behavioral instructions from BFI-2 rating sentences using Ollama.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --host 192.168.4.98              Extract using remote Ollama
  %(prog)s --host localhost                 Extract using local Ollama
  %(prog)s --dry-run                        Preview sentences without LLM calls
  %(prog)s --limit 10                       Test with first 10 sentences
  %(prog)s --model mistral:latest           Use different model

Ollama Setup (on target host):
  1. Install: curl -fsSL https://ollama.com/install.sh | sh
  2. Pull model: ollama pull qwen2.5:7b
  3. Enable LAN access: Add 'Environment="OLLAMA_HOST=0.0.0.0"' to systemd service
        """,
    )
    parser.add_argument(
        "--host",
        type=str,
        default="192.168.4.98",
        help="Ollama host address (default: 192.168.4.98)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="qwen2.5:7b",
        help="Ollama model name (default: qwen2.5:7b)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview sentences without querying Ollama",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of items to process (for testing)",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file path (default: persona_api/data/behavioral_instructions.json)",
    )
    parser.add_argument(
        "-y", "--yes",
        action="store_true",
        help="Skip confirmation prompt",
    )
    args = parser.parse_args()

    # Paths
    base_dir = Path(__file__).parent.parent
    owl_path = base_dir / "big5.owl"
    output_path = Path(args.output) if args.output else base_dir / "persona_api" / "data" / "behavioral_instructions.json"

    # Check OWL file exists
    if not owl_path.exists():
        print(f"ERROR: OWL file not found: {owl_path}")
        print("\nThe big5.owl file should be in the project root directory.")
        sys.exit(1)

    # Parse OWL
    items = parse_owl_file(owl_path)
    if not items:
        print(f"ERROR: No survey items found in {owl_path}")
        sys.exit(1)

    if args.limit:
        items = items[:args.limit]

    # Dry run mode
    if args.dry_run:
        print("=" * 70)
        print("DRY RUN - Preview of sentences to process")
        print("=" * 70)
        print()
        for item in items:
            print(f"  {item['id']}: {item['sentence'][:70]}...")
        print()
        print(f"Total: {len(items)} sentences")
        print("\nRun without --dry-run to process these sentences.")
        return

    # Print preface
    print_preface(args, owl_path, output_path, len(items))

    # Check Ollama connection
    print("Checking Ollama connection...")
    ok, message = check_ollama_connection(args.host, args.model)
    if not ok:
        print(f"\nERROR: {message}")
        print()
        print("Troubleshooting:")
        print(f"  1. Verify Ollama is running: ssh {args.host} 'systemctl status ollama'")
        print(f"  2. Check network access: curl http://{args.host}:11434/api/tags")
        print(f"  3. Pull model if needed: ssh {args.host} 'ollama pull {args.model}'")
        print()
        print("See script docstring for Ollama network configuration instructions.")
        sys.exit(1)

    print(f"  Connection: OK")
    if message != "OK":
        print(f"  Note: {message}")
    print()

    # Confirmation
    if not args.yes:
        print("-" * 70)
        response = input("Press ENTER to continue, or Ctrl+C to cancel... ")
        print()

    # Process sentences
    print(f"Processing {len(items)} sentences...\n")
    start_time = time.time()
    results = {}

    for i, item in enumerate(items):
        print(f"[{i + 1}/{len(items)}] {item['id']}: ", end="", flush=True)

        try:
            instructions = query_ollama(args.host, item["sentence"], args.model)
            results[item["id"]] = {
                "sentence": item["sentence"],
                "base_id": item["base_id"],
                "rating": item["rating"],
                "instructions": instructions,
            }
            print(f"{len(instructions)} instructions")
        except Exception as e:
            print(f"ERROR: {e}")
            results[item["id"]] = {
                "sentence": item["sentence"],
                "base_id": item["base_id"],
                "rating": item["rating"],
                "instructions": [],
                "error": str(e),
            }

        # Small delay to avoid overwhelming the server
        time.sleep(0.1)

    elapsed = time.time() - start_time

    # Save results
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(results, indent=2))

    # Print summary
    print_summary(results, output_path, elapsed)


if __name__ == "__main__":
    main()
