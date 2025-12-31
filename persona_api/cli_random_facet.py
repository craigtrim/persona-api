import argparse
import json
import random
import sys

from persona_api.services import DomainTextResolver, RandomFacetGenerator

MAX_INSTRUCTIONS = 5

COHERENCE_WARNING = """
WARNING: No coherence level specified.

Without --coherence, facet scores are generated randomly and may produce
contradictory behavioral instructions (e.g., both "dominant tone" and
"prefers listening" in the same profile).

Coherence levels:
  1 = Coherent (facets within ±1 of each other)
  2 = Uncertain (moderate spread, ±2)
  3 = Contradictory (large spread, ≥3)

Press ENTER to continue with random coherence, or Ctrl+C to cancel...
"""


def sample_instructions(instructions: list[str], rng: random.Random) -> list[str]:
    """Sample up to MAX_INSTRUCTIONS from the list."""
    if len(instructions) <= MAX_INSTRUCTIONS:
        return instructions
    return rng.sample(instructions, MAX_INSTRUCTIONS)


def main():
    parser = argparse.ArgumentParser(description="Generate BFI-2 personality profiles")
    parser.add_argument("--seed", "-s", type=str, help="Seed for reproducible generation")
    parser.add_argument("--count", "-n", type=int, default=1, help="Number of profiles to generate")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    parser.add_argument("--behaviors", "-b", action="store_true", help="Include behavioral instructions")
    parser.add_argument(
        "--coherence", "-c",
        type=int,
        choices=[1, 2, 3],
        help="Coherence level: 1=coherent, 2=uncertain, 3=contradictory",
    )
    args = parser.parse_args()

    # Warn if coherence not specified
    if args.coherence is None:
        if sys.stdin.isatty():
            print(COHERENCE_WARNING, file=sys.stderr)
            try:
                input()
            except KeyboardInterrupt:
                print("\nCancelled.", file=sys.stderr)
                sys.exit(1)

    for i in range(args.count):
        gen = RandomFacetGenerator(seed=args.seed if args.count == 1 else None)
        result = gen.generate(coherence=args.coherence)

        # Create a shared RNG for sampling instructions (same seed for reproducibility)
        rng = random.Random(result.seed)

        # Resolve behaviors if requested
        behaviors = None
        if args.behaviors:
            resolver = DomainTextResolver(seed=result.seed)
            raw_behaviors = resolver.resolve_all({
                "extraversion": (
                    result.extraversion.facets.sociability,
                    result.extraversion.facets.assertiveness,
                    result.extraversion.facets.energy_level,
                ),
                "agreeableness": (
                    result.agreeableness.facets.compassion,
                    result.agreeableness.facets.respectfulness,
                    result.agreeableness.facets.trust,
                ),
                "conscientiousness": (
                    result.conscientiousness.facets.organization,
                    result.conscientiousness.facets.productiveness,
                    result.conscientiousness.facets.responsibility,
                ),
                "negative_emotionality": (
                    result.negative_emotionality.facets.anxiety,
                    result.negative_emotionality.facets.depression,
                    result.negative_emotionality.facets.emotional_volatility,
                ),
                "open_mindedness": (
                    result.open_mindedness.facets.intellectual_curiosity,
                    result.open_mindedness.facets.aesthetic_sensitivity,
                    result.open_mindedness.facets.creative_imagination,
                ),
            })

            # Sample instructions for each domain
            behaviors = {}
            for domain, behavior in raw_behaviors.items():
                if behavior:
                    behaviors[domain] = {
                        "coherence": behavior["coherence"],
                        "text": behavior["text"],
                        "instructions": sample_instructions(behavior["instructions"], rng),
                    }
                else:
                    behaviors[domain] = None

        if args.json:
            output = {
                "seed": result.seed,
                "extraversion": {
                    "score": result.extraversion.score,
                    "facets": {
                        "sociability": result.extraversion.facets.sociability,
                        "assertiveness": result.extraversion.facets.assertiveness,
                        "energy_level": result.extraversion.facets.energy_level,
                    },
                },
                "agreeableness": {
                    "score": result.agreeableness.score,
                    "facets": {
                        "compassion": result.agreeableness.facets.compassion,
                        "respectfulness": result.agreeableness.facets.respectfulness,
                        "trust": result.agreeableness.facets.trust,
                    },
                },
                "conscientiousness": {
                    "score": result.conscientiousness.score,
                    "facets": {
                        "organization": result.conscientiousness.facets.organization,
                        "productiveness": result.conscientiousness.facets.productiveness,
                        "responsibility": result.conscientiousness.facets.responsibility,
                    },
                },
                "negative_emotionality": {
                    "score": result.negative_emotionality.score,
                    "facets": {
                        "anxiety": result.negative_emotionality.facets.anxiety,
                        "depression": result.negative_emotionality.facets.depression,
                        "emotional_volatility": result.negative_emotionality.facets.emotional_volatility,
                    },
                },
                "open_mindedness": {
                    "score": result.open_mindedness.score,
                    "facets": {
                        "intellectual_curiosity": result.open_mindedness.facets.intellectual_curiosity,
                        "aesthetic_sensitivity": result.open_mindedness.facets.aesthetic_sensitivity,
                        "creative_imagination": result.open_mindedness.facets.creative_imagination,
                    },
                },
            }
            if behaviors:
                for domain, behavior in behaviors.items():
                    if behavior:
                        output[domain]["behavior"] = {
                            "text": behavior["text"],
                            "instructions": behavior["instructions"],
                            "coherence": behavior["coherence"],
                        }
            print(json.dumps(output, indent=2))
        else:
            if args.count > 1:
                print(f"--- Profile {i + 1} (seed: {result.seed}) ---")
            else:
                print(f"Seed: {result.seed}\n")

            print(f"Extraversion: {result.extraversion.score}")
            print(f"  sociability: {result.extraversion.facets.sociability}")
            print(f"  assertiveness: {result.extraversion.facets.assertiveness}")
            print(f"  energy_level: {result.extraversion.facets.energy_level}")
            if behaviors and behaviors.get("extraversion"):
                b = behaviors["extraversion"]
                print(f"  instructions: {', '.join(b['instructions'])}")

            print(f"Agreeableness: {result.agreeableness.score}")
            print(f"  compassion: {result.agreeableness.facets.compassion}")
            print(f"  respectfulness: {result.agreeableness.facets.respectfulness}")
            print(f"  trust: {result.agreeableness.facets.trust}")
            if behaviors and behaviors.get("agreeableness"):
                b = behaviors["agreeableness"]
                print(f"  instructions: {', '.join(b['instructions'])}")

            print(f"Conscientiousness: {result.conscientiousness.score}")
            print(f"  organization: {result.conscientiousness.facets.organization}")
            print(f"  productiveness: {result.conscientiousness.facets.productiveness}")
            print(f"  responsibility: {result.conscientiousness.facets.responsibility}")
            if behaviors and behaviors.get("conscientiousness"):
                b = behaviors["conscientiousness"]
                print(f"  instructions: {', '.join(b['instructions'])}")

            print(f"Negative Emotionality: {result.negative_emotionality.score}")
            print(f"  anxiety: {result.negative_emotionality.facets.anxiety}")
            print(f"  depression: {result.negative_emotionality.facets.depression}")
            print(f"  emotional_volatility: {result.negative_emotionality.facets.emotional_volatility}")
            if behaviors and behaviors.get("negative_emotionality"):
                b = behaviors["negative_emotionality"]
                print(f"  instructions: {', '.join(b['instructions'])}")

            print(f"Open-Mindedness: {result.open_mindedness.score}")
            print(f"  intellectual_curiosity: {result.open_mindedness.facets.intellectual_curiosity}")
            print(f"  aesthetic_sensitivity: {result.open_mindedness.facets.aesthetic_sensitivity}")
            print(f"  creative_imagination: {result.open_mindedness.facets.creative_imagination}")
            if behaviors and behaviors.get("open_mindedness"):
                b = behaviors["open_mindedness"]
                print(f"  instructions: {', '.join(b['instructions'])}")

            if args.count > 1:
                print()


if __name__ == "__main__":
    main()
