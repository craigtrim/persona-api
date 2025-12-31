#!/usr/bin/env python3
"""Extract discriminating keywords for each BFI-2 facet at each score level.

Uses TF-IDF analysis to find keywords that best distinguish each facet's
score levels (1-5) from others. Output is used for the personality slider UI.

Related: https://github.com/craigtrim/persona-api/issues/1
"""

import json
import math
from collections import defaultdict
from pathlib import Path


# Domain to facet mapping (order matches file path structure)
DOMAIN_FACETS = {
    "agreeableness": ["Compassion", "Respectfulness", "Trust"],
    "conscientiousness": ["Organization", "Productiveness", "Responsibility"],
    "extraversion": ["Sociability", "Assertiveness", "Energy_Level"],
    "negative_emotionality": ["Anxiety", "Depression", "Emotional_Volatility"],
    "open_mindedness": ["Intellectual_Curiosity", "Aesthetic_Sensitivity", "Creative_Imagination"],
}

DATA_DIR = Path(__file__).parent.parent.parent / "persona_api" / "data" / "text"
OUTPUT_FILE = Path(__file__).parent.parent / "data" / "facet_keywords.json"


def load_all_instructions() -> dict:
    """Load all instruction keywords from JSON files.

    Returns:
        Dict structure: {domain: {facet_idx: {score: [keywords]}}}
    """
    data = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    for domain, facets in DOMAIN_FACETS.items():
        domain_dir = DATA_DIR / domain
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

            meta = content.get("_meta", {})
            scores = meta.get("scores", [])
            texts = content.get("texts", {})

            if len(scores) != 3:
                continue

            # Collect all keywords from this file
            all_keywords = []
            for keyword_list in texts.values():
                all_keywords.extend(keyword_list)

            # Associate keywords with each facet's score
            for facet_idx, score in enumerate(scores):
                data[domain][facet_idx][score].extend(all_keywords)

    return data


def compute_tf(keywords: list[str]) -> dict[str, float]:
    """Compute term frequency for keywords."""
    counts = defaultdict(int)
    for kw in keywords:
        counts[kw] += 1
    total = len(keywords)
    return {kw: count / total for kw, count in counts.items()}


def compute_idf(keyword: str, all_docs: list[list[str]]) -> float:
    """Compute inverse document frequency."""
    n_docs = len(all_docs)
    n_containing = sum(1 for doc in all_docs if keyword in doc)
    if n_containing == 0:
        return 0
    return math.log(n_docs / n_containing)


def compute_tfidf_scores(data: dict) -> dict:
    """Compute TF-IDF scores for each facet/score combination.

    Returns:
        Dict: {domain: {facet_name: {score: [(keyword, tfidf_score), ...]}}}
    """
    results = {}

    for domain, facets in DOMAIN_FACETS.items():
        results[domain] = {}
        domain_data = data.get(domain, {})

        for facet_idx, facet_name in enumerate(facets):
            facet_data = domain_data.get(facet_idx, {})
            results[domain][facet_name] = {}

            # Build document list (one per score level)
            all_docs = []
            score_keywords = {}
            for score in range(1, 6):
                keywords = facet_data.get(score, [])
                score_keywords[score] = keywords
                all_docs.append(keywords)

            # Compute TF-IDF for each score level
            for score in range(1, 6):
                keywords = score_keywords[score]
                if not keywords:
                    results[domain][facet_name][score] = []
                    continue

                tf = compute_tf(keywords)
                tfidf_scores = {}

                for kw in set(keywords):
                    idf = compute_idf(kw, all_docs)
                    tfidf_scores[kw] = tf[kw] * idf

                # Sort by TF-IDF score descending
                sorted_keywords = sorted(
                    tfidf_scores.items(),
                    key=lambda x: x[1],
                    reverse=True
                )

                results[domain][facet_name][score] = sorted_keywords

    return results


def is_clean_english(text: str) -> bool:
    """Check if text is clean English (no non-ASCII characters)."""
    return all(ord(c) < 128 for c in text)


def extract_top_keywords(tfidf_results: dict, top_n: int = 5) -> dict:
    """Extract top N keywords for each facet/score.

    Returns:
        Dict: {domain: {facet_name: {score: [keyword1, keyword2, ...]}}}
    """
    output = {}

    for domain, facets in tfidf_results.items():
        output[domain] = {}
        for facet_name, scores in facets.items():
            output[domain][facet_name] = {}
            for score, keywords in scores.items():
                # Take top N, filter out zero scores and non-English text
                top = [kw for kw, s in keywords if s > 0 and is_clean_english(kw)][:top_n]
                output[domain][facet_name][score] = top

    return output


def print_summary(results: dict):
    """Print a human-readable summary of results."""
    for domain, facets in results.items():
        print(f"\n{'='*60}")
        print(f"DOMAIN: {domain.upper()}")
        print(f"{'='*60}")

        for facet_name, scores in facets.items():
            print(f"\n  {facet_name}:")
            for score in range(1, 6):
                keywords = scores.get(score, [])
                kw_str = ", ".join(keywords[:3]) if keywords else "(none)"
                print(f"    {score}: {kw_str}")


def main():
    print("Loading instruction data from JSON files...")
    data = load_all_instructions()

    # Count files loaded
    total_keywords = 0
    for domain, facet_data in data.items():
        for facet_idx, score_data in facet_data.items():
            for score, keywords in score_data.items():
                total_keywords += len(keywords)
    print(f"Loaded {total_keywords:,} keyword occurrences")

    print("\nComputing TF-IDF scores...")
    tfidf_results = compute_tfidf_scores(data)

    print("Extracting top keywords per facet/score...")
    top_keywords = extract_top_keywords(tfidf_results, top_n=5)

    # Print summary
    print_summary(top_keywords)

    # Save output
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(top_keywords, f, indent=2)
    print(f"\nSaved results to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
