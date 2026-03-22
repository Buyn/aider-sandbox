# Task:
## Objective
Add comprehensive unit tests for the Food class to ensure its correctness and increase test coverage.

## Background
The Food class is currently only tested indirectly through game tests, which mock the Food class. Direct unit tests for Food are missing. This leaves a gap in test coverage and makes it harder to verify the food spawning logic in isolation.

## Issues to Address
- The Food class has no dedicated test file (test_food.py).
- The spawn method's behavior (random position not occupied) is not directly verified.
- Edge cases such as spawning when the grid is nearly full are not tested.

## Additional Notes
- Use the unittest framework.
- Follow the existing test structure and style in test_snake.py and test_game.py.
- Since Food.spawn uses randomness, consider patching the random module or testing properties (e.g., position is within grid bounds, not in occupied list) rather than exact values.
- Ensure tests are deterministic and reliable.
- Place the new test file in snake/tests/test_food.py.
- Run all tests with `python -m unittest` to ensure they pass and don't break existing tests.

## Referenced code quoting
(No code quoting needed; refer to src/food.py for implementation details.)
