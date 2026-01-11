class Timeline:
    """Tracks day/night and boss cadence."""

    def __init__(self, ticks_per_day: int = 6):
        self.ticks_per_day = ticks_per_day
        self.tick = 0

    def advance(self, steps: int = 1) -> None:
        self.tick += steps

    @property
    def day(self) -> int:
        return self.tick // self.ticks_per_day

    @property
    def is_night(self) -> bool:
        return (self.tick % self.ticks_per_day) >= (self.ticks_per_day // 2)
