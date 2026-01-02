#!/usr/bin/env python3
"""Generate focused prompts for individual personality keywords using Ollama.

This script:
1. Extracts all unique keywords from persona_api/data/text/<domain>/**/*.json
2. Groups keywords by domain
3. Queries Ollama to generate a focused system prompt for each keyword
4. Saves output to persona_api/data/keyword_prompts.json

The output is used by the persona-ui to show focused prompts when a user
clicks on a specific keyword in the slider back panel.

Prerequisites:
    1. Ollama must be running on sparx (192.168.4.98)
    2. qwen2.5:7b model must be pulled

Usage:
    poetry run python scripts/gen_keyword_prompts.py --host 192.168.4.98
    poetry run python scripts/gen_keyword_prompts.py --dry-run
    poetry run python scripts/gen_keyword_prompts.py --domain extraversion --limit 10
"""

import argparse
import json
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

import requests

# Domain to facet mapping
DOMAIN_FACETS = {
    "agreeableness": ["Compassion", "Respectfulness", "Trust"],
    "conscientiousness": ["Organization", "Productiveness", "Responsibility"],
    "extraversion": ["Sociability", "Assertiveness", "Energy_Level"],
    "negative_emotionality": ["Anxiety", "Depression", "Emotional_Volatility"],
    "open_mindedness": ["Intellectual_Curiosity", "Aesthetic_Sensitivity", "Creative_Imagination"],
}

PROMPT_TEMPLATE = """You are writing a focused system prompt instruction for an AI chatbot.

The chatbot is being configured to exhibit a specific personality trait keyword. Write a concise 1-2 sentence instruction that tells the chatbot how to embody ONLY this specific behavioral trait in its responses.

The instruction should:
- Be written as a direct instruction to the chatbot (use "you" or imperative voice)
- Focus ONLY on the specific keyword given
- Be concise but specific about observable behavior
- NOT include the keyword itself in quotes or as a label

Domain: {domain}
Keyword: "{keyword}"

Write the focused instruction:"""


def extract_unique_keywords(data_dir: Path, domain_filter: str | None = None) -> dict[str, set[str]]:
    """Extract unique keywords from all JSON files, grouped by domain.

    Returns:
        Dict mapping domain name to set of unique keywords
    """
    keywords_by_domain: dict[str, set[str]] = defaultdict(set)

    domains = [domain_filter] if domain_filter else DOMAIN_FACETS.keys()

    for domain in domains:
        domain_dir = data_dir / domain
        if not domain_dir.exists():
            print(f"Warning: Missing domain directory: {domain_dir}")
            continue

        for json_file in domain_dir.rglob("*.json"):
            try:
                with open(json_file) as f:
                    content = json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not read {json_file}: {e}")
                continue

            texts = content.get("texts", {})
            for keyword_list in texts.values():
                for keyword in keyword_list:
                    # Only include clean ASCII keywords
                    if all(ord(c) < 128 for c in keyword):
                        keywords_by_domain[domain].add(keyword)

    return keywords_by_domain


def check_ollama_connection(host: str, model: str) -> tuple[bool, str]:
    """Check if Ollama is reachable and model is available."""
    try:
        response = requests.get(f"http://{host}:11434/api/tags", timeout=10)
        response.raise_for_status()
        data = response.json()

        available_models = [m["name"] for m in data.get("models", [])]

        if model not in available_models and f"{model}:latest" not in available_models:
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


def query_ollama(host: str, domain: str, keyword: str, model: str = "qwen2.5:7b") -> str:
    """Query Ollama API for a focused prompt for the given keyword."""
    url = f"http://{host}:11434/api/generate"

    payload = {
        "model": model,
        "prompt": PROMPT_TEMPLATE.format(domain=domain, keyword=keyword),
        "stream": False,
        "options": {
            "temperature": 0.4,
        },
    }

    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status()

    result = response.json()
    text = result.get("response", "").strip()

    # Clean up the response - remove any leading/trailing quotes
    text = text.strip('"\'')

    return text


def print_preface(args, data_dir: Path, output_path: Path, keywords_by_domain: dict) -> None:
    """Print preface explaining what the script will do."""
    total_keywords = sum(len(kws) for kws in keywords_by_domain.values())

    print("=" * 70)
    print("KEYWORD PROMPT GENERATION")
    print("=" * 70)
    print()
    print("This script generates focused system prompts for individual personality")
    print("keywords using Ollama. These prompts are shown when a user clicks on a")
    print("specific keyword in the persona-ui slider panel.")
    print()
    print("-" * 70)
    print("CONFIGURATION")
    print("-" * 70)
    print(f"  Ollama Host:     {args.host}")
    print(f"  Model:           {args.model}")
    print(f"  Data Directory:  {data_dir}")
    print(f"  Output File:     {output_path}")
    print()
    print("-" * 70)
    print("KEYWORDS BY DOMAIN")
    print("-" * 70)
    for domain, keywords in sorted(keywords_by_domain.items()):
        print(f"  {domain}: {len(keywords)} unique keywords")
    print(f"  TOTAL: {total_keywords} keywords")
    print()
    if args.limit:
        print(f"  Limit: {args.limit} keywords per domain (testing mode)")
        print()


def print_summary(results: dict, output_path: Path, elapsed: float) -> None:
    """Print summary of what was done."""
    total = sum(len(kws) for kws in results.values())

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    for domain, keywords in sorted(results.items()):
        print(f"  {domain}: {len(keywords)} prompts generated")
    print()
    print(f"  Total prompts:      {total}")
    print(f"  Time elapsed:       {elapsed:.1f}s ({elapsed / max(total, 1):.2f}s per keyword)")
    print()
    print(f"  Output saved to: {output_path}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Generate focused prompts for personality keywords using Ollama.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--host",
        type=str,
        default="192.168.4.98",
        help="Ollama host address (default: 192.168.4.98 / sparx)",
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
        help="Preview keywords without querying Ollama",
    )
    parser.add_argument(
        "--domain",
        type=str,
        choices=list(DOMAIN_FACETS.keys()),
        help="Process only this domain (for testing)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit keywords per domain (for testing)",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file path (default: persona_api/data/keyword_prompts.json)",
    )
    parser.add_argument(
        "-y", "--yes",
        action="store_true",
        help="Skip confirmation prompt",
    )
    args = parser.parse_args()

    # Paths
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "persona_api" / "data" / "text"
    output_path = Path(args.output) if args.output else base_dir / "persona_api" / "data" / "keyword_prompts.json"

    # Check data directory exists
    if not data_dir.exists():
        print(f"ERROR: Data directory not found: {data_dir}")
        sys.exit(1)

    # Extract unique keywords
    print("Extracting unique keywords from JSON files...")
    keywords_by_domain = extract_unique_keywords(data_dir, args.domain)

    if not any(keywords_by_domain.values()):
        print("ERROR: No keywords found in data files")
        sys.exit(1)

    # Apply limit if specified
    if args.limit:
        for domain in keywords_by_domain:
            keywords_by_domain[domain] = set(list(keywords_by_domain[domain])[:args.limit])

    # Dry run mode
    if args.dry_run:
        print("=" * 70)
        print("DRY RUN - Preview of keywords to process")
        print("=" * 70)
        for domain, keywords in sorted(keywords_by_domain.items()):
            print(f"\n{domain.upper()} ({len(keywords)} keywords):")
            for kw in sorted(keywords)[:10]:
                print(f"  - {kw}")
            if len(keywords) > 10:
                print(f"  ... and {len(keywords) - 10} more")
        print()
        total = sum(len(kws) for kws in keywords_by_domain.values())
        print(f"Total: {total} keywords")
        print("\nRun without --dry-run to generate prompts.")
        return

    # Print preface
    print_preface(args, data_dir, output_path, keywords_by_domain)

    # Check Ollama connection
    print("Checking Ollama connection...")
    ok, message = check_ollama_connection(args.host, args.model)
    if not ok:
        print(f"\nERROR: {message}")
        sys.exit(1)

    print(f"  Connection: OK")
    if message != "OK":
        print(f"  Note: {message}")
    print()

    # Confirmation
    if not args.yes:
        print("-" * 70)
        input("Press ENTER to continue, or Ctrl+C to cancel... ")
        print()

    # Process keywords
    total_keywords = sum(len(kws) for kws in keywords_by_domain.values())
    print(f"Processing {total_keywords} keywords...\n")

    start_time = time.time()
    results: dict[str, dict[str, str]] = defaultdict(dict)
    processed = 0

    for domain, keywords in sorted(keywords_by_domain.items()):
        print(f"\n{domain.upper()}:")
        for keyword in sorted(keywords):
            processed += 1
            print(f"  [{processed}/{total_keywords}] {keyword}: ", end="", flush=True)

            try:
                prompt = query_ollama(args.host, domain, keyword, args.model)
                results[domain][keyword] = prompt
                # Show truncated preview
                preview = prompt[:50] + "..." if len(prompt) > 50 else prompt
                print(f"OK - {preview}")
            except Exception as e:
                print(f"ERROR: {e}")
                results[domain][keyword] = f"Error: {e}"

            # Small delay to avoid overwhelming the server
            time.sleep(0.1)

    elapsed = time.time() - start_time

    # Save results
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(dict(results), indent=2, sort_keys=True))

    # Print summary
    print_summary(results, output_path, elapsed)


if __name__ == "__main__":
    main()
