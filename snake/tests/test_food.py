import sys
import os
import unittest

# Add src directory to path to import food and config
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from food import Food
from config import GRID_WIDTH, GRID_HEIGHT

class TestFood(unittest.TestCase):
    def test_initialization_with_position(self):
        pos = (5, 10)
        food = Food(pos)
        self.assertEqual(food.get_position(), pos)

    def test_initialization_without_position(self):
        food = Food()
        self.assertIsNone(food.get_position())

    def test_spawn_single_occupancy(self):
        food = Food()
        occupied = {(1, 2)}
        food.spawn(occupied)
        pos = food.get_position()
        self.assertIsNotNone(pos)
        self.assertGreaterEqual(pos[0], 0)
        self.assertLess(pos[0], GRID_WIDTH)
        self.assertGreaterEqual(pos[1], 0)
        self.assertLess(pos[1], GRID_HEIGHT)
        self.assertNotIn(pos, occupied)

    def test_spawn_multiple_occupancy(self):
        food = Food()
        occupied = {(1, 2), (3, 4), (5, 6)}
        food.spawn(occupied)
        pos = food.get_position()
        self.assertIsNotNone(pos)
        self.assertGreaterEqual(pos[0], 0)
        self.assertLess(pos[0], GRID_WIDTH)
        self.assertGreaterEqual(pos[1], 0)
        self.assertLess(pos[1], GRID_HEIGHT)
        self.assertNotIn(pos, occupied)

    def test_spawn_no_space(self):
        food = Food()
        occupied = {(x, y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)}
        with self.assertRaises(ValueError) as context:
            food.spawn(occupied)
        self.assertIn("No free positions", str(context.exception))

    def test_spawn_randomness(self):
        food = Food()
        occupied = set()
        positions = set()
        for _ in range(20):
            food.spawn(occupied)
            pos = food.get_position()
            positions.add(pos)
        self.assertGreaterEqual(len(positions), 2, f"Only got {len(positions)} distinct positions: {positions}")

if __name__ == "__main__":
    unittest.main()
