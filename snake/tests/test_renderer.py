import unittest
from io import StringIO
import sys
from src import config
from src.renderer import Renderer
from src.snake import Snake
from src.food import Food

class TestRenderer(unittest.TestCase):
    def setUp(self):
        # Save original config values
        self.original_walls_enabled = config.WALLS_ENABLED
        self.original_wall_symbol = config.WALL_SYMBOL
        self.original_wall_color = config.WALL_COLOR
        
        # Redirect stdout to capture output
        self.held_output = sys.stdout
        sys.stdout = StringIO()
    
    def tearDown(self):
        # Restore config
        config.WALLS_ENABLED = self.original_walls_enabled
        config.WALL_SYMBOL = self.original_wall_symbol
        config.WALL_COLOR = self.original_wall_color
        # Restore stdout
        sys.stdout = self.held_output
    
    def test_render_with_walls_enabled(self):
        config.WALLS_ENABLED = True
        config.WALL_SYMBOL = '#'
        config.WALL_COLOR = '\033[93m'
        
        # Create a simple snake and food
        snake = Snake(body=[(1,1), (0,1), (0,0)], direction=config.DIRECTION_RIGHT)
        food = Food(position=(2,1))
        renderer = Renderer()
        renderer.render(snake, food, 3, 2)
        
        output = sys.stdout.getvalue()
        lines = output.split('\n')
        # Expect at least: escape+top, row0, row1, bottom, trailing empty
        self.assertGreaterEqual(len(lines), 5)
        
        # Top border line (lines[0] contains escape sequence + top border)
        expected_top = config.WALL_COLOR + config.WALL_SYMBOL * (3 + 2) + '\033[0m'
        self.assertTrue(lines[0].endswith(expected_top), f"Top border not found. Output: {repr(lines[0])}")
        
        # Check row lines (lines[1] and lines[2])
        for i in range(1, 3):
            row_line = lines[i]
            self.assertTrue(row_line.startswith(config.WALL_COLOR + config.WALL_SYMBOL + '\033[0m'),
                            f"Row {i} missing left wall")
            self.assertTrue(row_line.endswith(config.WALL_COLOR + config.WALL_SYMBOL + '\033[0m'),
                            f"Row {i} missing right wall")
        
        # Bottom border line (lines[3])
        bottom_line = lines[3]
        self.assertEqual(bottom_line, expected_top, "Bottom border mismatch")
    
    def test_render_with_walls_disabled(self):
        config.WALLS_ENABLED = False
        snake = Snake(body=[(1,1), (0,1)], direction=config.DIRECTION_RIGHT)
        food = Food(position=(2,1))
        renderer = Renderer()
        renderer.render(snake, food, 3, 2)
        
        output = sys.stdout.getvalue()
        lines = output.split('\n')
        # Without walls: escape, row0, row1, maybe empty
        self.assertGreaterEqual(len(lines), 3)
        
        # Row lines should not contain wall symbol
        row0 = lines[1]
        row1 = lines[2]
        self.assertNotIn(config.WALL_SYMBOL, row0)
        self.assertNotIn(config.WALL_SYMBOL, row1)
        # Also should not start with wall color
        self.assertFalse(row0.startswith(config.WALL_COLOR))
        self.assertFalse(row1.startswith(config.WALL_COLOR))
    
    def test_wall_color_and_symbol_used(self):
        config.WALLS_ENABLED = True
        config.WALL_SYMBOL = '='
        config.WALL_COLOR = '\033[94m'  # blue
        snake = Snake(body=[(0,0)], direction=config.DIRECTION_RIGHT)
        food = Food(position=(1,0))
        renderer = Renderer()
        renderer.render(snake, food, 2, 1)
        
        output = sys.stdout.getvalue()
        lines = output.split('\n')
        expected_top = config.WALL_COLOR + '====' + '\033[0m'  # grid_width+2 = 4
        self.assertTrue(lines[0].endswith(expected_top))
        row_line = lines[1]
        self.assertTrue(row_line.startswith(config.WALL_COLOR + '=' + '\033[0m'))
        self.assertTrue(row_line.endswith(config.WALL_COLOR + '=' + '\033[0m'))
    
    def test_render_with_default_wall_config(self):
        # This test verifies that the default configuration values are correct and used.
        self.assertTrue(config.WALLS_ENABLED)
        self.assertEqual(config.WALL_SYMBOL, '#')
        self.assertEqual(config.WALL_COLOR, '\033[93m')
        snake = Snake(body=[(0,0)], direction=config.DIRECTION_RIGHT)
        food = Food(position=(1,0))
        renderer = Renderer()
        renderer.render(snake, food, 2, 1)
        output = sys.stdout.getvalue()
        lines = output.split('\n')
        expected_top = config.WALL_COLOR + config.WALL_SYMBOL * (2+2) + '\033[0m'
        self.assertTrue(lines[0].endswith(expected_top))

if __name__ == '__main__':
    unittest.main()
