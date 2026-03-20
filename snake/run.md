# Task: Fix Input Handler Unit Tests

## Description
The unit tests for `src/input_handler.py` are failing due to incorrect mock patch targets. The `InputHandler` class uses the `curses` module imported within `src/input_handler.py`, but the tests are patching the top-level `curses` module. This causes a `_curses.error: must call initscr() first` because the actual `curses.initscr()` is called without being patched.

## Required Changes
In `tests/test_input_handler.py`, update all `@patch` decorators to target the `curses` module as it is imported in `src/input_handler.py`:

- Change `@patch('curses.initscr')` to `@patch('snake.src.input_handler.curses.initscr')`
- Change `@patch('curses.endwin')` to `@patch('snake.src.input_handler.curses.endwin')`
- Change `@patch('curses.noecho')` to `@patch('snake.src.input_handler.curses.noecho')`
- Change `@patch('curses.cbreak')` to `@patch('snake.src.input_handler.curses.cbreak')`

Apply these changes to every test method in the `TestInputHandler` class that uses these patches.

## Verification
After making the changes, run the test suite:
