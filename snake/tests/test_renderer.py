import sys
import os
import unittest
import io
from unittest.mock import patch

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from renderer import Renderer
from snake import Snake
from food import Food
from config import COLOR_SNAKE_BODY, COLOR_SNAKE_HEAD, COLOR_FOOD, CHAR_SNAKE_BODY, CHAR_SNAKE_HEAD, CHAR_FOOD, DIRECTION_RIGHT

class TestRenderer(unittest.TestCase):
    def test_render_instantiation(self):
        renderer = Renderer()
        self.assertIsNotNone(renderer)

    def test_render_output(self):
        snake = Snake(body=[(0,0), (1,0)], direction=DIRECTION_RIGHT)
        food = Food(position=(1,1))
        renderer = Renderer()
        grid_width, grid_height = 2, 2
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            renderer.render(snake, food, grid_width, grid_height)
            output = mock_stdout.getvalue()
            mock_stdout.flush.assert_called_once()
        expected = "\033[2J\033[H"
        # Row 0
        expected += COLOR_SNAKE_HEAD + CHAR_SNAKE_HEAD + "\033[0m"
        expected += COLOR_SNAKE_BODY + CHAR_SNAKE_BODY + "\033[0m"
        expected += '\n'
        # Row 1
        expected += ' '
        expected += COLOR_FOOD + CHAR_FOOD + "\033[0m"
        expected += '\n'
        self.assertEqual(output, expected)

    def test_render_output_single_segment(self):
        snake = Snake(body=[(0,0)], direction=DIRECTION_RIGHT)
        food = Food(position=(1,1))
        renderer = Renderer()
        grid_width, grid_height = 2, 2
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            renderer.render(snake, food, grid_width, grid_height)
            output = mock_stdout.getvalue()
        expected = "\033[2J\033[H"
        # Row 0
        expected += COLOR_SNAKE_HEAD + CHAR_SNAKE_HEAD + "\033[0m"
        expected += ' '
        expected += '\n'
        # Row 1
        expected += ' '
        expected += COLOR_FOOD + CHAR_FOOD + "\033[0m"
        expected += '\n'
        self.assertEqual(output, expected)

    def test_render_output_food_on_head(self):
        snake = Snake(body=[(0,0)], direction=DIRECTION_RIGHT)
        food = Food(position=(0,0))
        renderer = Renderer()
        grid_width, grid_height = 2, 2
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            renderer.render(snake, food, grid_width, grid_height)
            output = mock_stdout.getvalue()
        expected = "\033[2J\033[H"
        # Row 0
        expected += COLOR_SNAKE_HEAD + CHAR_SNAKE_HEAD + "\033[0m"
        expected += ' '
        expected += '\n'
        # Row 1: both empty
        expected += '  \n'
        self.assertEqual(output, expected)

    def test_render_output_food_on_body(self):
        snake = Snake(body=[(0,0), (1,0)], direction=DIRECTION_RIGHT)
        food = Food(position=(1,0))
        renderer = Renderer()
        grid_width, grid_height = 2, 2
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            renderer.render(snake, food, grid_width, grid_height)
            output = mock_stdout.getvalue()
        expected = "\033[2J\033[H"
        # Row 0
        expected += COLOR_SNAKE_HEAD + CHAR_SNAKE_HEAD + "\033[0m"
        expected += COLOR_SNAKE_BODY + CHAR_SNAKE_BODY + "\033[0m"
        expected += '\n'
        # Row 1: both empty
        expected += '  \n'
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()
