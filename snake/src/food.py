from . import config
import random

class Food:
    def __init__(self, position=None):
        if position is None:
            self.position = self.spawn([])
        else:
            self.position = position

    def spawn(self, occupied_positions):
        while True:
            x = random.randint(0, config.GRID_WIDTH - 1)
            y = random.randint(0, config.GRID_HEIGHT - 1)
            if (x, y) not in occupied_positions:
                self.position = (x, y)
                break
        return self.position

    def get_position(self):
        return self.position
