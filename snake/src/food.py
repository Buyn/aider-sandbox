import random
from snake.src.config import GRID_WIDTH, GRID_HEIGHT

class Food:
    def __init__(self, position=None):
        self.position = position

    def spawn(self, occupied_positions):
        all_positions = {(x, y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)}
        occupied_set = set(occupied_positions)
        free_positions = all_positions - occupied_set
        if not free_positions:
            raise ValueError("No free positions available for food spawn")
        self.position = random.choice(list(free_positions))

    def get_position(self):
        return self.position
