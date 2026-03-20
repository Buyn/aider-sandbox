# Project Progress

## Completed and reviewed


## Completed
- [x] Configuration module (`src/config.py`) implemented with all required constants.
- [x] Unit tests for config.py (`tests/test_config.py`) written and passing.
- [x] Project structure set up (`src/`, `tests/` directories).
- [x] Snake class (`src/snake.py`) implemented with movement, growth, wrap-around, and collision detection.
- [x] Unit tests for `snake.py` (`tests/test_snake.py`) written and passing.
- [x] Food class (`src/food.py`) implemented with random spawning avoiding snake body.
- [x] Unit tests for `food.py` (`tests/test_food.py`) written and passing.
- [x] Renderer class (`src/renderer.py`) implemented with ANSI color output.
- [x] Unit tests for `renderer.py` (`tests/test_renderer.py`) written and passing.
- [x] Input handler class (`src/input_handler.py`) implemented with support for pause (space) and restart ('r') actions.
- [ ] Unit tests for `input_handler.py` (`tests/test_input_handler.py`) - currently failing due to mocking issues; needs fix.

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
