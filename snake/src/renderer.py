from . import config

class Renderer:
    def render(self, snake, food, grid_width, grid_height):
        # Clear screen and move cursor to home
        print("\033[2J\033[H", end='')
        
        # If walls are enabled, draw top border
        if config.WALLS_ENABLED:
            top_bottom = config.WALL_COLOR + config.WALL_SYMBOL * (grid_width + 2) + '\033[0m'
            print(top_bottom)
        
        for y in range(grid_height):
            row_parts = []
            # Left wall
            if config.WALLS_ENABLED:
                row_parts.append(config.WALL_COLOR + config.WALL_SYMBOL + '\033[0m')
            
            # Grid cells
            for x in range(grid_width):
                if (x, y) == snake.get_head():
                    row_parts.append(config.COLOR_SNAKE_HEAD + config.CHAR_SNAKE_HEAD + '\033[0m')
                elif (x, y) in snake.get_body():
                    row_parts.append(config.COLOR_SNAKE_BODY + config.CHAR_SNAKE_BODY + '\033[0m')
                elif (x, y) == food.get_position():
                    row_parts.append(config.COLOR_FOOD + config.CHAR_FOOD + '\033[0m')
                else:
                    row_parts.append(' ')
            
            # Right wall
            if config.WALLS_ENABLED:
                row_parts.append(config.WALL_COLOR + config.WALL_SYMBOL + '\033[0m')
            
            print(''.join(row_parts))
        
        # If walls are enabled, draw bottom border
        if config.WALLS_ENABLED:
            print(top_bottom)
