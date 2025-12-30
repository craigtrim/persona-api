from enum import Enum

from pydantic import BaseModel, Field


class PromptUse(str, Enum):
    system_prompt = "system_prompt"
    input_prompt = "input_prompt"
    profile = "profile"


class FacetScores(BaseModel):
    aesthetic_sensitivity: int = Field(ge=1, le=5)
    creative_imagination: int = Field(ge=1, le=5)
    intellectual_curiosity: int = Field(ge=1, le=5)


class OpennessFacets(FacetScores):
    pass


class ConscientiousnessFacets(BaseModel):
    organization: int = Field(ge=1, le=5)
    productiveness: int = Field(ge=1, le=5)
    responsibility: int = Field(ge=1, le=5)


class ExtraversionFacets(BaseModel):
    assertiveness: int = Field(ge=1, le=5)
    energy_level: int = Field(ge=1, le=5)
    sociability: int = Field(ge=1, le=5)


class AgreeablenessFacets(BaseModel):
    compassion: int = Field(ge=1, le=5)
    respectfulness: int = Field(ge=1, le=5)
    trust: int = Field(ge=1, le=5)


class NeuroticismFacets(BaseModel):
    anxiety: int = Field(ge=1, le=5)
    depression: int = Field(ge=1, le=5)
    emotional_volatility: int = Field(ge=1, le=5)


class DomainScore(BaseModel):
    score: int = Field(ge=1, le=5)


class OpennessScore(DomainScore):
    facets: OpennessFacets


class ConscientiousnessScore(DomainScore):
    facets: ConscientiousnessFacets


class ExtraversionScore(DomainScore):
    facets: ExtraversionFacets


class AgreeablenessScore(DomainScore):
    facets: AgreeablenessFacets


class NeuroticismScore(DomainScore):
    facets: NeuroticismFacets


class PersonalityScores(BaseModel):
    openness: OpennessScore
    conscientiousness: ConscientiousnessScore
    extraversion: ExtraversionScore
    agreeableness: AgreeablenessScore
    neuroticism: NeuroticismScore


class PersonalityResponse(BaseModel):
    scores: PersonalityScores
    prompt: str
    seed: str
