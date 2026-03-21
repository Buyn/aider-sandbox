# Task:
## Objective
Fix test suite discovery, fix InputHandler non-blocking issue, ensure all unit tests pass, then refactor game.py to use config.KEY_MAPPING.

## Background
The test suite is not being discovered when running `python -m unittest`. The last_unittest_run.log shows "NO TESTS RAN". Additionally, InputHandler uses blocking getch, violating the non-blocking requirement from the specification. All other modules (config, snake, food, renderer) have been implemented and reviewed, but game.py needs to pass its unit tests. game.py currently uses hardcoded key mappings instead of the centralized config.KEY_MAPPING, which is a non-compliance.

## Issues to Address
1. **Test discovery**: Ensure tests are discoverable by unittest. Check that test files are in `snake/tests/` and follow naming conventions (`test_*.py`). Ensure `snake/tests/` is a package (has `__init__.py`). Also ensure tests can import the `src` modules (may need to adjust PYTHONPATH or use proper absolute imports like `from snake.src.snake import Snake`). Run `python -m unittest` from the project root.
2. **InputHandler non-blocking**: Modify `InputHandler.__init__` to call `self.stdscr.nodelay(True)` to make `get_key` non-blocking. This ensures the game loop does not wait for key presses.
3. **Test failures**: Once tests are discovered and InputHandler is non-blocking, run the tests and fix any failures, particularly in `game.py` (direction handling, growth logic, state management) to meet the specification.
4. **Refactor key handling**: After all tests pass, modify `game.py`'s `_key_to_direction` method to use `config.KEY_MAPPING` instead of hardcoded mappings. Note: `config.KEY_MAPPING` may need adjustment to use integer key codes (e.g., `ord('k')` instead of `'k'`) to match the integer values returned by `getch`.

## Additional Notes
- Do not introduce new features until all tests pass.
- Refer to `technical_specification.md` for requirements on input handling and key mappings.
- The project uses relative imports; ensure any changes maintain that.
- Verify that `InputHandler.get_key` returns `None` when no key is pressed and does not block.

## Referenced code quoting
(No specific code needed; the programmer should inspect existing code and tests.)
