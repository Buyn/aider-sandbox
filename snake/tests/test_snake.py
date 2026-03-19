import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from snake import Snake
from config import GRID_WIDTH, GRID_HEIGHT, DIRECTION_RIGHT, DIRECTION_LEFT, DIRECTION_UP, DIRECTION_DOWN

class TestSnake(unittest.TestCase):
    def test_initialization(self):
        snake = Snake()
        self.assertEqual(snake.get_length(), 3)
        center_x = GRID_WIDTH // 2
        center_y = GRID_HEIGHT // 2
        self.assertEqual(snake.get_head(), (center_x, center_y))
        self.assertEqual(snake.get_body(), [(center_x, center_y), (center_x-1, center_y), (center_x-2, center_y)])
        self.assertEqual(snake.direction, DIRECTION_RIGHT)

    def test_move_without_growth(self):
        snake = Snake(body=[(5,5), (4,5), (3,5)], direction=DIRECTION_RIGHT)
        result = snake.move(grow=False)
        self.assertTrue(result)
        self.assertEqual(snake.get_head(), (6,5))
        self.assertEqual(snake.get_body(), [(6,5), (5,5), (4,5)])
        self.assertEqual(snake.get_length(), 3)

    def test_move_with_growth(self):
        snake = Snake(body=[(5,5), (4,5), (3,5)], direction=DIRECTION_RIGHT)
        result = snake.move(grow=True)
        self.assertTrue(result)
        self.assertEqual(snake.get_head(), (6,5))
        self.assertEqual(snake.get_body(), [(6,5), (5,5), (4,5), (3,5)])
        self.assertEqual(snake.get_length(), 4)

    def test_wrap_around(self):
        snake = Snake(body=[(0,5), (1,5), (2,5)], direction=DIRECTION_LEFT)
        result = snake.move(grow=False)
        self.assertTrue(result)
        self.assertEqual(snake.get_head(), (GRID_WIDTH-1, 5))
        self.assertEqual(snake.get_body(), [(GRID_WIDTH-1,5), (0,5), (1,5)])

    def test_self_collision(self):
        snake = Snake(body=[(5,5), (6,5), (7,5)], direction=DIRECTION_RIGHT)
        result = snake.move(grow=False)
        self.assertFalse(result)
        self.assertEqual(snake.get_body(), [(5,5), (6,5), (7,5)])

if __name__ == '__main__':
    unittest.main()
