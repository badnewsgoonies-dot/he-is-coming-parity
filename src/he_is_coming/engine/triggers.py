from dataclasses import dataclass
from enum import Enum

class Trigger(Enum):
    BATTLE_START = "battle_start"
    ON_HIT = "on_hit"
    END_TURN = "end_turn"
    WOUNDED = "wounded"
    EXPOSED = "exposed"

@dataclass
class TriggerContext:
    actor_id: str
    target_id: str | None
    trigger: Trigger
