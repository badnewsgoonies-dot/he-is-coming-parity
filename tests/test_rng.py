from he_is_coming.engine.rng import RNG


def test_rng_determinism():
    rng_a = RNG(123)
    rng_b = RNG(123)
    assert [rng_a.randint(1, 100) for _ in range(5)] == [rng_b.randint(1, 100) for _ in range(5)]
