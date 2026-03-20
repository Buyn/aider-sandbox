# Task: Fix game.py to pass unit tests

## Objective
Correct the implementation of `snake/src/game.py` so that all unit tests in `snake/tests/test_game.py` pass.

## Background
The `game.py` module has been implemented but contains several issues that cause the unit tests to fail. The tests are already written and cover the required behavior. Your task is to fix the code to satisfy these tests.

## Issues to Address
1. **Import statements**: The current imports are absolute (`import snake`, `import food`, etc.). They should be relative imports within the package to correctly reference modules in the same package. Change to:
   ```python
   from . import snake, food, renderer, input_handler, config
   ```
   or import specific classes as needed.

2. **Missing `direction` attribute**: The `Game` class must have a `direction` attribute that mirrors the snake's current direction. In `__init__`, add:
   ```python
   self.direction = self.snake.direction
   ```
   Ensure this attribute stays in sync when the snake's direction changes (e.g., in the input handling loop, you may update `self.direction` when you call `self.snake.set_direction`).

3. **`restart` method does not reset `direction`**: After restarting, `self.direction` should be set to the new snake's direction. Add:
   ```python
   self.direction = self.snake.direction
   ```
   at the end of `restart`.

4. **Growth logic formatting**: There is a syntax error in the growth block: the line after `self.snake.body.append(old_tail)` has a comment and code on the same line. Ensure it is two separate lines:
   ```python
   self.snake.body.append(old_tail)
   self.food.spawn(self.snake.get_body())
   ```

5. **Potential import of `renderer` and `input_handler`**: Ensure these are also imported relatively.

6. **Ensure proper cleanup**: The `run` method already uses try/finally to call `self.input_handler.cleanup()`. That's good.

## Additional Notes
- The tests mock `time.sleep` and `input_handler.get_key`, so your implementation should use `time.sleep` with the interval from `config.TICKS_PER_SECOND` and call `self.input_handler.get_key()` each loop.
- The `Game` class should have `__init__`, `run`, and `restart` methods as expected by the tests.
- The `run` loop should handle input, movement, collision, food consumption, rendering, and sleeping as described in the specification.
- The `restart` method should reset the snake and food to initial states, and clear `paused` and `game_over`.
- After fixes, run `python -m unittest` to verify all tests pass.

## References
- See `snake/technical_specification.md` for full requirements.
- See `snake/progress.md` for current status.
