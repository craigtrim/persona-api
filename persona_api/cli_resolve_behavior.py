"""CLI for resolving domain scores to behavioral instructions."""

import argparse
import json

from persona_api.services import BehaviorResolver

DOMAINS = [
    "extraversion",
    "agreeableness",
    "conscientiousness",
    "negative_emotionality",
    "open_mindedness",
]


def main():
    parser = argparse.ArgumentParser(
        description="Resolve BFI-2 domain scores to behavioral instructions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s extraversion 4
  %(prog)s conscientiousness 2 --coherence 2
  %(prog)s negative_emotionality 5 --json
  %(prog)s --all 3,2,4,3,5
  %(prog)s --seed abc123 extraversion 3

Domains:
  extraversion, agreeableness, conscientiousness,
  negative_emotionality, open_mindedness
        """,
    )
    parser.add_argument(
        "domain",
        nargs="?",
        choices=DOMAINS,
        help="Domain name to resolve",
    )
    parser.add_argument(
        "score",
        nargs="?",
        type=int,
        choices=[1, 2, 3, 4, 5],
        help="Domain score (1-5)",
    )
    parser.add_argument(
        "--coherence", "-c",
        type=int,
        choices=[1, 2, 3],
        default=1,
        help="Max coherence level: 1=coherent, 2=+uncertain, 3=+contradictory (default: 1)",
    )
    parser.add_argument(
        "--all", "-a",
        type=str,
        metavar="SCORES",
        help="Resolve all domains with comma-separated scores (e.g., 3,2,4,3,5)",
    )
    parser.add_argument(
        "--seed", "-s",
        type=str,
        help="Seed for reproducible random selection",
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output as JSON",
    )
    args = parser.parse_args()

    resolver = BehaviorResolver(seed=args.seed)

    # Handle --all mode
    if args.all:
        scores_list = [int(s.strip()) for s in args.all.split(",")]
        if len(scores_list) != 5:
            parser.error("--all requires exactly 5 comma-separated scores")

        scores = dict(zip(DOMAINS, scores_list))
        results = resolver.resolve_all(scores, coherence=args.coherence)

        if args.json:
            output = {}
            for domain, result in results.items():
                if result:
                    output[domain] = {
                        "score": result["score"],
                        "facet_scores": result["facet_scores"],
                        "coherence": result["coherence"],
                        "text": result["text"],
                        "instructions": result["instructions"],
                    }
                else:
                    output[domain] = None
            print(json.dumps(output, indent=2))
        else:
            for domain, result in results.items():
                print(f"\n{'=' * 60}")
                print(f"{domain.upper().replace('_', ' ')} (score: {scores[domain]})")
                print("=" * 60)
                if result:
                    print(f"Facet scores: {result['facet_scores']}")
                    print(f"Coherence: {result['coherence']}")
                    print(f"\nText:\n  {result['text']}")
                    print(f"\nInstructions:")
                    for inst in result["instructions"]:
                        print(f"  - {inst}")
                else:
                    print("  No matching configuration found")
        return

    # Single domain mode
    if not args.domain or args.score is None:
        parser.error("domain and score are required (or use --all)")

    result = resolver.resolve(args.domain, args.score, coherence=args.coherence)

    if args.json:
        if result:
            output = {
                "domain": result["domain"],
                "score": result["score"],
                "facet_scores": result["facet_scores"],
                "coherence": result["coherence"],
                "text": result["text"],
                "instructions": result["instructions"],
            }
        else:
            output = None
        print(json.dumps(output, indent=2))
    else:
        if result:
            print(f"Domain: {result['domain']}")
            print(f"Score: {result['score']}")
            print(f"Facet scores: {result['facet_scores']}")
            print(f"Coherence: {result['coherence']}")
            print(f"\nText:\n  {result['text']}")
            print(f"\nInstructions:")
            for inst in result["instructions"]:
                print(f"  - {inst}")
        else:
            print(f"No matching configuration found for {args.domain} score {args.score}")


if __name__ == "__main__":
    main()
