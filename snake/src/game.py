import time
import curses
from .snake import Snake
from .food import Food
from .renderer import Renderer
from .input_handler import InputHandler
from . import config

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.food.spawn(self.snake.get_body())
        self.renderer = Renderer()
        self.input_handler = InputHandler()
        self.paused = False
        self.game_over = False
        self.direction = self.snake.direction

    def run(self):
        try:
            while True:
                start_time = time.time()
                key = self.input_handler.get_key()
                if key is not None:
                    self._handle_key(key)
                if not self.paused and not self.game_over:
                    self._update_game()
                self._render()
                elapsed = time.time() - start_time
                sleep_time = max(0, (1.0 / config.TICKS_PER_SECOND) - elapsed)
                time.sleep(sleep_time)
        finally:
            self.input_handler.cleanup()

    def _handle_key(self, key):
        if key == ord(' '):
            self.paused = not self.paused
        elif key == ord('r'):
            if self.game_over:
                self.restart()
        else:
            if not self.paused and not self.game_over:
                direction = self._key_to_direction(key)
                if direction:
                    self.snake.set_direction(direction)
                    self.direction = self.snake.direction

    def _key_to_direction(self, key):
        return config.KEY_MAPPING.get(key)

    def _update_game(self):
        if self.paused or self.game_over:
            return
        head_x, head_y = self.snake.get_head()
        dx, dy = self.snake.direction
        next_head = (
            (head_x + dx) % config.GRID_WIDTH,
            (head_y + dy) % config.GRID_HEIGHT
        )

        if next_head == self.food.get_position():
            self.snake.move(grow=True)
            self.food.spawn(self.snake.get_body())
        else:
            self.snake.move(grow=False)

        # Check for self-collision (exclude head itself)
        if self.snake.get_head() in self.snake.get_body()[1:]:
            self.game_over = True

    def _render(self):
        self.renderer.render(
            self.snake,
            self.food,
            config.GRID_WIDTH,
            config.GRID_HEIGHT
        )

    def restart(self):
        self.snake = Snake()
        self.food = Food()
        self.food.spawn(self.snake.get_body())
        self.paused = False
        self.game_over = False
        self.direction = self.snake.direction
