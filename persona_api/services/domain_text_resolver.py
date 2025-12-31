import json
import random
from pathlib import Path


class DomainTextResolver:
    """Resolves domain facet configurations to pre-computed text summaries."""

    def __init__(self, base_dir: Path | None = None, seed: str | None = None):
        if base_dir is None:
            base_dir = Path(__file__).parent.parent / "data" / "text"
        self._base_dir = base_dir
        self._rng = random.Random(seed)

    def get_file_path(self, domain: str, scores: tuple[int, int, int]) -> Path:
        """Get file path for a score combination."""
        return self._base_dir / domain / str(scores[0]) / str(scores[1]) / f"{scores[2]}.json"

    def resolve(
        self,
        domain: str,
        scores: tuple[int, int, int],
    ) -> dict | None:
        """Resolve domain configuration to text summary with instructions.

        Args:
            domain: Domain name (e.g., "conscientiousness").
            scores: Tuple of (score1, score2, score3) for each facet (1-5).

        Returns:
            Dict with coherence rating, random text, and its instructions,
            or None if not found/empty.
        """
        file_path = self.get_file_path(domain, scores)

        if not file_path.exists():
            return None

        content = json.loads(file_path.read_text())
        texts = content.get("texts", {})

        if not texts:
            return None

        # texts is now dict[str, list[str]] - pick a random key
        text = self._rng.choice(list(texts.keys()))
        instructions = texts[text]

        return {
            "coherence": content.get("coherence"),
            "text": text,
            "instructions": instructions,
        }

    def resolve_all(
        self,
        personality: dict[str, tuple[int, int, int]],
    ) -> dict[str, dict | None]:
        """Resolve all domains to text summaries.

        Args:
            personality: Dict mapping domain name to score tuple.

        Returns:
            Dict mapping domain name to result dict (coherence + text) or None.
        """
        result = {}
        for domain, scores in personality.items():
            result[domain] = self.resolve(domain, scores)
        return result
