from snake.src.config import GRID_WIDTH, GRID_HEIGHT, COLOR_SNAKE_BODY, COLOR_SNAKE_HEAD, COLOR_FOOD, CHAR_SNAKE_BODY, CHAR_SNAKE_HEAD, CHAR_FOOD
import sys

class Renderer:
    def render(self, snake, food, grid_width, grid_height):
        # Clear screen and move cursor to home
        print("\033[2J\033[H", end='')
        for y in range(grid_height):
            for x in range(grid_width):
                if (x, y) == snake.get_head():
                    print(f"{COLOR_SNAKE_HEAD}{CHAR_SNAKE_HEAD}\033[0m", end='')
                elif (x, y) in snake.get_body():
                    print(f"{COLOR_SNAKE_BODY}{CHAR_SNAKE_BODY}\033[0m", end='')
                elif (x, y) == food.get_position():
                    print(f"{COLOR_FOOD}{CHAR_FOOD}\033[0m", end='')
                else:
                    print(' ', end='')
            print()  # newline after each row
        sys.stdout.flush()
