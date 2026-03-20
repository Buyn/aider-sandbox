from .snake import Snake
from .food import Food
from .renderer import Renderer
from .input_handler import InputHandler
from .config import (
    GRID_WIDTH, GRID_HEIGHT, TICKS_PER_SECOND,
    DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT
)
import time
class Game:
    def __init__(self):
        self.snake = Snake(direction=DIRECTION_RIGHT)
        self.food = Food()
        self.food.spawn(self.snake.get_body())
        self.renderer = Renderer()
        self.input_handler = InputHandler()
        self.paused = False
        self.game_over = False
        self.direction_map = {
            'up': DIRECTION_UP,
            'down': DIRECTION_DOWN,
            'left': DIRECTION_LEFT,
            'right': DIRECTION_RIGHT
        }

    def run(self):
        try:
            while True:
                key = self.input_handler.get_key()
                if key == 'pause':
                    self.paused = not self.paused
                elif key == 'restart':
                    self.restart()
                elif key in self.direction_map:
                    new_direction = self.direction_map[key]
                    # Prevent reversing direction
                    if not (new_direction[0] == -self.snake.direction[0] and                            new_direction[1] == -self.snake.direction[1]):
                        self.snake.set_direction(new_direction)

                if not self.paused and not self.game_over:
                    # Calculate next head position with wrap-around
                    current_head = self.snake.get_head()
                    dx, dy = self.snake.direction
                    next_head = (
                        (current_head[0] + dx) % GRID_WIDTH,
                        (current_head[1] + dy) % GRID_HEIGHT
                    )
                    grow = (next_head == self.food.get_position())
                    self.snake.move(grow=grow)
                    if grow:
                        self.food.spawn(self.snake.get_body())
                    # Check for self-collision
                    if self.snake.get_head() in self.snake.get_body()[1:]:
                        self.game_over = True

                self.renderer.render(self.snake, self.food, GRID_WIDTH, GRID_HEIGHT)
                time.sleep(1.0 / TICKS_PER_SECOND)
        except KeyboardInterrupt:
            pass        finally:
            self.input_handler.cleanup()

    def restart(self):
        self.snake = Snake(direction=DIRECTION_RIGHT)
        self.food = Food()
        self.food.spawn(self.snake.get_body())
        self.paused = False
        self.game_over = False
