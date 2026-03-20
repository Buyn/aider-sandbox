# Next Action: Fix Unit Tests for Input Handler

## Objective
Fix the failing unit tests in `tests/test_input_handler.py` by correcting the mock patch targets. The tests currently fail with `_curses.error: must call initscr() first` because the patches are applied to the wrong module. The `InputHandler` class uses the `curses` module imported at the top of `src/input_handler.py`, so the tests must patch `curses` functions in that module's namespace.

## Problem Description
The test methods use decorators like:
