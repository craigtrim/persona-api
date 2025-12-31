"""Resolve domain scores to behavioral instructions."""

import json
import random
from pathlib import Path

# Domain -> ordered list of facet names
DOMAIN_FACETS = {
    "extraversion": ["sociability", "assertiveness", "energy_level"],
    "agreeableness": ["compassion", "respectfulness", "trust"],
    "conscientiousness": ["organization", "productiveness", "responsibility"],
    "negative_emotionality": ["anxiety", "depression", "emotional_volatility"],
    "open_mindedness": ["intellectual_curiosity", "aesthetic_sensitivity", "creative_imagination"],
}

DOMAINS = list(DOMAIN_FACETS.keys())


class BehaviorResolver:
    """Resolves domain scores to behavioral texts and instructions.

    Given a domain name (e.g., "extraversion") and a score (1-5),
    finds matching score combinations filtered by coherence level
    and returns a random text with its behavioral instructions.
    """

    def __init__(self, base_dir: Path | None = None, seed: str | None = None):
        if base_dir is None:
            base_dir = Path(__file__).parent.parent / "data" / "text"
        self._base_dir = base_dir
        self._rng = random.Random(seed)
        self._coherence_cache: dict[str, dict] = {}

    def _load_coherence_index(self, domain: str) -> dict:
        """Load and cache coherence index for a domain."""
        if domain not in self._coherence_cache:
            index_path = self._base_dir / domain / "coherence.json"
            if index_path.exists():
                self._coherence_cache[domain] = json.loads(index_path.read_text())
            else:
                self._coherence_cache[domain] = {"1": [], "2": [], "3": []}
        return self._coherence_cache[domain]

    def _get_matching_files(
        self,
        domain: str,
        score: int,
        coherence: int = 1,
    ) -> list[str]:
        """Get files matching the domain score and coherence level.

        A file matches if the average of its three facet scores rounds to
        the requested score.
        """
        index = self._load_coherence_index(domain)

        # Collect files at or below the coherence threshold
        # coherence=1 -> only "1", coherence=2 -> "1" and "2", etc.
        candidate_files = []
        for level in range(1, coherence + 1):
            candidate_files.extend(index.get(str(level), []))

        # Filter by score (average of the three facet scores)
        matching = []
        for file_path in candidate_files:
            # Parse scores from path like "3/2/4.json"
            parts = file_path.replace(".json", "").split("/")
            if len(parts) == 3:
                s1, s2, s3 = int(parts[0]), int(parts[1]), int(parts[2])
                avg = round((s1 + s2 + s3) / 3)
                if avg == score:
                    matching.append(file_path)

        return matching

    def resolve(
        self,
        domain: str,
        score: int,
        coherence: int = 1,
    ) -> dict | None:
        """Resolve domain score to behavioral text and instructions.

        Args:
            domain: Domain name (e.g., "extraversion", "conscientiousness").
            score: Target domain score (1-5).
            coherence: Maximum coherence level (1=coherent only, 2=include uncertain,
                       3=include contradictory). Defaults to 1.

        Returns:
            Dict with:
                - domain: The domain name
                - score: The requested score
                - facet_scores: The actual (score1, score2, score3) tuple used
                - coherence: The coherence rating of the selected file
                - text: A randomly selected personality text
                - instructions: Behavioral instructions for that text
            Or None if no matching files found.
        """
        if domain not in DOMAINS:
            return None

        if not 1 <= score <= 5:
            return None

        if not 1 <= coherence <= 3:
            coherence = 1

        matching_files = self._get_matching_files(domain, score, coherence)
        if not matching_files:
            return None

        # Pick a random file
        file_path = self._rng.choice(matching_files)
        full_path = self._base_dir / domain / file_path

        if not full_path.exists():
            return None

        content = json.loads(full_path.read_text())
        texts = content.get("texts", {})

        if not texts:
            return None

        # Pick a random text and its instructions
        text = self._rng.choice(list(texts.keys()))
        instructions = texts[text]

        # Parse facet scores from file path
        parts = file_path.replace(".json", "").split("/")
        facet_scores = tuple(int(p) for p in parts)

        return {
            "domain": domain,
            "score": score,
            "facet_scores": facet_scores,
            "coherence": content.get("coherence"),
            "text": text,
            "instructions": instructions,
        }

    def resolve_all(
        self,
        scores: dict[str, int],
        coherence: int = 1,
    ) -> dict[str, dict | None]:
        """Resolve multiple domain scores to behaviors.

        Args:
            scores: Dict mapping domain name to score (1-5).
            coherence: Maximum coherence level for all domains.

        Returns:
            Dict mapping domain name to result dict or None.
        """
        result = {}
        for domain, score in scores.items():
            result[domain] = self.resolve(domain, score, coherence)
        return result
