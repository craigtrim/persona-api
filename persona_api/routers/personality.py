from fastapi import APIRouter, Query

from persona_api.models import (
    AgreeablenessFacets,
    AgreeablenessScore,
    ConscientiousnessFacets,
    ConscientiousnessScore,
    ExtraversionFacets,
    ExtraversionScore,
    NeuroticismFacets,
    NeuroticismScore,
    OpennessFacets,
    OpennessScore,
    PersonalityResponse,
    PersonalityScores,
    PromptUse,
)

router = APIRouter(prefix="/personality", tags=["personality"])


@router.get("/random", response_model=PersonalityResponse)
def get_random_personality(
    model: str | None = Query(default=None, description="Target LLM model (e.g., claude_opus, gpt4)"),
    use: PromptUse = Query(default=PromptUse.system_prompt, description="Where the prompt will be used"),
) -> PersonalityResponse:
    """
    Generate a random personality profile with Big Five traits and facets.

    Returns quantitative scores and a generated prompt suitable for the specified use case.
    """
    # Stubbed response with hardcoded values
    return PersonalityResponse(
        scores=PersonalityScores(
            openness=OpennessScore(
                score=4,
                facets=OpennessFacets(
                    aesthetic_sensitivity=5,
                    creative_imagination=4,
                    intellectual_curiosity=3,
                ),
            ),
            conscientiousness=ConscientiousnessScore(
                score=2,
                facets=ConscientiousnessFacets(
                    organization=2,
                    productiveness=3,
                    responsibility=1,
                ),
            ),
            extraversion=ExtraversionScore(
                score=5,
                facets=ExtraversionFacets(
                    assertiveness=5,
                    energy_level=4,
                    sociability=5,
                ),
            ),
            agreeableness=AgreeablenessScore(
                score=3,
                facets=AgreeablenessFacets(
                    compassion=4,
                    respectfulness=3,
                    trust=2,
                ),
            ),
            neuroticism=NeuroticismScore(
                score=1,
                facets=NeuroticismFacets(
                    anxiety=1,
                    depression=1,
                    emotional_volatility=2,
                ),
            ),
        ),
        prompt=f"[STUB: {use.value} prompt for model={model}] You are a highly creative and outgoing assistant who thrives on social interaction. You approach tasks with flexibility rather than rigid structure, and maintain emotional stability under pressure.",
        seed="stub_seed_abc123",
    )
