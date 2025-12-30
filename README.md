# Persona API

[![Python versions](https://img.shields.io/pypi/pyversions/persona-api.svg)](https://pypi.org/project/persona-api/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

FastAPI service for generating Big Five personality profiles for LLM agents and chatbots.

## Why This Library?

Generate coherent, psychometrically-grounded personality configurations for your AI agents. Based on the **BFI-2** (Big Five Inventory-2) taxonomy with 5 domains and 15 facets.

## Features

- **Big Five scoring**: OCEAN traits with 3 facets each (1-5 scale)
- **Prompt generation**: Output prompts tailored for system prompts, input prompts, or profiles
- **Model targeting**: Specify target LLM (claude, gpt4, etc.)
- **Reproducible**: Seed-based generation for consistent results

## Installation

```bash
pip install persona-api
```

## Quick Start

```bash
make run
```

```bash
curl http://localhost:8000/personality/random
```

```json
{
  "scores": {
    "openness": { "score": 4, "facets": { "aesthetic_sensitivity": 5, "creative_imagination": 4, "intellectual_curiosity": 3 } },
    "conscientiousness": { "score": 2, "facets": { "organization": 2, "productiveness": 3, "responsibility": 1 } },
    "extraversion": { "score": 5, "facets": { "assertiveness": 5, "energy_level": 4, "sociability": 5 } },
    "agreeableness": { "score": 3, "facets": { "compassion": 4, "respectfulness": 3, "trust": 2 } },
    "neuroticism": { "score": 1, "facets": { "anxiety": 1, "depression": 1, "emotional_volatility": 2 } }
  },
  "prompt": "You are a highly creative and outgoing assistant...",
  "seed": "abc123"
}
```

## API Reference

### `GET /personality/random`

Generate a random personality profile.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model` | string | null | Target LLM model (e.g., `claude_opus`, `gpt4`) |
| `use` | enum | `system_prompt` | Output format: `system_prompt`, `input_prompt`, `profile` |

### `GET /health`

Health check endpoint.

## Big Five Taxonomy (BFI-2)

See [docs/bfi2-form.pdf](docs/bfi2-form.pdf) for the original 60-item questionnaire.

| Domain | Facets |
|--------|--------|
| Openness | aesthetic_sensitivity, creative_imagination, intellectual_curiosity |
| Conscientiousness | organization, productiveness, responsibility |
| Extraversion | assertiveness, energy_level, sociability |
| Agreeableness | compassion, respectfulness, trust |
| Neuroticism | anxiety, depression, emotional_volatility |

## Requirements

- Python 3.11+
- FastAPI
- Pydantic 2.0+

## License

MIT License
