import sys
import os

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

def test_grid_dimensions():
    assert GRID_WIDTH == 50
    assert GRID_HEIGHT == 50

def test_speed():
    assert TICKS_PER_SECOND == 2

def test_colors():
    assert COLOR_SNAKE_BODY == '\033[32m'
    assert COLOR_SNAKE_HEAD == '\033[92m'
    assert COLOR_FOOD == '\033[31m'
    assert COLOR_BACKGROUND == '\033[0m'

def test_characters():
    assert CHAR_SNAKE_BODY == '█'
    assert CHAR_SNAKE_HEAD == 'O'
    assert CHAR_FOOD == '●'

def test_direction_constants():
    assert DIRECTION_UP == (0, -1)
    assert DIRECTION_DOWN == (0, 1)
    assert DIRECTION_LEFT == (-1, 0)
    assert DIRECTION_RIGHT == (1, 0)

def test_key_mapping():
    # Check arrow keys
    assert KEY_MAPPING[curses.KEY_UP] == DIRECTION_UP
    assert KEY_MAPPING[curses.KEY_DOWN] == DIRECTION_DOWN
    assert KEY_MAPPING[curses.KEY_LEFT] == DIRECTION_LEFT
    assert KEY_MAPPING[curses.KEY_RIGHT] == DIRECTION_RIGHT
    # Check vim keys
    assert KEY_MAPPING['k'] == DIRECTION_UP
    assert KEY_MAPPING['j'] == DIRECTION_DOWN
    assert KEY_MAPPING['h'] == DIRECTION_LEFT
    assert KEY_MAPPING['l'] == DIRECTION_RIGHT
    # Check ESDF keys
    assert KEY_MAPPING['e'] == DIRECTION_UP
    assert KEY_MAPPING['s'] == DIRECTION_DOWN
    assert KEY_MAPPING['d'] == DIRECTION_RIGHT
    assert KEY_MAPPING['f'] == DIRECTION_LEFT
