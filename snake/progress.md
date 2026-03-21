# Project Progress

## Current Focus
Fixing test suite discovery, fixing InputHandler non-blocking issue, and ensuring all unit tests pass.

## Completed (implemented and reviewed)
- config.py: Implemented and reviewed.
- snake.py: Implemented and reviewed.
- food.py: Implemented and reviewed.
- renderer.py: Implemented and reviewed.
- game.py: Fixed relative imports, direction handling, growth logic, and state management (restart after game over). **Implementation complete, pending test validation.**
- input_handler.py: Implemented but **requires fix** for non-blocking input.

## In Progress
- Test suite discovery and validation.
- InputHandler non-blocking fix.

## Next Steps
1. Ensure test files are in `snake/tests/` and named `test_*.py`, and that `snake/src/` and `snake/tests/` are valid Python packages (add `__init__.py` if missing).
2. Fix InputHandler by setting `self.stdscr.nodelay(True)` in its `__init__` method.
3. Run `python -m unittest` from the project root and fix any test failures, particularly in `game.py`.
4. After all tests pass, refactor `game.py` to use `config.KEY_MAPPING`.

## Notes
- All source files now use relative imports within the package.
- The test suite currently fails to discover tests; `last_unittest_run.log` shows "NO TESTS RAN".
- InputHandler currently blocks; must be non-blocking.
- Refactor `game.py`'s key handling to use `config.KEY_MAPPING` after tests pass.
