import random
from dataclasses import dataclass


def _domain_score(f1: int, f2: int, f3: int) -> int:
    """Compute domain score as rounded average of facets."""
    return round((f1 + f2 + f3) / 3)


@dataclass
class ExtraversionFacets:
    sociability: int
    assertiveness: int
    energy_level: int


@dataclass
class AgreeablenessFacets:
    compassion: int
    respectfulness: int
    trust: int


@dataclass
class ConscientiousnessFacets:
    organization: int
    productiveness: int
    responsibility: int


@dataclass
class NegativeEmotionalityFacets:
    anxiety: int
    depression: int
    emotional_volatility: int


@dataclass
class OpenMindednessFacets:
    intellectual_curiosity: int
    aesthetic_sensitivity: int
    creative_imagination: int


@dataclass
class ExtraversionResult:
    score: int
    facets: ExtraversionFacets


@dataclass
class AgreeablenessResult:
    score: int
    facets: AgreeablenessFacets


@dataclass
class ConscientiousnessResult:
    score: int
    facets: ConscientiousnessFacets


@dataclass
class NegativeEmotionalityResult:
    score: int
    facets: NegativeEmotionalityFacets


@dataclass
class OpenMindednessResult:
    score: int
    facets: OpenMindednessFacets


@dataclass
class PersonalityResult:
    extraversion: ExtraversionResult
    agreeableness: AgreeablenessResult
    conscientiousness: ConscientiousnessResult
    negative_emotionality: NegativeEmotionalityResult
    open_mindedness: OpenMindednessResult
    seed: str


class RandomFacetGenerator:
    """Generates random BFI-2 personality scores."""

    def __init__(self, seed: str | None = None):
        self._seed = seed or self._generate_seed()
        self._rng = random.Random(self._seed)

    def _generate_seed(self) -> str:
        return f"{random.randint(0, 999999):06d}"

    def _random_facet(self, bias: int = 0) -> int:
        """Generate a random facet score (1-5) with optional bias."""
        score = self._rng.randint(1, 5) + bias
        return max(1, min(5, score))

    def _generate_negative_emotionality(self) -> NegativeEmotionalityFacets:
        """Generate N facets first (anchor for correlations)."""
        return NegativeEmotionalityFacets(
            anxiety=self._random_facet(),
            depression=self._random_facet(),
            emotional_volatility=self._random_facet(),
        )

    def _n_bias(self, n_facets: NegativeEmotionalityFacets) -> int:
        """Compute bias based on negative emotionality (high N -> lower E, A, C)."""
        n_avg = (n_facets.anxiety + n_facets.depression + n_facets.emotional_volatility) / 3
        if n_avg >= 4:
            return -1
        if n_avg <= 2:
            return 1
        return 0

    def _generate_extraversion(self, bias: int = 0) -> ExtraversionFacets:
        return ExtraversionFacets(
            sociability=self._random_facet(bias),
            assertiveness=self._random_facet(bias),
            energy_level=self._random_facet(bias),
        )

    def _generate_agreeableness(self, bias: int = 0) -> AgreeablenessFacets:
        return AgreeablenessFacets(
            compassion=self._random_facet(bias),
            respectfulness=self._random_facet(bias),
            trust=self._random_facet(bias),
        )

    def _generate_conscientiousness(self, bias: int = 0) -> ConscientiousnessFacets:
        return ConscientiousnessFacets(
            organization=self._random_facet(bias),
            productiveness=self._random_facet(bias),
            responsibility=self._random_facet(bias),
        )

    def _generate_open_mindedness(self, bias: int = 0) -> OpenMindednessFacets:
        return OpenMindednessFacets(
            intellectual_curiosity=self._random_facet(bias),
            aesthetic_sensitivity=self._random_facet(bias),
            creative_imagination=self._random_facet(bias),
        )

    def generate(self) -> PersonalityResult:
        """Generate a complete personality profile with correlated traits."""
        # Generate negative emotionality first (anchor trait for correlations)
        n_facets = self._generate_negative_emotionality()
        n_bias = self._n_bias(n_facets)

        # Apply correlation biases: high N -> lower E, A, C
        e_facets = self._generate_extraversion(bias=n_bias)
        a_facets = self._generate_agreeableness(bias=n_bias)
        c_facets = self._generate_conscientiousness(bias=n_bias)

        # Open-mindedness has weak positive correlation with E
        e_avg = (e_facets.sociability + e_facets.assertiveness + e_facets.energy_level) / 3
        o_bias = 1 if e_avg >= 4 else 0
        o_facets = self._generate_open_mindedness(bias=o_bias)

        return PersonalityResult(
            extraversion=ExtraversionResult(
                score=_domain_score(e_facets.sociability, e_facets.assertiveness, e_facets.energy_level),
                facets=e_facets,
            ),
            agreeableness=AgreeablenessResult(
                score=_domain_score(a_facets.compassion, a_facets.respectfulness, a_facets.trust),
                facets=a_facets,
            ),
            conscientiousness=ConscientiousnessResult(
                score=_domain_score(c_facets.organization, c_facets.productiveness, c_facets.responsibility),
                facets=c_facets,
            ),
            negative_emotionality=NegativeEmotionalityResult(
                score=_domain_score(n_facets.anxiety, n_facets.depression, n_facets.emotional_volatility),
                facets=n_facets,
            ),
            open_mindedness=OpenMindednessResult(
                score=_domain_score(o_facets.intellectual_curiosity, o_facets.aesthetic_sensitivity, o_facets.creative_imagination),
                facets=o_facets,
            ),
            seed=self._seed,
        )
