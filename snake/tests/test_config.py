import sys
import os
import unittest

# Add src directory to path to import config
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from config import (
    GRID_WIDTH, GRID_HEIGHT, TICKS_PER_SECOND,
    COLOR_SNAKE_BODY, COLOR_SNAKE_HEAD, COLOR_FOOD, COLOR_BACKGROUND,
    CHAR_SNAKE_BODY, CHAR_SNAKE_HEAD, CHAR_FOOD,
    DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT,
    KEY_MAPPING
)
import curses

class TestConfig(unittest.TestCase):
    def test_grid_dimensions(self):
        self.assertEqual(GRID_WIDTH, 50)
        self.assertEqual(GRID_HEIGHT, 50)

    def test_speed(self):
        self.assertEqual(TICKS_PER_SECOND, 2)

    def test_colors(self):
        self.assertEqual(COLOR_SNAKE_BODY, '\033[32m')
        self.assertEqual(COLOR_SNAKE_HEAD, '\033[92m')
        self.assertEqual(COLOR_FOOD, '\033[31m')
        self.assertEqual(COLOR_BACKGROUND, '\033[0m')

    def test_characters(self):
        self.assertEqual(CHAR_SNAKE_BODY, '█')
        self.assertEqual(CHAR_SNAKE_HEAD, 'O')
        self.assertEqual(CHAR_FOOD, '●')

    def test_direction_constants(self):
        self.assertEqual(DIRECTION_UP, (0, -1))
        self.assertEqual(DIRECTION_DOWN, (0, 1))
        self.assertEqual(DIRECTION_LEFT, (-1, 0))
        self.assertEqual(DIRECTION_RIGHT, (1, 0))

    def test_key_mapping(self):
        # Check arrow keys
        self.assertEqual(KEY_MAPPING[curses.KEY_UP], DIRECTION_UP)
        self.assertEqual(KEY_MAPPING[curses.KEY_DOWN], DIRECTION_DOWN)
        self.assertEqual(KEY_MAPPING[curses.KEY_LEFT], DIRECTION_LEFT)
        self.assertEqual(KEY_MAPPING[curses.KEY_RIGHT], DIRECTION_RIGHT)
        # Check vim keys
        self.assertEqual(KEY_MAPPING['k'], DIRECTION_UP)
        self.assertEqual(KEY_MAPPING['j'], DIRECTION_DOWN)
        self.assertEqual(KEY_MAPPING['h'], DIRECTION_LEFT)
        self.assertEqual(KEY_MAPPING['l'], DIRECTION_RIGHT)
        # Check ESDF keys
        self.assertEqual(KEY_MAPPING['e'], DIRECTION_UP)
        self.assertEqual(KEY_MAPPING['s'], DIRECTION_DOWN)
        self.assertEqual(KEY_MAPPING['d'], DIRECTION_RIGHT)
        self.assertEqual(KEY_MAPPING['f'], DIRECTION_LEFT)

if __name__ == "__main__":
    unittest.main()
