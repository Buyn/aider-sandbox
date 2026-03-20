# Snake Game Technical Specification

## 1. Project Overview
A console-based Snake game for Linux using ANSI characters and colors. The game will be implemented in Python with a modular architecture.

### 1.1 Current Implementation Status
The following modules have been implemented and have unit tests:
- `config.py`: Configuration settings.
- `snake.py`: Snake class with movement, growth, wrap-around, and collision detection.
- `food.py`: Food class with random spawning.
- `renderer.py`: Renderer class with ANSI output.
- `input_handler.py`: Input handling with curses, supporting directional keys, pause (space), and restart ('r').

Note: The unit tests for `input_handler.py` currently fail due to improper mocking of the curses module in the test suite. The implementation is correct; the tests need to be fixed to properly patch the curses functions used by `InputHandler`.

The next module to implement is `game.py` with main loop and state management.

## 2. Requirements

### 2.1 Functional Requirements
- The game area is a grid of 50x50 cells (configurable).
- The snake moves continuously in the current direction.
- The snake grows when it eats food.
- The snake dies if it collides with itself.
- The snake wraps around when hitting the grid boundaries (no wall collisions).
- Food appears at random locations not occupied by the snake.
- Controls: arrow keys, vim keys (h, j, k, l), and ESDF for direction.
- Pause functionality: space bar toggles pause.
- After game over, pressing 'r' restarts the game.
- No scoring system (no points displayed).

### 2.2 Non-Functional Requirements
- Platform: Linux only.
- Use external libraries for input handling (e.g., `curses`, `readchar`, `keyboard`).
- Game speed: constant 2 moves per second (configurable).
- Visuals: ANSI characters with colors:
  - Snake body: '█' (full block)
  - Snake head: 'O'
  - Food: '●'
  - No borders around the game area.
- The game should run in a terminal that supports ANSI colors and cursor control.

## 3. Technical Design

### 3.1 Architecture
The project will be organized into the following modules:

- `config.py`: Configuration settings (grid size, speed, colors, key mappings, etc.).
- `snake.py`: Snake class representing the snake's body, movement, growth, and collision detection.
- `food.py`: Food class for spawning and managing food items.
- `renderer.py`: Handles all terminal output, including drawing the snake, food, and handling colors.
- `input_handler.py`: Captures keyboard input in a non-blocking manner, supporting the required key sets.
- `game.py`: Main game loop, orchestrating the game state, input, rendering, and timing.
- and test files

### 3.2 Configuration
All configurable parameters will be stored in `config.py` as constants or a configuration class/object. This includes:
- `GRID_WIDTH = 50`
- `GRID_HEIGHT = 50`
- `TICKS_PER_SECOND = 2` (or `MOVE_INTERVAL = 0.5` seconds)
- Colors (ANSI escape codes) for snake body, snake head, food, and background.
- Key mappings: a dictionary mapping keys to directions (e.g., `KEY_UP = 'k'` or `'KEY_UP'` from curses).
- Any other tunable parameters.

### 3.3 Game Loop
The main loop will:
1. Process input (non-blocking) and update direction accordingly.
2. If not paused, update snake position based on current direction.
3. Check for collisions (self-collision) and food consumption.
4. If food eaten, grow snake and spawn new food.
5. Render the current state to the terminal.
6. Sleep to maintain the configured speed.

### 3.4 Input Handling
- Use a library like `curses` (standard) or `readchar` (third-party) to capture key presses without requiring Enter.
- Support both arrow keys and the specified character keys (h, j, k, l, e, s, d, f).
- Map keys to directions: up, down, left, right.
- Also handle space (pause) and 'r' (restart).

### 3.5 Rendering
- Use ANSI escape codes to clear the screen and position the cursor.
- Draw each cell of the snake and food using the appropriate character and color.
- The entire grid is redrawn each frame (or use incremental updates if performance requires, but for 50x50 it's fine).
- No borders; just the snake and food on a blank background.

### 3.6 Game State
- The `Game` class will hold:
  - `snake`: instance of `Snake`
  - `food`: instance of `Food`
  - `direction`: current movement direction
  - `paused`: boolean
  - `game_over`: boolean
  - `config`: reference to configuration

## 4. Dependencies
- Python 3.x
- Linux environment
- Recommended: `curses` (built-in) for input and terminal control.
- Alternatively: `readchar` (pip install readchar) for simpler key reading.
- testig framework

## 5. Platform
- Linux only. The code may use terminal-specific features (e.g., `curses` with ncurses) that are not portable to Windows without adjustments.

## 6. Implementation Steps
1. Set up project structure with `src/` directory and modules.
2. Create `config.py` with all settings.
3. Implement `snake.py` with movement, growth, and wrap-around logic.
4. Implement `food.py` with random spawning avoiding snake body.
5. Implement `renderer.py` with ANSI color output.
6. Implement `input_handler.py` to capture keys.
7. Implement `game.py` with main loop and state management.
8. Create a main entry point (e.g., `main.py` or `__main__.py`).
9. Test and refine.

## 7. Future Considerations (Optional)
- High score tracking.
- Adjustable difficulty (speed increase).
- Multiple food types.
- Sound effects (if terminal supports).
