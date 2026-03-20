# Project Progress

## Current Focus
Fixing `game.py` to pass unit tests. See `run.md` for detailed task.

## Completed and reviewed (implementations)
- [x] Configuration module (`src/config.py`) implemented with all required constants.
- [x] Snake class (`src/snake.py`) implemented with movement, growth, wrap-around, and collision detection.
- [x] Food class (`src/food.py`) implemented with random spawning avoiding snake body.
- [x] Renderer class (`src/renderer.py`) implemented with ANSI color output.
- [x] Input handler class (`src/input_handler.py`) implemented with support for pause (space) and restart ('r') actions.

## Completed (tests)
- [x] Unit tests for config.py (`tests/test_config.py`) written and passing.
- [x] Unit tests for snake.py (`tests/test_snake.py`) written and passing.
- [x] Unit tests for food.py (`tests/test_food.py`) written and passing.
- [x] Unit tests for renderer.py (`tests/test_renderer.py`) written and passing.
- [x] Unit tests for input_handler.py (`tests/test_input_handler.py`) written and passing.
- [ ] Unit tests for game.py (`tests/test_game.py`) written but currently failing due to issues in `game.py` implementation.

## In Progress
- [ ] Fixing `game.py` to pass unit tests.
- [ ] Ensuring all tests pass with `python -m unittest`.

## Next Steps
- Fix `game.py` to satisfy the existing test_game.py (see `run.md` for specific issues).
- Ensure all tests pass.
- Create a main entry point (e.g., `main.py` or `__main__.py`) to run the game.
- Test and refine the entire game manually.

## Notes
- The `game.py` implementation has the following issues that need to be addressed:
  - Import statements should be relative within the package.
  - The `Game` class lacks a `direction` attribute; it should be initialized from the snake's direction and kept in sync.
  - The `restart` method does not reset `direction` to the new snake's direction.
  - There is a formatting/syntax error in the food growth block (comment and code on same line).
- Pay attention to proper cleanup of `InputHandler` (curses) on exit to avoid terminal corruption.
- The tests mock `time.sleep`; ensure the loop uses `time.sleep` with the correct interval from config.
