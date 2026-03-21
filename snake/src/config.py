# Grid dimensions
GRID_WIDTH = 50
GRID_HEIGHT = 50

# Game speed: moves per second
TICKS_PER_SECOND = 2
# Optional: MOVE_INTERVAL = 1.0 / TICKS_PER_SECOND

# ANSI color codes (foreground)
COLOR_SNAKE_BODY = '\033[32m'   # Green
COLOR_SNAKE_HEAD = '\033[92m'   # Bright green
COLOR_FOOD = '\033[31m'         # Red
COLOR_BACKGROUND = '\033[0m'    # Reset/default

# Characters
CHAR_SNAKE_BODY = '█'
CHAR_SNAKE_HEAD = 'O'
CHAR_FOOD = '●'

# Direction vectors
DIRECTION_UP = (0, -1)
DIRECTION_DOWN = (0, 1)
DIRECTION_LEFT = (-1, 0)
DIRECTION_RIGHT = (1, 0)

# Action constants
ACTION_PAUSE = 'PAUSE'
ACTION_RESTART = 'RESTART'

# Key mappings: map key codes to direction vectors or actions.
# We include both character keys and curses key constants.
import curses

KEY_MAPPING = {
    # Arrow keys (curses constants)
    curses.KEY_UP: DIRECTION_UP,
    curses.KEY_DOWN: DIRECTION_DOWN,
    curses.KEY_LEFT: DIRECTION_LEFT,
    curses.KEY_RIGHT: DIRECTION_RIGHT,
    # Vim keys
    ord('k'): DIRECTION_UP,
    ord('j'): DIRECTION_DOWN,
    ord('h'): DIRECTION_LEFT,
    ord('l'): DIRECTION_RIGHT,
    # ESDF keys
    ord('e'): DIRECTION_UP,
    ord('d'): DIRECTION_RIGHT,
    ord('s'): DIRECTION_DOWN,
    ord('f'): DIRECTION_LEFT,
    # Special actions
    ord(' '): ACTION_PAUSE,
    ord('r'): ACTION_RESTART,
}
