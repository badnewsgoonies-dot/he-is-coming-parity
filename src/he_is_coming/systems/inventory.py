from dataclasses import dataclass
from typing import Iterable, Optional

from he_is_coming.engine.triggers import Trigger, TriggerEffect


@dataclass
class Item:
    item_id: str
    name: str
    effects: list[TriggerEffect]


class Inventory:
    """Slot-ordered inventory used by trigger resolution."""

    def __init__(self, slots: int):
        self.slots: list[Optional[Item]] = [None] * slots

    def set_slot(self, index: int, item: Optional[Item]) -> None:
        self.slots[index] = item

    def iter_items(self) -> Iterable[Item]:
        for item in self.slots:
            if item is not None:
                yield item

    def iter_trigger_effects(self, trigger: Trigger) -> Iterable[TriggerEffect]:
        for item in self.iter_items():
            for effect in item.effects:
                if effect.trigger == trigger:
                    yield effect
