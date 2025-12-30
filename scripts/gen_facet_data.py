#!/usr/bin/env python3
"""Generate static JSON data files from big5.owl for each BFI-2 facet."""

import json
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
    print(f"  Generated {output_file.name}")


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
    print(f"  Generated __init__.py")


def main():
    owl_path = Path(__file__).parent.parent / "big5.owl"
    output_dir = Path(__file__).parent.parent / "persona_api" / "data" / "facets"

    print(f"Loading {owl_path}...")
    g = Graph()
    g.parse(owl_path, format="turtle")
    print(f"  Loaded {len(g)} triples")

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nGenerating facet files in {output_dir}...")
    for facet_key, facet_uri in FACETS.items():
        data = extract_facet_data(g, facet_uri)
        generate_facet_file(facet_key, data, output_dir)

    generate_init_file(output_dir)

    print("\nDone!")


if __name__ == "__main__":
    main()
