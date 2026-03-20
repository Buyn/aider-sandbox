# Task: Implement game.py

## Objective
Implement the main game loop and state management in `snake/src/game.py`.

## Requirements
- Create a `Game` class that holds:
  - `snake`: instance of `Snake`
  - `food`: instance of `Food`
  - `direction`: current movement direction (initially from config or snake's direction)
  - `paused`: boolean
  - `game_over`: boolean
  - `config`: reference to configuration (from `config.py`)
- The main game loop should:
  1. Process input from `InputHandler` (non-blocking) and update direction accordingly. Handle special keys: space to toggle pause, 'r' to restart.
  2. If not paused and not game over, move the snake (with growth if food eaten).
  3. Check for collisions: self-collision ends the game (set `game_over`).
  4. If snake head collides with food, grow the snake and spawn new food (using `Food.spawn` with occupied positions from snake's body).
  5. Render the current state using `Renderer.render`.
  6. Sleep to maintain the game speed (2 moves per second from config).
- On game over, the game should wait for 'r' to restart. Restarting should reset the snake and food, and clear game_over and paused states.
- The game should run until interrupted (e.g., Ctrl+C).

## Implementation Notes
- Use the existing modules: `snake`, `food`, `renderer`, `input_handler`, `config`.
- The `InputHandler` should be instantiated once and its `get_key` method called each loop. Remember to call `cleanup` on exit.
- The `Renderer` should clear the screen each frame using ANSI codes as implemented.
- Ensure the game speed is controlled by `TICKS_PER_SECOND` or similar from config.
- Handle direction changes safely: prevent reversing direction (e.g., if moving right, cannot go left immediately).
- The `game.py` file should be placed in `snake/src/`.
- After implementation, write comprehensive unit tests for `game.py` in `snake/tests/test_game.py`. Use mocking for input and time where necessary.
- Follow the Python code style: keep functions short, modular, avoid comments, use descriptive names.

## Verification
- All existing unit tests must continue to pass.
- The game should be playable in a Linux terminal with ANSI support.
- Test pause, restart, and game over conditions manually.
- Unit tests for `game.py` should cover the game loop logic, state transitions, and handling of input.

## References
- See `snake/technical_specification.md` for full details.
- See `snake/progress.md` for project status.
