class ParityScoreboard:
    """Tracks parity gaps and target scores."""

    def __init__(self):
        self.gaps = {}

    def record_gap(self, key: str, score: float) -> None:
        self.gaps[key] = score
