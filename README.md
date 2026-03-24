# Snake Game

A console-based Snake game for Linux using ANSI characters and colors.

## Features

- Classic Snake gameplay with wrap-around boundaries.
- Configurable grid size, speed, colors, and key mappings.
- Optional visual wall display (purely cosmetic).
- Pause, restart, and exit functionality.

## Configuration

The game's behavior and appearance can be customized by editing `snake/src/config.py`. The wall display options are:

- `WALLS_ENABLED`: Whether to draw a border around the playable grid. The border is purely visual and does not affect gameplay (the snake still wraps). Default: `True`.
- `WALL_SYMBOL`: The character used for the wall border. Default: `'#'`.
- `WALL_COLOR`: The ANSI color code for the wall border. Default: `'\033[93m'` (bright yellow).

Other configurable parameters include grid dimensions, speed, colors, and key mappings.

## Requirements

- Python 3.x
- Linux environment
- Terminal supporting ANSI colors and cursor control

## Running the Game
