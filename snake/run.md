# Next Action: Add Pause and Restart Support to Input Handler

## Objective
Complete the `InputHandler` class by adding support for pause (space bar) and restart ('r' key) actions. This involves:
- Updating `src/config.py` to define action constants `ACTION_PAUSE` and `ACTION_RESTART`.
- Adding key mappings in `config.KEY_MAPPING` for `' '` (space) and `'r'` to these action constants.
- Ensuring that `InputHandler.get_key()` returns `ACTION_PAUSE` when space is pressed and `ACTION_RESTART` when 'r' is pressed.
- Verifying that all unit tests in `tests/test_input_handler.py` pass, particularly `test_get_key_special_actions`.

## Implementation Plan

### 1. Update `src/config.py`
- Add the following constants:
  ```python
  ACTION_PAUSE = 'PAUSE'
  ACTION_RESTART = 'RESTART'
  ```
- Extend `KEY_MAPPING` dictionary:
  ```python
      ' ': ACTION_PAUSE,
      'r': ACTION_RESTART,
  ```

### 2. Verify `src/input_handler.py` compatibility
- No changes needed to `input_handler.py` if it already uses `KEY_MAPPING` from `config`. Ensure it imports `KEY_MAPPING` correctly.
- Confirm that `get_key` returns the mapped value for space and 'r'.

### 3. Run Tests
- Execute all unit tests: `python -m unittest` or `pytest tests/`.
- Ensure all tests pass, including the special actions test.

## Success Criteria
- `config.py` includes `ACTION_PAUSE` and `ACTION_RESTART` constants and maps space and 'r' to them.
- `InputHandler.get_key()` returns the correct action constants for space and 'r'.
- All unit tests pass.

## Notes
- The game loop (to be implemented later) will use these action constants to control pause and restart behavior.
- Ensure that the mapping for space uses the character `' '` (space) and not any other representation.
