# Review logs and comments
## Files reviewed
- config.py: Reviewed, meets specification.
- snake.py: Reviewed, meets specification.
- food.py: Reviewed, meets specification.
- renderer.py: Reviewed, meets specification.
- input_handler.py: **Needs fix** - uses blocking `getch`; must set `nodelay` for non-blocking input as per specification.
- game.py: Reviewed after fixes; implementation appears correct but requires validation via unit tests. **Status: Pending test validation.**

## Issues to address
- **Test suite discovery**: Tests are not being discovered. The `last_unittest_run.log` shows "NO TESTS RAN". No test file in location `snake/tests/`.
- **Key mapping refactor**: After all tests pass, refactor `game.py`'s `_key_to_direction` method to use `config.KEY_MAPPING` instead of hardcoded mappings. Note: `config.KEY_MAPPING` may need to use integer key codes (e.g., `ord('k')`) to match `getch` return values.

## Notes for future sessions
