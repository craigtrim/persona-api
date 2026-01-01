# Persona API

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.0+-E92063?logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A FastAPI service for generating psychometrically-grounded personality profiles for LLM agents and chatbots. Built on the **Big Five Inventory-2 (BFI-2)** taxonomy with formal ontological foundations.

<p align="center">
  <em>Part of the Persona suite. See also: <a href="../persona-ui">persona-ui</a></em>
</p>

## Purpose

This API exists to solve a real problem: **how do you systematically vary AI personality for testing and evaluation?**

Primary use cases include:

- **Adversarial Testing**: Generate personalities that stress-test AI safety boundaries (hostile, manipulative, anxious personas)
- **Red Team Scenarios**: Create diverse chatbot configurations for security evaluations
- **Behavioral Coverage**: Ensure test suites cover the full personality space, not just "helpful assistant"
- **Reproducible Experiments**: Seed-based generation for consistent, replicable personality profiles

While the output can be used for entertainment or creative applications, the core design prioritizes scientific rigor and adversarial utility.

## Scientific Foundation

### BFI-2 Framework

This system implements the **Big Five Inventory-2** (Soto & John, 2017), the modern successor to the widely-used NEO-PI-R. The BFI-2 defines:

- **5 Domains**: Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism (OCEAN)
- **15 Facets**: 3 facets per domain, each measured on a 1-5 scale
- **60 Survey Items**: The official BFI-2 questionnaire used as ground truth

See [`docs/bfi2-form.pdf`](docs/bfi2-form.pdf) for the original 60-item questionnaire that serves as the basis for all behavioral mappings.

### Ontological Model

The personality model is formally specified in [`big5.owl`](big5.owl), an OWL 2 ontology that encodes:

```
Domain → Facet → Survey Item → Behavioral Instruction
```

Key ontological features:
- **Survey Rating Properties**: `surveyRating1` through `surveyRating5` map scale positions to behavioral descriptors
- **Emotion Triggers**: `triggers` / `triggeredBy` relationships connect traits to emotional responses
- **Trait-Behavior Associations**: `associatedWith` links observable behaviors to underlying traits

This formal structure ensures behavioral instructions derive from validated psychometric items rather than ad-hoc descriptions.

### Domain Correlations

Real personalities exhibit systematic correlations (e.g., high Neuroticism correlates with lower Extraversion). The [`docs/big5-correlations.md`](docs/big5-correlations.md) reference documents these patterns, which are implemented in the `RandomFacetGenerator` to produce realistic profiles:

| Correlation | Direction | Implementation |
|-------------|-----------|----------------|
| Neuroticism ↔ Conscientiousness | Strong negative | High N biases C downward |
| Neuroticism ↔ Extraversion | Strong negative | High N biases E downward |
| Neuroticism ↔ Agreeableness | Strong negative | High N biases A downward |
| Extraversion ↔ Openness | Moderate positive | High E biases O upward |

### Pre-Computed Training Data

The system prompts consumed by [persona-ui](../persona-ui) were generated through a large-scale computation process:

- **3,125 Domain Combinations**: All permutations of (A, C, E, O, N) scores from 1-5
- **500 Samples per Combination**: 100 runs × 5 length tiers (64, 128, 256, 512, unconstrained)
- **~1.56 Million Total Samples**: Generated using Qwen 2.5 (7B) on NVIDIA GPU infrastructure
- **Behavioral Instruction Slicing**: Each sample derives from round-robin selection across domain behaviors

This approach ensures coverage of the full personality space while maintaining linguistic diversity through stochastic generation.

> **Note**: Translating psychometric constructs into natural language inevitably involves interpretation. We've prioritized empirical grounding, but acknowledge that any verbalization of personality traits carries assumptions about how those traits manifest behaviorally.

## API Reference

### `GET /personality/random`

Generate a random personality profile with system prompt.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model` | string | null | Target LLM model (e.g., `claude_opus`, `gpt4`) |
| `use` | enum | `system_prompt` | Output format: `system_prompt`, `input_prompt`, `profile` |

**Response:**
```json
{
  "scores": {
    "openness": {
      "score": 4,
      "facets": {
        "aesthetic_sensitivity": 5,
        "creative_imagination": 4,
        "intellectual_curiosity": 3
      }
    },
    "conscientiousness": { "score": 2, "facets": { "...": "..." } },
    "extraversion": { "score": 5, "facets": { "...": "..." } },
    "agreeableness": { "score": 3, "facets": { "...": "..." } },
    "neuroticism": { "score": 1, "facets": { "...": "..." } }
  },
  "prompt": "You MUST adopt a highly creative and outgoing demeanor...",
  "seed": "abc123"
}
```

### `GET /health`

Health check endpoint.

## BFI-2 Taxonomy

| Domain | Facets | Description |
|--------|--------|-------------|
| **Openness** | Aesthetic Sensitivity, Creative Imagination, Intellectual Curiosity | Openness to experience, ideas, and aesthetics |
| **Conscientiousness** | Organization, Productiveness, Responsibility | Self-discipline and goal-directed behavior |
| **Extraversion** | Assertiveness, Energy Level, Sociability | Social engagement and positive emotionality |
| **Agreeableness** | Compassion, Respectfulness, Trust | Interpersonal warmth and cooperation |
| **Neuroticism** | Anxiety, Depression, Emotional Volatility | Tendency toward negative affect |

## Architecture

```
persona_api/
├── main.py                          # FastAPI application entry
├── routers/
│   └── personality.py               # API endpoints
├── models/
│   └── personality.py               # Pydantic response models
├── services/
│   ├── random_facet_generator.py    # BFI-2 score generation with correlations
│   ├── profile_generator.py         # System prompt generation via LLM
│   ├── behavior_resolver.py         # Score → behavioral instructions
│   ├── domain_text_resolver.py      # Facet combinations → text
│   └── facet_text_resolver.py       # Survey items → trait descriptors
├── data/
│   ├── behavioral/                  # 15 facet behavior JSON files
│   │   └── {facet}.json            # Survey items with behavioral instructions
│   ├── facets/                      # BFI-2 survey item definitions
│   └── text/                        # Pre-generated personality descriptions
│       └── {domain}/{s1}/{s2}/{s3}.json
├── cli_*.py                         # Development CLI tools
docs/
├── bfi2-form.pdf                    # Official BFI-2 60-item questionnaire
└── big5-correlations.md             # Domain correlation reference
big5.owl                             # OWL 2 ontology (563KB)
scripts/
├── generate_training_data.py        # Large-scale sample generation
└── consolidate_training_data.py     # Export to persona-ui format
```

## Installation

```bash
pip install poetry
poetry install
```

## Quick Start

```bash
make run
```

```bash
curl http://localhost:8000/personality/random
```

## CLI Tools

```bash
# Generate random personality
poetry run random-facet

# Resolve facet scores to text
poetry run resolve-facet --domain extraversion --scores 5,4,3

# Generate full profile via LLM
poetry run generate-profile --seed abc123 --host sparx
```

## Development

```bash
# Run tests
poetry run pytest

# Lint
poetry run ruff check .

# Type check
poetry run mypy persona_api/
```

## Related Projects

- **[persona-ui](../persona-ui)**: Interactive web frontend for personality exploration

## References

- Soto, C. J., & John, O. P. (2017). The next Big Five Inventory (BFI-2): Developing and assessing a hierarchical model with 15 facets. *Journal of Personality and Social Psychology*, 113(1), 117-143.
- Costa, P. T., & McCrae, R. R. (1992). *NEO-PI-R Professional Manual*. Psychological Assessment Resources.
- DeYoung, C. G., Quilty, L. C., & Peterson, J. B. (2007). Between facets and domains: 10 aspects of the Big Five. *Journal of Personality and Social Psychology*, 93(5), 880-896.

## License

MIT License
