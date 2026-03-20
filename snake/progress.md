# Project Progress

## Current Focus
Fixing unit tests for `input_handler.py` to ensure a green test suite before implementing `game.py`. See `run.md` for detailed task.

## Completed and reviewed (implementations)
- [x] Configuration module (`src/config.py`) implemented with all required constants.
- [x] Snake class (`src/snake.py`) implemented with movement, growth, wrap-around, and collision detection.
- [x] Food class (`src/food.py`) implemented with random spawning avoiding snake body.
- [x] Renderer class (`src/renderer.py`) implemented with ANSI color output.
- [x] Input handler class (`src/input_handler.py`) implemented with support for pause (space) and restart ('r') actions. (Implementation reviewed and correct; unit tests need mocking fix.)

## Completed (tests)
- [x] Unit tests for config.py (`tests/test_config.py`) written and passing.
- [x] Unit tests for snake.py (`tests/test_snake.py`) written and passing.
- [x] Unit tests for food.py (`tests/test_food.py`) written and passing.
- [x] Unit tests for renderer.py (`tests/test_renderer.py`) written and passing.
- [ ] Unit tests for input_handler.py (`tests/test_input_handler.py`) - currently failing due to mocking issues; needs fix.

## In Progress
- [ ] Fix unit tests for `input_handler.py` (mocking issues).
- [ ] `game.py` with main loop and state management.
- [ ] Unit tests for `game.py`.

## Next Steps
- Fix unit tests for `input_handler.py` to ensure all tests pass.
- Implement `game.py` with main loop and state management.
- Write unit tests for `game.py`.
- Create a main entry point (e.g., `main.py` or `__main__.py`).
- Test and refine the entire game.
