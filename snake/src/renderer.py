from . import config

class Renderer:
    def render(self, snake, food, grid_width, grid_height):
        # Clear screen and move cursor to home
        print("\033[2J\033[H", end='')
        for y in range(grid_height):
            for x in range(grid_width):
                if (x, y) == snake.get_head():
                    print(f"{config.COLOR_SNAKE_HEAD}{config.CHAR_SNAKE_HEAD}\033[0m", end='')
                elif (x, y) in snake.get_body():
                    print(f"{config.COLOR_SNAKE_BODY}{config.CHAR_SNAKE_BODY}\033[0m", end='')
                elif (x, y) == food.get_position():
                    print(f"{config.COLOR_FOOD}{config.CHAR_FOOD}\033[0m", end='')
                else:
                    print(' ', end='')
            print()  # New line after each row
