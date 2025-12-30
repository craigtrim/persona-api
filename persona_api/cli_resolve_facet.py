import argparse
import json

from persona_api.services import FacetTextResolver, RandomFacetGenerator


def main():
    parser = argparse.ArgumentParser(description="Resolve BFI-2 facet scores to descriptive text")
    parser.add_argument("--seed", "-s", type=str, help="Seed for reproducible generation")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    # Generate random facets
    gen = RandomFacetGenerator(seed=args.seed)
    result = gen.generate()

    # Convert to dict for resolver
    personality = {
        "extraversion": {
            "facets": {
                "sociability": result.extraversion.facets.sociability,
                "assertiveness": result.extraversion.facets.assertiveness,
                "energy_level": result.extraversion.facets.energy_level,
            }
        },
        "agreeableness": {
            "facets": {
                "compassion": result.agreeableness.facets.compassion,
                "respectfulness": result.agreeableness.facets.respectfulness,
                "trust": result.agreeableness.facets.trust,
            }
        },
        "conscientiousness": {
            "facets": {
                "organization": result.conscientiousness.facets.organization,
                "productiveness": result.conscientiousness.facets.productiveness,
                "responsibility": result.conscientiousness.facets.responsibility,
            }
        },
        "negative_emotionality": {
            "facets": {
                "anxiety": result.negative_emotionality.facets.anxiety,
                "depression": result.negative_emotionality.facets.depression,
                "emotional_volatility": result.negative_emotionality.facets.emotional_volatility,
            }
        },
        "open_mindedness": {
            "facets": {
                "intellectual_curiosity": result.open_mindedness.facets.intellectual_curiosity,
                "aesthetic_sensitivity": result.open_mindedness.facets.aesthetic_sensitivity,
                "creative_imagination": result.open_mindedness.facets.creative_imagination,
            }
        },
    }

    # Resolve to text
    resolver = FacetTextResolver(seed=args.seed)
    texts = resolver.resolve(personality)

    if args.json:
        output = {"seed": result.seed, "scores": personality, "texts": texts}
        print(json.dumps(output, indent=2))
    else:
        print(f"Seed: {result.seed}\n")

        for domain_name, domain_data in personality.items():
            print(f"{domain_name.replace('_', ' ').title()}:")
            facets = domain_data["facets"]
            domain_texts = texts.get(domain_name, {})

            for facet_name, score in facets.items():
                text = domain_texts.get(facet_name, "N/A")
                print(f"  {facet_name} ({score}): {text}")

            print()


if __name__ == "__main__":
    main()
