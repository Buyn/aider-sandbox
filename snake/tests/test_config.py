import unittest
import sys
import os
# Add the project root (snake) to the Python path to ensure 'src' is importable
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src import config
import curses

class TestConfig(unittest.TestCase):
    def test_grid_dimensions(self):
        self.assertIsInstance(config.GRID_WIDTH, int)
        self.assertIsInstance(config.GRID_HEIGHT, int)
        self.assertGreater(config.GRID_WIDTH, 0)
        self.assertGreater(config.GRID_HEIGHT, 0)

    def test_tick_rate(self):
        # Check either TICKS_PER_SECOND or MOVE_INTERVAL exists and is positive
        if hasattr(config, 'TICKS_PER_SECOND'):
            self.assertIsInstance(config.TICKS_PER_SECOND, (int, float))
            self.assertGreater(config.TICKS_PER_SECOND, 0)
        if hasattr(config, 'MOVE_INTERVAL'):
            self.assertIsInstance(config.MOVE_INTERVAL, (int, float))
            self.assertGreater(config.MOVE_INTERVAL, 0)

    def test_colors(self):
        self.assertIsInstance(config.COLOR_SNAKE_HEAD, str)
        self.assertIsInstance(config.COLOR_SNAKE_BODY, str)
        self.assertIsInstance(config.COLOR_FOOD, str)
        # Typically start with ANSI escape
        self.assertTrue(config.COLOR_SNAKE_HEAD.startswith('\033['))
        self.assertTrue(config.COLOR_SNAKE_BODY.startswith('\033['))
        self.assertTrue(config.COLOR_FOOD.startswith('\033['))

    def test_characters(self):
        self.assertIsInstance(config.CHAR_SNAKE_HEAD, str)
        self.assertIsInstance(config.CHAR_SNAKE_BODY, str)
        self.assertIsInstance(config.CHAR_FOOD, str)
        self.assertEqual(len(config.CHAR_SNAKE_HEAD), 1)
        self.assertEqual(len(config.CHAR_SNAKE_BODY), 1)
        self.assertEqual(len(config.CHAR_FOOD), 1)

    def test_key_mapping(self):
        self.assertIsInstance(config.KEY_MAPPING, dict)
        for key in config.KEY_MAPPING.keys():
            self.assertIsInstance(key, int)  # integer key codes
        # Check direction mappings
        expected_direction_keys = {
            curses.KEY_UP: config.DIRECTION_UP,
            curses.KEY_DOWN: config.DIRECTION_DOWN,
            curses.KEY_LEFT: config.DIRECTION_LEFT,
            curses.KEY_RIGHT: config.DIRECTION_RIGHT,
            ord('k'): config.DIRECTION_UP,
            ord('j'): config.DIRECTION_DOWN,
            ord('h'): config.DIRECTION_LEFT,
            ord('l'): config.DIRECTION_RIGHT,
            ord('e'): config.DIRECTION_UP,
            ord('d'): config.DIRECTION_RIGHT,
            ord('s'): config.DIRECTION_DOWN,
            ord('f'): config.DIRECTION_LEFT,
        }
        for key, expected_dir in expected_direction_keys.items():
            self.assertIn(key, config.KEY_MAPPING)
            self.assertEqual(config.KEY_MAPPING[key], expected_dir)
        # Check action mappings
        self.assertEqual(config.KEY_MAPPING[ord(' ')], config.ACTION_PAUSE)
        self.assertEqual(config.KEY_MAPPING[ord('r')], config.ACTION_RESTART)

    def test_direction_constants(self):
        self.assertTrue(hasattr(config, 'DIRECTION_UP'))
        self.assertTrue(hasattr(config, 'DIRECTION_DOWN'))
        self.assertTrue(hasattr(config, 'DIRECTION_LEFT'))
        self.assertTrue(hasattr(config, 'DIRECTION_RIGHT'))
        self.assertEqual(config.DIRECTION_UP, (0, -1))
        self.assertEqual(config.DIRECTION_DOWN, (0, 1))
        self.assertEqual(config.DIRECTION_LEFT, (-1, 0))
        self.assertEqual(config.DIRECTION_RIGHT, (1, 0))

if __name__ == '__main__':
    unittest.main()
