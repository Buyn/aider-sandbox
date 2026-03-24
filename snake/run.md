# Task: Implement Exit Functionality

## Objective
Implement the exit functionality as specified in the technical specification: the game should exit gracefully when the user presses 'q' or the ESC key.

## Background
The core game mechanics are complete and all existing unit tests pass (39 tests, 1 skipped). The main game loop currently handles directional input, pause (space), and restart ('r'). Exit functionality is the missing piece before the project can be considered feature-complete. The optional wall display feature will be addressed after exit functionality is complete and reviewed.

## Requirements
1. **Exit Keys**: The game must respond to both 'q' and ESC keys by exiting the game loop and performing cleanup.
2. **Graceful Exit**: When an exit key is detected, the game loop should break, and the program should call `input_handler.cleanup()` to restore terminal settings before exiting. Ensure no double cleanup occurs (the entry point already handles cleanup after `game.run()` returns).
3. **Input Handling**: The `InputHandler` class should properly detect the ESC key. With curses, ESC may be represented as a special key constant (e.g., `curses.KEY_EXIT` or key code 27). Ensure cross-terminal compatibility; test on typical Linux terminals.
4. **Game Loop**: In `Game.run()`, after processing input, check if the input indicates an exit request. If so, break the main loop. The exit should be possible from any game state (playing, paused, game over).
5. **Unit Tests**: Add unit tests to `snake/tests/test_game.py` to verify:
   - Pressing 'q' causes the game loop to exit.
   - Pressing ESC causes the game loop to exit.
   - The exit path does not interfere with pause/restart functionality.
   - Cleanup is called exactly once when exiting (existing `test_cleanup.py` should still pass; ensure no regression).
6. **Integration Testing**: After implementation, perform manual integration testing to verify that pressing 'q' or ESC exits the game and returns the terminal to a usable state (no lingering curses settings).

## Additional Notes
- The existing `test_cleanup.py` already verifies that cleanup is called exactly once from the entry point. Ensure that the exit path still satisfies these tests; do not introduce additional cleanup calls.
- The `Game` class currently has a `game_over` flag. Exit functionality should be independent of game state; pressing 'q' or ESC should exit regardless of whether the game is paused, running, or in game over state.
- The `_handle_key` method in `Game` is a natural place to handle exit keys, or the main loop in `run()` can check for a special return value from `_handle_key`. Choose an approach that keeps the code clean and testable.
- Consider whether the exit key should be processed even when the game is paused. The specification implies it should always exit; implement accordingly.
- Ensure that the ESC key detection works reliably across different terminals. Using curses' built-in key constants (e.g., `curses.KEY_EXIT` if available, or checking for 27) is recommended. Be aware that some terminals may send different sequences; test thoroughly.
- After implementing exit functionality, all existing unit tests must continue to pass. Do not break any existing behavior.
- Once exit functionality is complete and tested, the next feature to implement will be the optional wall display (see technical_specification.md section 2.1 and 3.5). But focus solely on exit functionality for this task.

## Referenced code quoting
(No specific code changes are prescribed; the programmer will determine the exact implementation based on these requirements and the existing codebase.)
