from dataclasses import dataclass, field
from enum import Enum


class Status(Enum):
    WOUNDED = "wounded"
    EXPOSED = "exposed"
    FREEZE = "freeze"
    THORNS = "thorns"
    POISON = "poison"
    ACID = "acid"
    STUN = "stun"
    RIPTIDE = "riptide"


@dataclass
class StatusState:
    counts: dict[Status, int] = field(default_factory=dict)

    def add(self, status: Status, stacks: int = 1) -> None:
        self.counts[status] = max(0, self.counts.get(status, 0) + stacks)

    def remove(self, status: Status, stacks: int = 1) -> None:
        if status not in self.counts:
            return
        remaining = self.counts[status] - stacks
        if remaining > 0:
            self.counts[status] = remaining
        else:
            self.counts.pop(status, None)

    def get(self, status: Status) -> int:
        return self.counts.get(status, 0)

    def has(self, status: Status) -> bool:
        return self.get(status) > 0
