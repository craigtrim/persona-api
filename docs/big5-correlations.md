# Big Five Trait Correlations

Reference for implementing coherent personality generation.

## Domain-Level Correlations

### Strong Positive
| Trait A | Trait B | Notes |
|---------|---------|-------|
| Extraversion | Openness | Socially engaged people tend toward novelty-seeking |
| Conscientiousness | Agreeableness | Both reflect self-regulation and social adaptation |

### Strong Negative
| Trait A | Trait B | Notes |
|---------|---------|-------|
| Neuroticism | Conscientiousness | Emotional instability undermines goal-directed behavior |
| Neuroticism | Extraversion | Anxiety inhibits social approach behaviors |
| Neuroticism | Agreeableness | Negative affect strains cooperative tendencies |

### Weak/Neutral
| Trait A | Trait B | Notes |
|---------|---------|-------|
| Openness | Conscientiousness | Creativity and structure are largely independent |
| Openness | Agreeableness | Intellectual curiosity unrelated to warmth |
| Extraversion | Conscientiousness | Sociability and discipline are orthogonal |

## Facet-Level Tensions

Within-domain facets that create narrative friction when divergent:

| Domain | Facet A | Facet B | Tension |
|--------|---------|---------|---------|
| Neuroticism | anxiety | emotional_volatility | High anxiety + low volatility = internalized worry without outbursts (rare but valid) |
| Extraversion | sociability | assertiveness | High assertive + low social = dominant loner archetype |
| Agreeableness | trust | compassion | High trust + low compassion = naive but cold (incoherent) |
| Conscientiousness | organization | productiveness | High organized + low productive = perfectionist paralysis |

## Cross-Domain Dissonance

Combinations that are psychometrically possible but narratively awkward:

| Pattern | Why It's Odd |
|---------|--------------|
| High Neuroticism + High Extraversion | Socially driven but emotionally volatile; exists but exhausting to portray |
| High Openness + Low Extraversion + Low Agreeableness | Creative misanthropic recluse; coherent but niche |
| High Conscientiousness + High Openness + High Neuroticism | Perfectionist creative anxious type; real but complex |
| Low everything | Flat affect, disengaged; technically valid, hard to make interesting |
| High everything | Manic polymath; unrealistic ceiling effects |

## Implementation Guidance

**For truly random generation:**
- Accept all combinations; some will be "unusual personalities"
- Consider flagging statistical outliers (e.g., 3+ strong negative correlations violated)

**For coherent generation:**
- Apply correlation weights: if Neuroticism > 3, bias Conscientiousness downward
- Keep facets within ±2 of their domain score to maintain internal consistency
- Avoid extremes (all 1s or all 5s) unless intentionally generating archetypes

## References

- Costa & McCrae (1992). NEO-PI-R Professional Manual.
- DeYoung et al. (2007). Between Facets and Domains: 10 Aspects of the Big Five.
