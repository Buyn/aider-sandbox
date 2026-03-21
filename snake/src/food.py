from . import config
import random

class Food:
    def __init__(self, position=None):
        self.position = position

    def spawn(self, occupied_positions):
        all_positions = {(x, y) for x in range(config.GRID_WIDTH) for y in range(config.GRID_HEIGHT)}
        occupied_set = set(occupied_positions)
        free_positions = all_positions - occupied_set
        if not free_positions:
            raise ValueError("No free positions available for food spawn")
        self.position = random.choice(list(free_positions))

    def get_position(self):
        return self.position
