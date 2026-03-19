import sys
import os

# Add src directory to path to import food and config
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from food import Food
from config import GRID_WIDTH, GRID_HEIGHT

def test_initialization_with_position():
    pos = (5, 10)
    food = Food(pos)
    assert food.get_position() == pos

def test_initialization_without_position():
    food = Food()
    assert food.get_position() is None

def test_spawn_single_occupancy():
    food = Food()
    occupied = {(1, 2)}
    food.spawn(occupied)
    pos = food.get_position()
    assert pos is not None
    assert 0 <= pos[0] < GRID_WIDTH
    assert 0 <= pos[1] < GRID_HEIGHT
    assert pos not in occupied

def test_spawn_multiple_occupancy():
    food = Food()
    occupied = {(1, 2), (3, 4), (5, 6)}
    food.spawn(occupied)
    pos = food.get_position()
    assert pos is not None
    assert 0 <= pos[0] < GRID_WIDTH
    assert 0 <= pos[1] < GRID_HEIGHT
    assert pos not in occupied

def test_spawn_no_space():
    food = Food()
    occupied = {(x, y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)}
    try:
        food.spawn(occupied)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert "No free positions" in str(e)

def test_spawn_randomness():
    food = Food()
    occupied = set()
    positions = set()
    for _ in range(20):
        food.spawn(occupied)
        pos = food.get_position()
        positions.add(pos)
    assert len(positions) >= 2, f"Only got {len(positions)} distinct positions: {positions}"
