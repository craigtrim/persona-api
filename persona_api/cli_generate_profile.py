"""CLI for generating chatbot personality profiles."""

import argparse
import json
import sys

from persona_api.services import DomainTextResolver, ProfileGenerator, RandomFacetGenerator

DEFAULT_TRAIT_COUNT = 5
DEFAULT_DOMAIN_SCORE = 3  # Neutral score for unspecified domains

# Domain display prefixes (single letter)
DOMAIN_PREFIX = {
    "extraversion": "E",
    "agreeableness": "A",
    "conscientiousness": "C",
    "negative_emotionality": "N",
    "open_mindedness": "O",
}

# Score-based emoji gradients (1-5 scale)
# Each domain has emojis that visually indicate the polarity/intensity
DOMAIN_EMOJI_GRADIENT = {
    # Negative Emotionality: calm (1) → anxious (5)
    "negative_emotionality": {1: "😌", 2: "🙂", 3: "😐", 4: "😟", 5: "😰"},
    # Extraversion: reserved (1) → energetic (5)
    "extraversion": {1: "🌑", 2: "🌒", 3: "🌓", 4: "🌔", 5: "🌕"},
    # Agreeableness: challenging (1) → warm (5)
    "agreeableness": {1: "🧊", 2: "❄️", 3: "🌥️", 4: "🌤️", 5: "☀️"},
    # Conscientiousness: flexible (1) → disciplined (5)
    "conscientiousness": {1: "🌀", 2: "😅", 3: "📝", 4: "📋", 5: "🎯"},
    # Open-mindedness: conventional (1) → creative (5)
    "open_mindedness": {1: "📦", 2: "📐", 3: "🔍", 4: "🎨", 5: "🌈"},
}

# Unicode subscript digits for score display
SUBSCRIPT_DIGITS = {1: "₁", 2: "₂", 3: "₃", 4: "₄", 5: "₅"}

# Consistent domain order for display (A, C, E, O, N)
DOMAIN_ORDER = [
    "agreeableness",
    "conscientiousness",
    "extraversion",
    "open_mindedness",
    "negative_emotionality",
]

# Map flag letters to domain names
FLAG_TO_DOMAIN = {
    "A": "agreeableness",
    "C": "conscientiousness",
    "E": "extraversion",
    "O": "open_mindedness",
    "N": "negative_emotionality",
}

# Short labels for mode description (shows what each letter means)
DOMAIN_SHORT_LABEL = {
    "agreeableness": "Agreeable",
    "conscientiousness": "Conscientious",
    "extraversion": "Extravert",
    "open_mindedness": "Open",
    "negative_emotionality": "Neurotic",
}

# Random mode descriptions
RANDOM_DESC = {
    1: "coherent (facets within ±1)",
    2: "mixed (moderate spread ±2)",
    3: "chaotic (large spread ≥3)",
}


def check_domain_flag_typos(args: list[str]) -> str | None:
    """Check for common domain flag typos and return helpful message."""
    import re
    for arg in args:
        # Match patterns like --A3, --E2, --N1 (missing space)
        match = re.match(r"^--([ACEON])(\d)$", arg)
        if match:
            flag, num = match.groups()
            return f"Did you mean '--{flag} {num}' (with a space)?"

        # Match lowercase domain flags
        match = re.match(r"^--([aceon])(?:\s+(\d))?$", arg)
        if match:
            flag = match.group(1).upper()
            return f"Domain flags must be uppercase. Use '--{flag}' instead of '--{flag.lower()}'."

    return None


def main():
    # Check for common typos before parsing
    typo_hint = check_domain_flag_typos(sys.argv[1:])

    parser = argparse.ArgumentParser(
        description="""
Generate chatbot personality profiles from BFI-2 (Big Five) traits.

This tool creates system prompts that instruct an LLM to embody a specific
personality. You can either specify domain scores explicitly or use random
generation with a coherence level.
        """.strip(),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
─────────────────────────────────────────────────────────────────────────────
MODES
─────────────────────────────────────────────────────────────────────────────
  You must use EITHER --random OR domain flags (--A, --C, --E, --N, --O).

  Random mode:    All domain scores are randomly generated.
  Explicit mode:  You set domain scores; unspecified domains default to 3.

─────────────────────────────────────────────────────────────────────────────
RANDOM MODE  (--random {1,2,3})
─────────────────────────────────────────────────────────────────────────────
  1  Coherent   Facets align (±1). Produces consistent personalities.
  2  Mixed      Moderate spread (±2). Some internal tension.
  3  Chaotic    Large spread (≥3). Conflicting traits for complex personas.

─────────────────────────────────────────────────────────────────────────────
DOMAIN FLAGS  (set score level 1-5)
─────────────────────────────────────────────────────────────────────────────
  --A {1-5}  🧊→☀️  Agreeableness      1=cold, 5=warm
  --C {1-5}  🌀→🎯  Conscientiousness  1=flexible, 5=disciplined
  --E {1-5}  🌑→🌕  Extraversion       1=reserved, 5=energetic
  --O {1-5}  📦→🌈  Open-mindedness    1=conventional, 5=creative
  --N {1-5}  😌→😰  Negative emotion   1=calm, 5=anxious

  Unspecified domains default to 3 (neutral).

─────────────────────────────────────────────────────────────────────────────
EXAMPLES
─────────────────────────────────────────────────────────────────────────────
  %(prog)s --random 1
      Random coherent personality

  %(prog)s --random 3
      Random chaotic personality with conflicting traits

  %(prog)s --N 5 --A 1
      High neuroticism, low agreeableness (E=3, C=3, O=3)

  %(prog)s --E 5 --O 5 --N 1
      Energetic, creative, calm personality

  %(prog)s --N 5 --dry-run
      Preview traits without calling Ollama

  %(prog)s --random 1 --json
      Random generation with JSON output
        """,
    )
    parser.add_argument(
        "--seed", "-s",
        type=str,
        metavar="STR",
        help="Seed for reproducible generation (any string)",
    )
    parser.add_argument(
        "--random", "-r",
        type=int,
        choices=[1, 2, 3],
        metavar="{1,2,3}",
        help="Random generation: 1=coherent, 2=mixed, 3=chaotic",
    )
    # Domain-specific score flags
    for flag, domain in FLAG_TO_DOMAIN.items():
        parser.add_argument(
            f"--{flag}",
            type=int,
            choices=[1, 2, 3, 4, 5],
            metavar="{1-5}",
            help=argparse.SUPPRESS,
        )
    parser.add_argument(
        "--model", "-m",
        type=str,
        default="llama3.2",
        metavar="NAME",
        help="Ollama model for profile generation (default: llama3.2)",
    )
    parser.add_argument(
        "--host",
        type=str,
        default="sparx",
        metavar="HOST",
        help="SSH host running Ollama (default: sparx)",
    )
    parser.add_argument(
        "--length", "-l",
        type=int,
        metavar="CHARS",
        help="Target profile length in characters (±10%%, max ~600)",
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output full result as JSON (includes facets, traits, profile)",
    )
    parser.add_argument(
        "--dry-run", "-d",
        action="store_true",
        help="Preview traits and prompt without calling Ollama",
    )

    # Parse with custom error handling
    try:
        args = parser.parse_args()
    except SystemExit as e:
        if e.code != 0 and typo_hint:
            print(f"\n💡 Hint: {typo_hint}", file=sys.stderr)
        raise

    # Collect domain scores from flags
    domain_scores = {}
    for flag, domain in FLAG_TO_DOMAIN.items():
        score = getattr(args, flag, None)
        if score is not None:
            domain_scores[domain] = score

    has_domain_flags = len(domain_scores) > 0
    has_random = args.random is not None

    # Validate: must use --random XOR domain flags
    if has_random and has_domain_flags:
        print("Error: Cannot use --random with domain flags (--A, --C, --E, --N, --O).", file=sys.stderr)
        print("", file=sys.stderr)
        print("Use --random for fully random generation, or domain flags for explicit scores.", file=sys.stderr)
        sys.exit(1)

    if not has_random and not has_domain_flags:
        print("Error: Must specify either --random or at least one domain flag.", file=sys.stderr)
        print("", file=sys.stderr)
        print("Examples:", file=sys.stderr)
        print("  generate-profile --random 1          # Random coherent personality", file=sys.stderr)
        print("  generate-profile --N 5 --A 1         # Explicit: high N, low A", file=sys.stderr)
        print("", file=sys.stderr)
        print("Run with --help for full usage.", file=sys.stderr)
        sys.exit(1)

    # Determine mode and build facet scores
    if has_random:
        # Random mode: generate all domains randomly
        facet_gen = RandomFacetGenerator(seed=args.seed)
        result = facet_gen.generate(coherence=args.random)
        seed = result.seed

        facet_scores = {
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
        }
        mode_desc = f"Random: {args.random} - {RANDOM_DESC[args.random]}"
    else:
        # Explicit mode: use provided scores, default others to 3
        # For explicit mode, we set all three facets to the same score
        seed = args.seed or f"{hash(tuple(sorted(domain_scores.items()))) % 1000000:06d}"

        facet_scores = {}
        for domain in FLAG_TO_DOMAIN.values():
            score = domain_scores.get(domain, DEFAULT_DOMAIN_SCORE)
            facet_scores[domain] = (score, score, score)

        specified = [f"{DOMAIN_PREFIX[d]}({DOMAIN_SHORT_LABEL[d]})={s}" for d, s in domain_scores.items()]
        mode_desc = f"Explicit: {', '.join(specified)}" if specified else "Explicit: all neutral"

    # Resolve behaviors for all domains
    resolver = DomainTextResolver(seed=seed)
    behaviors = resolver.resolve_all(facet_scores)

    # Slice traits (always 5, distributed across domains with behaviors)
    profile_gen = ProfileGenerator(seed=seed)
    traits = profile_gen.slice_instructions(behaviors, count=DEFAULT_TRAIT_COUNT)

    def get_domain_score(domain: str) -> int:
        """Get the rounded average score for a domain (1-5)."""
        scores = facet_scores[domain]
        return round(sum(scores) / len(scores))

    def format_traits_display():
        """Format traits with score-based emoji and subscript in consistent order."""
        # Sort traits by domain order
        sorted_traits = sorted(traits, key=lambda t: DOMAIN_ORDER.index(t["domain"]))
        lines = []
        for t in sorted_traits:
            domain = t["domain"]
            score = get_domain_score(domain)
            emoji = DOMAIN_EMOJI_GRADIENT[domain][score]
            prefix = DOMAIN_PREFIX[domain]
            subscript = SUBSCRIPT_DIGITS[score]
            lines.append(f"  {prefix}{subscript} {emoji} | {t['trait']}")
        return "\n".join(lines)

    def get_emoji_summary() -> str:
        """Get unique emojis from traits in domain order."""
        seen = set()
        emojis = []
        for domain in DOMAIN_ORDER:
            # Check if any trait uses this domain
            if any(t["domain"] == domain for t in traits):
                score = get_domain_score(domain)
                emoji = DOMAIN_EMOJI_GRADIENT[domain][score]
                if emoji not in seen:
                    seen.add(emoji)
                    emojis.append(emoji)
        return "".join(emojis)

    if args.dry_run:
        prompt = profile_gen.generate_prompt(traits, length=args.length)
        if args.json:
            output = {
                "seed": seed,
                "mode": "random" if has_random else "explicit",
                "domain_scores": {DOMAIN_PREFIX[d]: get_domain_score(d) for d in DOMAIN_ORDER},
                "facets": {d: list(s) for d, s in facet_scores.items()},
                "traits": traits,
                "prompt": prompt,
            }
            if has_random:
                output["coherence"] = args.random
            if args.length:
                output["target_length"] = args.length
            print(json.dumps(output, indent=2))
        else:
            print(f"Seed: {seed}")
            print(f"Mode: {mode_desc}")
            if args.length:
                print(f"Target length: ~{args.length} chars")
            print(f"\nTraits ({len(traits)}): {get_emoji_summary()}")
            print(format_traits_display())
            print(f"\nPrompt:\n{prompt}")
        return

    # Generate profile via Ollama
    try:
        profile = profile_gen.generate_profile(
            traits,
            model=args.model,
            host=args.host,
            length=args.length,
        )
    except Exception as e:
        print(f"Error calling Ollama: {e}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        output = {
            "seed": seed,
            "mode": "random" if has_random else "explicit",
            "domain_scores": {DOMAIN_PREFIX[d]: get_domain_score(d) for d in DOMAIN_ORDER},
            "facets": {d: list(s) for d, s in facet_scores.items()},
            "traits": traits,
            "profile": profile,
            "profile_length": len(profile),
        }
        if has_random:
            output["coherence"] = args.random
        if args.length:
            output["target_length"] = args.length
        print(json.dumps(output, indent=2))
    else:
        print(f"Seed: {seed}")
        print(f"Mode: {mode_desc}")
        print(f"\nTraits ({len(traits)}): {get_emoji_summary()}")
        print(format_traits_display())
        print(f"\nProfile ({len(profile)} chars):\n{profile}")


if __name__ == "__main__":
    main()
