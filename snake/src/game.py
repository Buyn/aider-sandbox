import time
from snake.src import snake, food, renderer, input_handler, config

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
                if key == config.ACTION_PAUSE:
                    self.paused = not self.paused
                elif key == config.ACTION_RESTART and self.game_over:
                    self.restart()
                elif not self.paused and not self.game_over:
                    if key in (config.DIRECTION_UP, config.DIRECTION_DOWN, config.DIRECTION_LEFT, config.DIRECTION_RIGHT):
                        new_direction = key
                        # Prevent reversing direction
                        if (self.direction[0] * -1, self.direction[1] * -1) != new_direction:
                            self.snake.set_direction(new_direction)
                            self.direction = new_direction

                    # Determine if the snake will eat food this move
                    head = self.snake.get_head()
                    dx, dy = self.snake.direction
                    new_head = ((head[0] + dx) % self.config.GRID_WIDTH, (head[1] + dy) % self.config.GRID_HEIGHT)
                    grew = (new_head == self.food.get_position())

                    if not self.snake.move(grow=grew):
                        self.game_over = True
                    elif grew:
                        self.food.spawn(self.snake.get_body())

                self.renderer.render(self.snake, self.food, self.config.GRID_WIDTH, self.config.GRID_HEIGHT)
                time.sleep(1 / self.config.TICKS_PER_SECOND)
        finally:
            self.input_handler.cleanup()

    def restart(self):
        self.snake = snake.Snake()
        self.food = food.Food()
        self.food.spawn(self.snake.get_body())
        self.paused = False
        self.game_over = False
        self.direction = self.snake.direction
