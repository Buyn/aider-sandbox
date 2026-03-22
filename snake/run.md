# Task:
## Objective
Write comprehensive unit tests for the Food class in `snake/tests/test_food.py` to verify its behavior in isolation, with a focus on the `spawn` method's logic for generating random positions that avoid occupied cells.

## Background
The Food class implementation is complete and has been verified through integration tests. However, dedicated unit tests are missing. Adding these tests will increase test coverage, ensure the spawn logic is robust, and provide a safety net for future changes.

## Issues to Address
- Test all public methods: `__init__` (with and without position argument), `spawn(occupied_positions)`, and `get_position()`.
- Verify that `spawn` returns a position not present in `occupied_positions`.
- Test edge cases: spawning with an empty occupied list, spawning with a full grid (should handle gracefully, though unlikely), spawning after multiple calls to ensure randomness (use mocking to control random output).
- Use `unittest.mock.patch` to mock the `random` module if needed to make tests deterministic.
- Follow the project's test conventions: use `unittest`, absolute imports (`from src import food` or similar), and ensure the test file is discoverable via `python -m unittest`.
- Ensure tests are independent and do not share state.
- After implementation, run the full test suite to confirm no regressions.

## Additional Notes
- The Food class resides in `snake/src/food.py`. Refer to it for method signatures and expected behavior.
- The `spawn` method should generate positions within the grid boundaries defined in `config.py` (GRID_WIDTH, GRID_HEIGHT). However, to keep tests isolated, you may mock config or pass grid dimensions indirectly via occupied positions. Ideally, test that spawn returns valid coordinates within the grid.
- Consider using parameterized tests or multiple test cases to cover various scenarios.
- The test file should be named `test_food.py` and placed in the `snake/tests/` directory.
- Do not modify the Food class implementation; only write tests.

## Referenced code quoting
N/A (the programmer should refer to existing source files and technical specification as needed)
