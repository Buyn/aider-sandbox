import time
import snake
import food
import renderer
import input_handler
import config


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

    def run(self):
        try:
            while True:
                key = self.input_handler.get_key()
                if key is not None:
                    if key == ' ':
                        self.paused = not self.paused
                    elif key == 'r':
                        self.restart()
                    elif key in self.config.KEY_MAPPING:
                        new_direction = self.config.KEY_MAPPING[key]
                        # Prevent reversing direction
                        current_direction = self.snake.direction
                        opposite_direction = (-current_direction[0], -current_direction[1])
                        if new_direction != opposite_direction:
                            self.snake.set_direction(new_direction)

                if not self.paused and not self.game_over:
                    # Save current tail for potential growth                    old_tail = self.snake.get_body()[-1]
                    # Move snake without growing
                    self.snake.move(grow=False)
                    # Check if snake ate food
                    if self.snake.get_head() == self.food.get_position():
                        # Grow by adding the old tail back
                        self.snake.body.append(old_tail)
                        # Spawn new food
                        self.food.spawn(self.snake.get_body())
                    # Check for self collision                    if self.snake.get_head() in self.snake.get_body()[1:]:
                        self.game_over = True

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
