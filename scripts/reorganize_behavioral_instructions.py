#!/usr/bin/env python3
"""Reorganize behavioral instructions into per-facet JSON files.

This script takes the flat behavioral_instructions.json output from
gen_behavioral_instructions.py and reorganizes it into 15 separate
files, one per BFI-2 facet.

Prerequisites:
    Run gen_behavioral_instructions.py first to generate the input file.

Input:
    persona_api/data/behavioral_instructions.json (flat file, 300 entries)

Output:
    persona_api/data/behavioral/{facet}.json (15 files, 4 survey items each)

Output Structure:
    {
        "facet": "organization",
        "survey_items": [
            {
                "id": "BFI_NO_03",
                "ratings": {
                    "1": {"sentence": "...", "instructions": [...]},
                    "2": {"sentence": "...", "instructions": [...]},
                    ...
                }
            }
        ]
    }

Next Steps:
    After running this script, run gen_domain_text_structure.py to generate
    the final domain text files with behavioral instructions included.

Usage:
    poetry run python scripts/reorganize_behavioral_instructions.py
    poetry run python scripts/reorganize_behavioral_instructions.py -y  # skip confirmation
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


def check_input_file(instructions_path: Path) -> tuple[bool, str]:
    """Check if input file exists and is valid."""
    if not instructions_path.exists():
        return False, f"Input file not found: {instructions_path}"

    try:
        data = json.loads(instructions_path.read_text())
        if not data:
            return False, "Input file is empty"
        return True, f"Found {len(data)} entries"
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"


def parse_survey_facet_mapping(owl_path: Path) -> dict[str, str]:
    """Parse OWL to get survey item -> facet mapping."""
    content = owl_path.read_text()

    # Pattern: ns:BFI_NO_XX rdf:type owl:NamedIndividual ,\n                      ns:FacetName ;
    pattern = r"ns:(BFI_NO_\d{2})\s+rdf:type\s+owl:NamedIndividual\s*,\s*ns:(\w+)\s*;"
    matches = re.findall(pattern, content)

    return {item_id: facet.lower() for item_id, facet in matches}


def reorganize_instructions(
    instructions_path: Path,
    owl_path: Path,
    output_dir: Path,
) -> dict[str, int]:
    """Reorganize flat instructions into per-facet files."""
    # Load flat instructions
    instructions = json.loads(instructions_path.read_text())

    # Get survey -> facet mapping
    survey_to_facet = parse_survey_facet_mapping(owl_path)

    # Group by facet
    facets: dict[str, dict[str, dict]] = defaultdict(lambda: defaultdict(dict))
    warnings = []

    for item_id, data in instructions.items():
        base_id = data["base_id"]
        rating = str(data["rating"])

        facet = survey_to_facet.get(base_id)
        if not facet:
            warnings.append(f"No facet found for {base_id}")
            continue

        facets[facet][base_id][rating] = {
            "sentence": data["sentence"],
            "instructions": data["instructions"],
        }

    # Write per-facet files
    output_dir.mkdir(parents=True, exist_ok=True)
    counts = {}

    for facet, survey_items in sorted(facets.items()):
        output = {
            "facet": facet,
            "survey_items": [],
        }

        for survey_id in sorted(survey_items.keys()):
            ratings = survey_items[survey_id]
            output["survey_items"].append({
                "id": survey_id,
                "ratings": dict(sorted(ratings.items())),
            })

        output_path = output_dir / f"{facet}.json"
        output_path.write_text(json.dumps(output, indent=2))
        counts[facet] = len(output["survey_items"])

    return counts, warnings


def print_preface(instructions_path: Path, owl_path: Path, output_dir: Path) -> None:
    """Print preface explaining what the script will do."""
    print("=" * 70)
    print("REORGANIZE BEHAVIORAL INSTRUCTIONS")
    print("=" * 70)
    print()
    print("This script reorganizes the flat behavioral_instructions.json file")
    print("into 15 separate per-facet JSON files for use by gen_domain_text_structure.py")
    print()
    print("-" * 70)
    print("CONFIGURATION")
    print("-" * 70)
    print(f"  Input:      {instructions_path}")
    print(f"  OWL file:   {owl_path}")
    print(f"  Output dir: {output_dir}")
    print()
    print("-" * 70)
    print("PREREQUISITES")
    print("-" * 70)
    print("  Run gen_behavioral_instructions.py first to generate the input file.")
    print()
    print("-" * 70)
    print("WHAT HAPPENS NEXT")
    print("-" * 70)
    print("  After this script completes, run:")
    print("  $ poetry run python scripts/gen_domain_text_structure.py")
    print()
    print("  This generates the final domain text files with behavioral")
    print("  instructions included.")
    print()


def print_summary(counts: dict[str, int], warnings: list[str], output_dir: Path) -> None:
    """Print summary of what was done."""
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("Generated files:")
    for facet, count in sorted(counts.items()):
        print(f"  {facet}.json: {count} survey items")
    print()
    print(f"Total: {len(counts)} facet files")

    if warnings:
        print()
        print("Warnings:")
        for w in warnings:
            print(f"  - {w}")

    print()
    print("-" * 70)
    print("NEXT STEPS")
    print("-" * 70)
    print()
    print("  1. Review generated files:")
    print(f"     $ ls -la {output_dir}")
    print()
    print("  2. Generate domain text structure:")
    print("     $ poetry run python scripts/gen_domain_text_structure.py")
    print()
    print("  3. The flat behavioral_instructions.json can now be deleted:")
    print("     $ rm persona_api/data/behavioral_instructions.json")
    print()
    print("=" * 70)


def print_dependency_error(instructions_path: Path) -> None:
    """Print helpful error message about missing input file."""
    print("=" * 70)
    print("ERROR: Missing required input file")
    print("=" * 70)
    print()
    print(f"Expected: {instructions_path}")
    print()
    print("-" * 70)
    print("HOW TO FIX")
    print("-" * 70)
    print()
    print("Run gen_behavioral_instructions.py first to generate the input file:")
    print()
    print("  $ poetry run python scripts/gen_behavioral_instructions.py --host <ollama-host>")
    print()
    print("This sends BFI-2 rating sentences to Ollama to extract behavioral")
    print("instructions. Requires Ollama running with a model like qwen2.5:7b.")
    print()
    print("For testing, you can limit to a few sentences:")
    print("  $ poetry run python scripts/gen_behavioral_instructions.py --host <host> --limit 10")
    print()
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Reorganize behavioral instructions into per-facet JSON files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                Reorganize with confirmation prompt
  %(prog)s -y             Reorganize without confirmation

Prerequisites:
  Run gen_behavioral_instructions.py first to generate the input file.
        """,
    )
    parser.add_argument(
        "-y", "--yes",
        action="store_true",
        help="Skip confirmation prompt",
    )
    args = parser.parse_args()

    # Paths
    base_dir = Path(__file__).parent.parent
    instructions_path = base_dir / "persona_api" / "data" / "behavioral_instructions.json"
    owl_path = base_dir / "big5.owl"
    output_dir = base_dir / "persona_api" / "data" / "behavioral"

    # Check input file exists
    ok, message = check_input_file(instructions_path)
    if not ok:
        print_dependency_error(instructions_path)
        sys.exit(1)

    # Check OWL file exists
    if not owl_path.exists():
        print(f"ERROR: OWL file not found: {owl_path}")
        print("\nThe big5.owl file should be in the project root directory.")
        sys.exit(1)

    # Print preface
    print_preface(instructions_path, owl_path, output_dir)

    print(f"Input validation: {message}")
    print()

    # Confirmation
    if not args.yes:
        print("-" * 70)
        input("Press ENTER to continue, or Ctrl+C to cancel... ")
        print()

    # Reorganize
    print("Reorganizing instructions...")
    counts, warnings = reorganize_instructions(instructions_path, owl_path, output_dir)

    # Print summary
    print_summary(counts, warnings, output_dir)


if __name__ == "__main__":
    main()
