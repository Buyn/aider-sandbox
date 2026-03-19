# Next Action: Implement Configuration Module and Tests

## Objective
Create the `config.py` module within the `src/` directory that defines all configurable parameters as specified in the TECHNICAL_SPECIFICATION.md. Additionally, set up the project structure and write unit tests to verify the configuration.

## Rationale
The configuration module is the foundation for the entire game. All other modules (snake, food, renderer, input_handler, game) will depend on these settings. Implementing it first ensures that subsequent development has a single source of truth for all constants.

## Requirements from Specification
From Section 3.2 Configuration:
- `GRID_WIDTH = 50`
- `GRID_HEIGHT = 50`
- `TICKS_PER_SECOND = 2` (or `MOVE_INTERVAL = 0.5` seconds)
- Colors (ANSI escape codes) for snake body, snake head, food, and background.
- Key mappings: a dictionary mapping keys to directions (e.g., `KEY_UP = 'k'` or `'KEY_UP'` from curses).
- Any other tunable parameters.

Also, from Section 2.1 Functional Requirements:
- Grid size 50x50 cells (configurable) -> `GRID_WIDTH`, `GRID_HEIGHT`.
- Game speed: constant 2 moves per second (configurable) -> `TICKS_PER_SECOND`.
- Visuals: ANSI characters with colors -> color constants.
- Controls: arrow keys, vim keys (h, j, k, l), and ESDF -> key mappings.

## Implementation Plan

### 1. Project Structure
Create the following directories and files:
