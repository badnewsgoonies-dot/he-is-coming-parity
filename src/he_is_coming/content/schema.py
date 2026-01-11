from dataclasses import dataclass
from typing import List

@dataclass
class ItemDef:
    id: str
    name: str
    rarity: str
    tags: List[str]
    triggers: List[dict]

@dataclass
class EnemyDef:
    id: str
    name: str
    level: int
    stats: dict
    traits: List[str]
