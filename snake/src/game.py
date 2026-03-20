import time
from . import config
from . import snake
from . import food
from . import renderer
from . import input_handler

class Game:
    def __init__(self):
        self.config = config
        self.snake = snake.Snake()
        self.food = food.Food()
        self.food.spawn(self.snake.get_body())
        self.renderer = renderer.Renderer()
        self.input_handler = input_handler.InputHandler()
        self.paused = False
        self.game_over = False
        self.direction = self.snake.direction

    def run(self):
        try:
            while True:
                key = self.input_handler.get_key()
                if key == 'pause':
                    self.paused = not self.paused
                elif key == 'restart':
                    self.restart()
                elif key in self.config.KEY_MAP:
                    new_direction = self.config.KEY_MAP[key]
                    # Prevent reversing direction
                    if new_direction != (-self.direction[0], -self.direction[1]):
                        self.direction = new_direction
                        self.snake.set_direction(self.direction)

                if not self.paused and not self.game_over:
                    # Calculate next head position with wrap-around                    current_head = self.snake.get_head()
                    dx, dy = self.direction
                    next_head = (
                        (current_head[0] + dx) % self.config.GRID_WIDTH,
                        (current_head[1] + dy) % self.config.GRID_HEIGHT
                    )
                    grow = (next_head == self.food.get_position())
                    self.snake.move(grow=grow)
                    if grow:
                        self.food.spawn(self.snake.get_body())
                    # Check for self-collision
                    if self.snake.get_head() in self.snake.get_body()[1:]:
                        self.game_over = True

                self.renderer.render(self.snake, self.food, self.config.GRID_WIDTH, self.config.GRID_HEIGHT)
                time.sleep(1.0 / self.config.TICKS_PER_SECOND)
        except KeyboardInterrupt:
            pass
        finally:
            self.input_handler.cleanup()

    def restart(self):
        self.snake = snake.Snake()
        self.food = food.Food()
        self.food.spawn(self.snake.get_body())
        self.direction = self.snake.direction        self.paused = False
        self.game_over = False
