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

**Note:** The 22 unit tests for config, snake, food, and renderer modules pass. Input handler tests are not yet passing due to missing pause/restart support.

## In Progress
- [ ] `input_handler.py` to capture keys (directional keys work; pause/restart pending).
- [ ] Unit tests for `input_handler.py` (some tests failing due to missing action mappings).

**Note:** The current implementation of `input_handler.py` lacks support for pause (space) and restart ('r') actions, causing related tests to fail. This must be addressed to complete the input handler.

## Next Steps
- Implement `game.py` with main loop and state management.
- Write unit tests for `game.py`.
- Create a main entry point (e.g., `main.py` or `__main__.py`).
- Test and refine the entire game.
