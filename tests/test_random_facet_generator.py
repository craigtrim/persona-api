from persona_api.services import RandomFacetGenerator


class TestRandomFacetGenerator:
    def test_generate_returns_result(self):
        gen = RandomFacetGenerator()
        result = gen.generate()

        assert result is not None
        assert result.seed is not None
        assert result.extraversion is not None
        assert result.agreeableness is not None
        assert result.conscientiousness is not None
        assert result.negative_emotionality is not None
        assert result.open_mindedness is not None

    def test_extraversion_has_correct_facets(self):
        gen = RandomFacetGenerator()
        result = gen.generate()

        assert 1 <= result.extraversion.score <= 5
        assert 1 <= result.extraversion.facets.sociability <= 5
        assert 1 <= result.extraversion.facets.assertiveness <= 5
        assert 1 <= result.extraversion.facets.energy_level <= 5

    def test_agreeableness_has_correct_facets(self):
        gen = RandomFacetGenerator()
        result = gen.generate()

        assert 1 <= result.agreeableness.score <= 5
        assert 1 <= result.agreeableness.facets.compassion <= 5
        assert 1 <= result.agreeableness.facets.respectfulness <= 5
        assert 1 <= result.agreeableness.facets.trust <= 5

    def test_conscientiousness_has_correct_facets(self):
        gen = RandomFacetGenerator()
        result = gen.generate()

        assert 1 <= result.conscientiousness.score <= 5
        assert 1 <= result.conscientiousness.facets.organization <= 5
        assert 1 <= result.conscientiousness.facets.productiveness <= 5
        assert 1 <= result.conscientiousness.facets.responsibility <= 5

    def test_negative_emotionality_has_correct_facets(self):
        gen = RandomFacetGenerator()
        result = gen.generate()

        assert 1 <= result.negative_emotionality.score <= 5
        assert 1 <= result.negative_emotionality.facets.anxiety <= 5
        assert 1 <= result.negative_emotionality.facets.depression <= 5
        assert 1 <= result.negative_emotionality.facets.emotional_volatility <= 5

    def test_open_mindedness_has_correct_facets(self):
        gen = RandomFacetGenerator()
        result = gen.generate()

        assert 1 <= result.open_mindedness.score <= 5
        assert 1 <= result.open_mindedness.facets.intellectual_curiosity <= 5
        assert 1 <= result.open_mindedness.facets.aesthetic_sensitivity <= 5
        assert 1 <= result.open_mindedness.facets.creative_imagination <= 5

    def test_seed_produces_reproducible_results(self):
        gen1 = RandomFacetGenerator(seed="test123")
        gen2 = RandomFacetGenerator(seed="test123")

        result1 = gen1.generate()
        result2 = gen2.generate()

        assert result1.extraversion.score == result2.extraversion.score
        assert result1.negative_emotionality.score == result2.negative_emotionality.score
        assert result1.seed == result2.seed

    def test_different_seeds_produce_different_results(self):
        gen1 = RandomFacetGenerator(seed="aaa")
        gen2 = RandomFacetGenerator(seed="bbb")

        result1 = gen1.generate()
        result2 = gen2.generate()

        scores1 = [
            result1.extraversion.score,
            result1.agreeableness.score,
            result1.conscientiousness.score,
            result1.negative_emotionality.score,
            result1.open_mindedness.score,
        ]
        scores2 = [
            result2.extraversion.score,
            result2.agreeableness.score,
            result2.conscientiousness.score,
            result2.negative_emotionality.score,
            result2.open_mindedness.score,
        ]
        assert scores1 != scores2
