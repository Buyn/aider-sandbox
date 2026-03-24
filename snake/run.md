# Task:
## Objective
Implement exit functionality (q/ESC keys) to allow the player to quit the game gracefully.

## Background
The game currently supports pause, restart, but lacks a way to exit. The technical specification requires that pressing 'q' or ESC exits the game. The main entry point (`__main__.py`) already handles cleanup, so the game loop needs to detect exit keys and break out of the loop, returning control to the entry point.

## Issues to Address
- Detect 'q' key and ESC key in the input handling.
- Ensure that when exit is requested, the game loop terminates and control returns to the entry point without calling cleanup (cleanup is handled by `__main__.py`).
- The ESC key may be represented as a special key code in curses (e.g., 27 or `curses.KEY_EXIT`). Need to handle it properly across terminals.
- The exit should work regardless of game state (paused, playing, game over).
- Ensure that after exit, the game loop breaks and the `run()` method returns.
- Do not break existing functionality (pause, restart, direction changes).
- Consider adding unit tests for exit handling in `test_game.py` to verify that the game exits correctly when 'q' or ESC is pressed. Ensure that cleanup is still called exactly once (existing `test_cleanup.py` should pass).
- The `input_handler.py` may need to expose the ESC key appropriately; currently it returns key codes. Ensure that ESC is distinguishable from other keys.

## Additional Notes
- The `Game` class's `_handle_key` method is the appropriate place to handle exit keys. It can set a flag like `self.exit_requested = True`, and the `run` loop can check this flag to break.
- Alternatively, the `run` loop could break directly if `_handle_key` returns a signal. Choose a clean design consistent with existing code.
- The `input_handler.get_key()` returns key codes; for ESC, it might return `'\x1b'` or a numeric code (27). Test in the actual terminal to determine representation. Using `curses` constants is recommended if available.
- The `__main__.py` already wraps `game.run()` in a try/finally to call cleanup. Ensure that when exit is requested, `game.run()` returns normally (not via exception) so that cleanup is called exactly once.
- After implementation, run all unit tests to ensure no regressions.
- Update documentation (`snake/README.md`) to mention the exit keys if needed, but that may be a later step.

## Referenced code quoting
From `technical_specification.md`: "Exit functionality: pressing 'q' or ESC exits the game."
From `input_handler.py`: The `get_key` method returns key codes.
From `game.py`: The `run` loop and `_handle_key` method.
