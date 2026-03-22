# Task:
## Objective
Fix the double cleanup issue in the game termination sequence and then perform manual integration testing to verify all gameplay features.

## Background
The game uses `curses` for input handling. Both `game.run()` and `__main__.py` have `finally` blocks that call `input_handler.cleanup()`. This results in calling `cleanup()` twice when the game exits (e.g., via Ctrl+C). The second call may fail because after the first `curses.endwin()`, the curses screen is closed and further curses operations can cause errors. This needs to be resolved to ensure clean terminal restoration.

## Issues to Address
1. **Double cleanup bug**: Identify why cleanup is called twice and modify the code so that cleanup happens exactly once, regardless of how the game exits (exception or normal termination). The responsibility for cleanup should be clearly assigned. Consider:
   - Removing the `finally` block from `game.run()` and relying on `__main__.py`'s `finally` (as per the specification that the entry point ensures cleanup).
   - Or, keep the `finally` in `game.run()` and remove it from `__main__.py`.
   Ensure that the terminal is always restored to a usable state.
2. **Manual integration testing**: After fixing the cleanup issue, run the game with `python -m snake.src` and verify:
   - All controls work (arrow keys, vim keys, ESDF, space for pause, 'r' for restart).
   - Visuals match the specification (colors, characters, no borders).
   - Gameplay mechanics (movement, growth, wrap-around, self-collision, food spawning).
   - Pause and restart functionality.
   - The game runs at the correct speed (2 moves per second).
   - The terminal is properly restored after exit (no lingering curses settings, cursor visible, etc.).

## Additional Notes
- The technical specification (snake/technical_specification.md) provides full details on requirements.
- All unit tests pass (29 tests), but the double cleanup issue is not covered by unit tests because they mock the input handler.
- The fix should be minimal and not alter the overall architecture.

## Referenced code quoting
- `snake/src/game.py`: contains the `run` method with a `finally` block that calls `self.input_handler.cleanup()`.
- `snake/src/__main__.py`: contains a `finally` block that calls `game.input_handler.cleanup()`.
