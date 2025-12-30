import argparse
import json

from persona_api.services import RandomFacetGenerator


def main():
    parser = argparse.ArgumentParser(description="Generate BFI-2 personality profiles")
    parser.add_argument("--seed", "-s", type=str, help="Seed for reproducible generation")
    parser.add_argument("--count", "-n", type=int, default=1, help="Number of profiles to generate")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    for i in range(args.count):
        gen = RandomFacetGenerator(seed=args.seed if args.count == 1 else None)
        result = gen.generate()

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

            print(f"Agreeableness: {result.agreeableness.score}")
            print(f"  compassion: {result.agreeableness.facets.compassion}")
            print(f"  respectfulness: {result.agreeableness.facets.respectfulness}")
            print(f"  trust: {result.agreeableness.facets.trust}")

            print(f"Conscientiousness: {result.conscientiousness.score}")
            print(f"  organization: {result.conscientiousness.facets.organization}")
            print(f"  productiveness: {result.conscientiousness.facets.productiveness}")
            print(f"  responsibility: {result.conscientiousness.facets.responsibility}")

            print(f"Negative Emotionality: {result.negative_emotionality.score}")
            print(f"  anxiety: {result.negative_emotionality.facets.anxiety}")
            print(f"  depression: {result.negative_emotionality.facets.depression}")
            print(f"  emotional_volatility: {result.negative_emotionality.facets.emotional_volatility}")

            print(f"Open-Mindedness: {result.open_mindedness.score}")
            print(f"  intellectual_curiosity: {result.open_mindedness.facets.intellectual_curiosity}")
            print(f"  aesthetic_sensitivity: {result.open_mindedness.facets.aesthetic_sensitivity}")
            print(f"  creative_imagination: {result.open_mindedness.facets.creative_imagination}")

            if args.count > 1:
                print()


if __name__ == "__main__":
    main()
