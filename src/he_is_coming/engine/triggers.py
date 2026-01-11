from dataclasses import dataclass
from enum import Enum
from typing import Optional

from he_is_coming.engine.status import Status


class Trigger(Enum):
    BATTLE_START = "battle_start"
    ON_HIT = "on_hit"
    END_TURN = "end_turn"
    WOUNDED = "wounded"
    EXPOSED = "exposed"


@dataclass
class Effect:
    kind: str
    amount: int | None = None
    status: Optional[Status] = None
    target: str = "self"


@dataclass
class TriggerEffect:
    trigger: Trigger
    effect: Effect


@dataclass
class TriggerEvent:
    trigger: Trigger
    actor_id: str
    target_id: Optional[str]
    source: str
