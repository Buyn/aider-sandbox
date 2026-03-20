from. import snake, food, renderer, input_handler, config
import time


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
                if key == 'r':
                    self.restart()
                    continue
                if key == ' ':
                    self.paused = not self.paused
                    continue
                if key in self.config.KEY_MAPPING and not self.paused:
                    new_direction = self.config.KEY_MAPPING[key]
                    self.snake.set_direction(new_direction)
                    self.direction = new_direction

                if not self.paused and not self.game_over:
                    old_tail = self.snake.get_body()[-1]
                    if not self.snake.move(grow=False):
                        self.game_over = True
                    else:
                        if self.snake.get_head() == self.food.get_position():
                            self.snake.body.append(old_tail)
                            self.food.spawn(self.snake.get_body())

                self.renderer.render(
                    self.snake,
                    self.food,
                    self.config.GRID_WIDTH,
                    self.config.GRID_HEIGHT
                )
                time.sleep(1.0 / self.config.TICKS_PER_SECOND)
        except KeyboardInterrupt:
            pass
        finally:
            self.input_handler.cleanup()

    def restart(self):
        self.snake = snake.Snake()
        self.food = food.Food()
        self.food.spawn(self.snake.get_body())
        self.paused = False
        self.game_over = False
        self.direction = self.snake.direction
