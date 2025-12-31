#!/usr/bin/env python3
"""Generate coherence ratings documentation for all score combinations.

This script generates a markdown document showing the coherence rating
for every possible (score1, score2, score3) facet score combination.
This is useful for understanding which personality configurations are
psychometrically coherent vs. contradictory.

Coherence Rating Scale:
    1 = Coherent    - All facets in same direction or within +/-1
    2 = Uncertain   - Moderate spread (+/-2)
    3 = Contradictory - Outlier >=3 points from others

Each domain has 5^3 = 125 possible score combinations.
Total across all 5 domains: 625 combinations.

Output:
    docs/score-coherence.md

Usage:
    poetry run python scripts/gen_score_coherence.py
    poetry run python scripts/gen_score_coherence.py -y  # skip confirmation
"""

import argparse
import sys
from itertools import product
from pathlib import Path

DOMAINS = {
    "extraversion": ["sociability", "assertiveness", "energy_level"],
    "agreeableness": ["compassion", "respectfulness", "trust"],
    "conscientiousness": ["organization", "productiveness", "responsibility"],
    "negative_emotionality": ["anxiety", "depression", "emotional_volatility"],
    "open_mindedness": ["intellectual_curiosity", "aesthetic_sensitivity", "creative_imagination"],
}

SCORES = range(1, 6)


def rate_coherence(scores: tuple[int, int, int]) -> int:
    """Rate coherence of a score combination.

    Returns:
        1 = coherent
        2 = uncertain
        3 = contradictory
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
    # e.g., (1, 1, 5) or (5, 5, 1)
    sorted_scores = sorted(scores)

    # If two scores are close and one is far
    if sorted_scores[1] - sorted_scores[0] <= 1 and sorted_scores[2] - sorted_scores[1] >= 3:
        return 3
    if sorted_scores[2] - sorted_scores[1] <= 1 and sorted_scores[1] - sorted_scores[0] >= 3:
        return 3

    # General large spread
    if spread >= 3:
        return 3

    return 2


def generate_domain_ratings(domain: str, facets: list[str]) -> list[dict]:
    """Generate ratings for all 125 score combos in a domain."""
    results = []

    for scores in product(SCORES, repeat=3):
        rating = rate_coherence(scores)
        results.append({
            "scores": scores,
            "rating": rating,
            "path": f"{scores[0]}/{scores[1]}/{scores[2]}.json",
        })

    return results


def print_preface(output_path: Path) -> None:
    """Print preface explaining what the script will do."""
    print("=" * 70)
    print("GENERATE SCORE COHERENCE DOCUMENTATION")
    print("=" * 70)
    print()
    print("This script generates documentation showing coherence ratings for all")
    print("possible facet score combinations in the BFI-2 personality model.")
    print()
    print("-" * 70)
    print("CONFIGURATION")
    print("-" * 70)
    print(f"  Output:        {output_path}")
    print(f"  Domains:       {len(DOMAINS)}")
    print(f"  Combinations:  {len(DOMAINS) * (5 ** 3)} total (125 per domain)")
    print()
    print("-" * 70)
    print("COHERENCE RATINGS")
    print("-" * 70)
    print("  1 = Coherent      All facets same direction or within +/-1")
    print("  2 = Uncertain     Moderate spread (+/-2)")
    print("  3 = Contradictory Outlier >=3 points from others")
    print()
    print("-" * 70)
    print("PURPOSE")
    print("-" * 70)
    print("  This documentation helps identify which personality configurations")
    print("  are psychometrically valid vs. internally contradictory.")
    print()
    print("  Example contradictory: (1, 1, 5) - two low scores, one high")
    print("  Example coherent: (4, 5, 4) - all high scores")
    print()


def print_summary(summary: dict, output_path: Path) -> None:
    """Print summary of what was done."""
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("  Distribution of coherence ratings:")
    print(f"    Coherent (1):      {summary['1']:3d} combinations ({summary['1'] / 625 * 100:.1f}%)")
    print(f"    Uncertain (2):     {summary['2']:3d} combinations ({summary['2'] / 625 * 100:.1f}%)")
    print(f"    Contradictory (3): {summary['3']:3d} combinations ({summary['3'] / 625 * 100:.1f}%)")
    print(f"    Total:             {sum(summary.values())} combinations")
    print()
    print(f"  Output saved to: {output_path}")
    print()
    print("-" * 70)
    print("INTERPRETATION")
    print("-" * 70)
    print()
    print("  A high percentage of contradictory combinations is expected -")
    print("  real personality profiles tend to have correlated facets.")
    print()
    print("  The gen_domain_text_structure.py script uses these ratings to flag")
    print("  potentially unrealistic personality configurations.")
    print()
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Generate coherence ratings documentation for all score combinations.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s              Generate documentation with confirmation
  %(prog)s -y           Generate without confirmation

Coherence Ratings:
  1 = Coherent      - All facets same direction or within +/-1
  2 = Uncertain     - Moderate spread (+/-2)
  3 = Contradictory - Outlier >=3 points from others
        """,
    )
    parser.add_argument(
        "-y", "--yes",
        action="store_true",
        help="Skip confirmation prompt",
    )
    args = parser.parse_args()

    # Path
    output_path = Path(__file__).parent.parent / "docs" / "score-coherence.md"

    # Print preface
    print_preface(output_path)

    # Confirmation
    if not args.yes:
        print("-" * 70)
        input("Press ENTER to continue, or Ctrl+C to cancel... ")
        print()

    # Generate
    print("Generating coherence ratings...")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Score Combination Coherence Ratings",
        "",
        "Rates each (facet1, facet2, facet3) score combination on a 1-3 scale:",
        "",
        "- **1** = Coherent (all same direction or within +/-1)",
        "- **2** = Uncertain (moderate spread, +/-2)",
        "- **3** = Contradictory (outlier >=3 points from others)",
        "",
    ]

    summary = {"1": 0, "2": 0, "3": 0}

    for domain, facets in DOMAINS.items():
        lines.append(f"## {domain.replace('_', ' ').title()}")
        lines.append("")
        lines.append(f"Facets: {', '.join(facets)}")
        lines.append("")
        lines.append("| Scores | Path | Rating |")
        lines.append("|--------|------|--------|")

        ratings = generate_domain_ratings(domain, facets)

        domain_summary = {"1": 0, "2": 0, "3": 0}

        for r in ratings:
            scores_str = f"({r['scores'][0]}, {r['scores'][1]}, {r['scores'][2]})"
            rating_str = str(r["rating"])
            lines.append(f"| {scores_str} | {r['path']} | {rating_str} |")

            domain_summary[rating_str] += 1
            summary[rating_str] += 1

        lines.append("")
        lines.append(f"**Domain summary:** {domain_summary['1']} coherent, {domain_summary['2']} uncertain, {domain_summary['3']} contradictory")
        lines.append("")

    # Overall summary
    lines.insert(8, "## Summary")
    lines.insert(9, "")
    lines.insert(10, f"- Coherent (1): {summary['1']} combinations")
    lines.insert(11, f"- Uncertain (2): {summary['2']} combinations")
    lines.insert(12, f"- Contradictory (3): {summary['3']} combinations")
    lines.insert(13, f"- Total: {sum(summary.values())} combinations")
    lines.insert(14, "")

    output_path.write_text("\n".join(lines))

    # Print summary
    print_summary(summary, output_path)


if __name__ == "__main__":
    main()
