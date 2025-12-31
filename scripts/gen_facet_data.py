#!/usr/bin/env python3
"""Generate static Python data files from big5.owl for each BFI-2 facet.

This script parses the big5.owl ontology file and generates Python modules
containing static facet data. This is typically a one-time operation during
initial project setup.

Prerequisites:
    The big5.owl file must be present in the project root directory.
    This file contains the BFI-2 (Big Five Inventory-2) ontology with
    60 survey items across 15 facets.

Input:
    big5.owl - OWL/Turtle ontology file

Output:
    persona_api/data/facets/{facet}.py (15 files)
    persona_api/data/facets/__init__.py

Output Structure:
    Each facet file contains a DATA dict with:
    - name: Facet name (e.g., "Organization")
    - label: Display label
    - description: Facet description from ontology
    - survey_items: List of 4 survey items, each with:
        - id: Survey item ID (e.g., "BFI_NO_03")
        - prompt: LLM prompt template
        - ratings: Dict mapping score (1-5) to rating text

Usage:
    poetry run python scripts/gen_facet_data.py
    poetry run python scripts/gen_facet_data.py -y  # skip confirmation
"""

import argparse
import json
import sys
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS

NS = Namespace("http://modai.ai/big5#")

FACETS = {
    "sociability": "Sociability",
    "assertiveness": "Assertiveness",
    "energy_level": "Energy_Level",
    "compassion": "Compassion",
    "respectfulness": "Respectfulness",
    "trust": "Trust",
    "organization": "Organization",
    "productiveness": "Productiveness",
    "responsibility": "Responsibility",
    "anxiety": "Anxiety",
    "depression": "Depression",
    "emotional_volatility": "Emotional_Volatility",
    "intellectual_curiosity": "Intellectual_Curiosity",
    "aesthetic_sensitivity": "Aesthetic_Sensitivity",
    "creative_imagination": "Creative_Imagination",
}


def extract_facet_data(g: Graph, facet_uri: str) -> dict:
    """Extract all data for a single facet."""
    facet = NS[facet_uri]

    # Get facet metadata
    label = None
    comment = None
    see_also = None

    for _, _, o in g.triples((facet, RDFS.label, None)):
        label = str(o)
    for _, _, o in g.triples((facet, RDFS.comment, None)):
        comment = str(o)
    for _, _, o in g.triples((facet, RDFS.seeAlso, None)):
        see_also = str(o)

    # Get survey items (individuals of this facet type)
    survey_items = []
    for s, _, _ in g.triples((None, RDF.type, facet)):
        if "BFI_NO_" in str(s):
            item_data = extract_survey_item(g, s)
            if item_data:
                survey_items.append(item_data)

    # Get emotions associated with this facet
    emotions = []
    emotions_strong = []
    for s, _, _ in g.triples((None, RDF.type, facet)):
        for _, _, o in g.triples((s, NS.hasEmotion, None)):
            emo_name = str(o).split("#")[-1]
            if emo_name not in emotions:
                emotions.append(emo_name)
        for _, _, o in g.triples((s, NS.hasEmotionStrong, None)):
            emo_name = str(o).split("#")[-1]
            if emo_name not in emotions_strong:
                emotions_strong.append(emo_name)

    return {
        "name": facet_uri,
        "label": label,
        "description": comment,
        "see_also": see_also,
        "survey_items": sorted(survey_items, key=lambda x: x["id"]),
        "emotions": sorted(emotions),
        "emotions_strong": sorted(emotions_strong),
    }


def extract_survey_item(g: Graph, item_uri) -> dict | None:
    """Extract data for a single survey item."""
    item_id = str(item_uri).split("#")[-1]

    # Get the survey prompt from rdfs:comment
    prompt = None
    for _, _, o in g.triples((item_uri, RDFS.comment, None)):
        prompt = str(o)

    # Get ratings 1-5
    ratings = {}
    for i in range(1, 6):
        rating_prop = NS[f"surveyRating{i}"]
        for _, _, rating_uri in g.triples((item_uri, rating_prop, None)):
            # Get the survey text for this rating
            for _, _, survey_text in g.triples((rating_uri, NS.survey, None)):
                ratings[i] = str(survey_text)

    if not ratings:
        return None

    return {
        "id": item_id,
        "prompt": prompt,
        "ratings": ratings,
    }


def generate_facet_file(facet_key: str, data: dict, output_dir: Path) -> None:
    """Generate a Python file with static JSON data for a facet."""
    output_file = output_dir / f"{facet_key}.py"

    json_str = json.dumps(data, indent=2, ensure_ascii=False)

    content = f'''"""Static data for {data["label"]} facet."""

DATA = {json_str}
'''

    output_file.write_text(content)


def generate_init_file(output_dir: Path) -> None:
    """Generate __init__.py that exports all facet data."""
    imports = []
    exports = []

    for facet_key in sorted(FACETS.keys()):
        var_name = facet_key.upper()
        imports.append(f"from persona_api.data.facets.{facet_key} import DATA as {var_name}")
        exports.append(var_name)

    content = '''"""Static facet data extracted from big5.owl."""

'''
    content += "\n".join(imports)
    content += "\n\n__all__ = [\n"
    content += "".join(f'    "{e}",\n' for e in exports)
    content += "]\n"

    init_file = output_dir / "__init__.py"
    init_file.write_text(content)


def print_preface(owl_path: Path, output_dir: Path) -> None:
    """Print preface explaining what the script will do."""
    print("=" * 70)
    print("GENERATE FACET DATA")
    print("=" * 70)
    print()
    print("This script extracts BFI-2 facet data from the OWL ontology and")
    print("generates static Python modules for runtime use.")
    print()
    print("-" * 70)
    print("CONFIGURATION")
    print("-" * 70)
    print(f"  Input (OWL):  {owl_path}")
    print(f"  Output dir:   {output_dir}")
    print(f"  Facets:       {len(FACETS)}")
    print()
    print("-" * 70)
    print("PREREQUISITES")
    print("-" * 70)
    print("  The big5.owl file must be present in the project root.")
    print("  This is typically obtained from the BFI-2 ontology source.")
    print()
    print("-" * 70)
    print("OUTPUT")
    print("-" * 70)
    print("  This will generate 15 Python files + __init__.py:")
    for facet_key in sorted(FACETS.keys()):
        print(f"    - {facet_key}.py")
    print()


def print_summary(output_dir: Path, triple_count: int) -> None:
    """Print summary of what was done."""
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print(f"  OWL triples parsed: {triple_count}")
    print(f"  Facet files generated: {len(FACETS)}")
    print(f"  Output directory: {output_dir}")
    print()
    print("-" * 70)
    print("NEXT STEPS")
    print("-" * 70)
    print()
    print("  The facet data is now available for import:")
    print()
    print("    from persona_api.data.facets import ORGANIZATION, SOCIABILITY")
    print()
    print("  These files are typically generated once during initial setup.")
    print("  Regenerate only if big5.owl is updated.")
    print()
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Generate static Python data files from big5.owl for each BFI-2 facet.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s              Generate facet files with confirmation
  %(prog)s -y           Generate without confirmation

Note:
  This is typically a one-time operation during initial project setup.
  Regenerate only if the big5.owl ontology file is updated.
        """,
    )
    parser.add_argument(
        "-y", "--yes",
        action="store_true",
        help="Skip confirmation prompt",
    )
    args = parser.parse_args()

    # Paths
    owl_path = Path(__file__).parent.parent / "big5.owl"
    output_dir = Path(__file__).parent.parent / "persona_api" / "data" / "facets"

    # Check OWL file exists
    if not owl_path.exists():
        print("=" * 70)
        print("ERROR: OWL file not found")
        print("=" * 70)
        print()
        print(f"Expected: {owl_path}")
        print()
        print("The big5.owl file should be in the project root directory.")
        print("This file contains the BFI-2 ontology with personality facet definitions.")
        print()
        print("=" * 70)
        sys.exit(1)

    # Print preface
    print_preface(owl_path, output_dir)

    # Confirmation
    if not args.yes:
        print("-" * 70)
        input("Press ENTER to continue, or Ctrl+C to cancel... ")
        print()

    # Load OWL
    print(f"Loading {owl_path}...")
    g = Graph()
    g.parse(owl_path, format="turtle")
    print(f"  Loaded {len(g)} triples")

    # Generate files
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nGenerating facet files in {output_dir}...")
    for facet_key, facet_uri in FACETS.items():
        data = extract_facet_data(g, facet_uri)
        generate_facet_file(facet_key, data, output_dir)
        print(f"  Generated {facet_key}.py")

    generate_init_file(output_dir)
    print("  Generated __init__.py")

    # Print summary
    print_summary(output_dir, len(g))


if __name__ == "__main__":
    main()
