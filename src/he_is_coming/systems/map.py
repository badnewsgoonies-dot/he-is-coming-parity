from dataclasses import dataclass

@dataclass
class MapState:
    width: int
    height: int
    seed: int
    fog_radius: int = 3
