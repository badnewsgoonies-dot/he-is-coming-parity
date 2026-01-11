class Inventory:
    """Slot-ordered inventory used by trigger resolution."""

    def __init__(self, slots: int):
        self.slots = [None] * slots
