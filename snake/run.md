# Task:
## Objective
Implement the main entry point for the Snake game to allow launching from the command line.

## Background
All core modules (config, snake, food, renderer, input_handler, game) are implemented and unit tests pass (29 tests). The technical specification (section 3.7, step 8) requires a main entry point (e.g., main.py or __main__.py) to start the game.

## Issues to Address
None in existing code; this is a new component.

## Additional Notes
- The entry point should be placed in the `src` directory to maintain project structure.
- It should initialize the `Game` class and call its `run` method.
- Ensure proper handling of terminal cleanup (curses) on exit. The `InputHandler` likely handles cleanup, but verify.
- The game should be runnable via `python -m snake.src` (if using `__main__.py`) or `python snake/src/main.py`.
- No additional features; just the bootstrap.
- After implementation, perform manual integration testing to verify:
  - Snake appears and moves continuously.
  - Food spawns at random locations.
  - Controls work: arrow keys, vim keys (h,j,k,l), ESDF for direction; space to pause; 'r' to restart after game over.
  - Wrap-around at grid boundaries.
  - Self-collision ends the game.
  - Visuals: snake body as '█', head as 'O', food as '●', with appropriate colors.

## Referenced code quoting
N/A (new file)
