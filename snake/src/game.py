import time
from snake.src.snake import Snake
from snake.src.food import Food
from snake.src.renderer import Renderer
from snake.src.input_handler import InputHandler
import configclass Game:
    def __init__(self):
        self.config = config
        self.snake = Snake()
        self.food = Food()
        self.food.spawn(self.snake.get_body())
        self.renderer = Renderer()
        self.input_handler = InputHandler()
        self.paused = False
        self.game_over = False

    def run(self):
        try:
            while not self.game_over:
                start_time = time.time()
                key = self.input_handler.get_key()
                if key is not None:
                    self._handle_key(key)
                if not self.paused and not self.game_over:
                    self._update_game()
                self._render()
                elapsed = time.time() - start_time
                sleep_time = max(0, (1.0 / self.config.TICKS_PER_SECOND) - elapsed)
                time.sleep(sleep_time)
        finally:
            self.input_handler.cleanup()

    def _handle_key(self, key):
        if key == ord(' '):
            self.paused = not self.paused
        elif key == ord('r'):
            self.restart()
        else:
            direction = self._key_to_direction(key)
            if direction:
                self.snake.set_direction(direction)

    def _key_to_direction(self, key):
        # Arrow keys
        if key == curses.KEY_UP:
            return config.DIRECTION_UP        elif key == curses.KEY_DOWN:
            return config.DIRECTION_DOWN
        elif key == curses.KEY_LEFT:
            return config.DIRECTION_LEFT
        elif key == curses.KEY_RIGHT:
            return config.DIRECTION_RIGHT
        # Vim keys        elif key == ord('h'):
            return config.DIRECTION_LEFT
        elif key == ord('j'):
            return config.DIRECTION_DOWN
        elif key == ord('k'):
            return config.DIRECTION_UP
        elif key == ord('l'):
            return config.DIRECTION_RIGHT
        # ESDF keys
        elif key == ord('e'):
            return config.DIRECTION_UP
        elif key == ord('d'):
            return config.DIRECTION_RIGHT
        elif key == ord('s'):
            return config.DIRECTION_DOWN
        elif key == ord('f'):
            return config.DIRECTION.LEFT
        return None

    def _update_game(self):
        self.snake.move(grow=False)
        if self.snake.get_head() == self.food.get_position():
            self.snake.move(grow=True)
            self.food.spawn(self.snake.get_body())
        # Check for self-collision
        if self.snake.get_head() in self.snake.get_body()[1:]:
            self.game_over = True

    def _render(self):
        self.renderer.render(
            self.snake,
            self.food,
            self.config.GRID_WIDTH,
            self.config.GRID_HEIGHT
        )

    def restart(self):
        self.snake = Snake()
        self.food = Food()
        self.food.spawn(self.snake.get_body())
        self.paused = False
        self.game_over = False
