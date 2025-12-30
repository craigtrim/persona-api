import random
from typing import Any

from persona_api.data.facets import (
    AESTHETIC_SENSITIVITY,
    ANXIETY,
    ASSERTIVENESS,
    COMPASSION,
    CREATIVE_IMAGINATION,
    DEPRESSION,
    EMOTIONAL_VOLATILITY,
    ENERGY_LEVEL,
    INTELLECTUAL_CURIOSITY,
    ORGANIZATION,
    PRODUCTIVENESS,
    RESPECTFULNESS,
    RESPONSIBILITY,
    SOCIABILITY,
    TRUST,
)

FACET_DATA = {
    "sociability": SOCIABILITY,
    "assertiveness": ASSERTIVENESS,
    "energy_level": ENERGY_LEVEL,
    "compassion": COMPASSION,
    "respectfulness": RESPECTFULNESS,
    "trust": TRUST,
    "organization": ORGANIZATION,
    "productiveness": PRODUCTIVENESS,
    "responsibility": RESPONSIBILITY,
    "anxiety": ANXIETY,
    "depression": DEPRESSION,
    "emotional_volatility": EMOTIONAL_VOLATILITY,
    "intellectual_curiosity": INTELLECTUAL_CURIOSITY,
    "aesthetic_sensitivity": AESTHETIC_SENSITIVITY,
    "creative_imagination": CREATIVE_IMAGINATION,
}


class FacetTextResolver:
    """Resolves facet scores to descriptive text from BFI-2 survey items."""

    def __init__(self, seed: str | None = None):
        self._rng = random.Random(seed)

    def _get_texts_for_score(self, facet_name: str, score: int) -> list[str]:
        """Get all rating texts for a given facet and score."""
        data = FACET_DATA.get(facet_name)
        if not data:
            return []

        texts = []
        score_key = str(score)
        for item in data.get("survey_items", []):
            ratings = item.get("ratings", {})
            if score_key in ratings:
                texts.append(ratings[score_key])

        return texts

    def resolve_facet(self, facet_name: str, score: int) -> str | None:
        """Return a random text description for the given facet and score."""
        texts = self._get_texts_for_score(facet_name, score)
        if not texts:
            return None
        return self._rng.choice(texts)

    def resolve(self, personality: dict[str, Any]) -> dict[str, dict[str, str]]:
        """Resolve all facet scores to text descriptions.

        Args:
            personality: dict with structure {domain: {facets: {facet_name: score}}}

        Returns:
            dict with structure {domain: {facet_name: text}}
        """
        result = {}

        for domain_name, domain_data in personality.items():
            if domain_name == "seed":
                continue

            facets = domain_data.get("facets", {})
            result[domain_name] = {}

            for facet_name, score in facets.items():
                text = self.resolve_facet(facet_name, score)
                if text:
                    result[domain_name][facet_name] = text

        return result
