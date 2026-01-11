import random

class RNG:
    """Seeded RNG wrapper for deterministic runs."""

    def __init__(self, seed: int):
        self._random = random.Random(seed)

    def reseed(self, seed: int) -> None:
        self._random.seed(seed)

    def randint(self, low: int, high: int) -> int:
        return self._random.randint(low, high)

    def choice(self, items):
        return self._random.choice(items)

    def random(self) -> float:
        return self._random.random()
