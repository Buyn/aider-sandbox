# Next Action: Implement Snake Class and Tests

## Objective
Implement the `Snake` class in `src/snake.py` with the following functionality:
- The snake has a body represented as a list of (x, y) coordinates, with the head at index 0.
- The snake moves in a current direction (one of the direction vectors from config).
- When moving, the snake adds a new head in the current direction and (unless growing) removes the tail.
- The snake wraps around the grid boundaries (using modulo arithmetic with GRID_WIDTH and GRID_HEIGHT from config).
- The snake can grow by one segment when `move(grow=True)` is called (used when food is eaten).
- The snake detects self-collision: if the new head position is in the current body (considering whether the tail will be removed or not), then it's a collision.

Additionally, write unit tests in `tests/test_snake.py` to verify:
- Initialization: default snake has length 3, centered horizontally, moving right.
- Movement without growth: the snake moves one step, the tail is removed, the head is at the new position.
- Movement with growth: the snake moves and the tail is not removed, so length increases by one.
- Wrap-around: when the head moves beyond the grid, it appears on the opposite side.
- Self-collision: moving into the body (excluding the tail if not growing) returns False (collision).

## Implementation Plan

### 1. Snake Class (`src/snake.py`)
- Import necessary constants from `config`: `GRID_WIDTH`, `GRID_HEIGHT`, `DIRECTION_UP`, `DIRECTION_DOWN`, `DIRECTION_LEFT`, `DIRECTION_RIGHT`.
- Define the `Snake` class.
- `__init__(self, body=None, direction=None)`: if body is not provided, create a default body of length 3 centered in the grid (using `GRID_WIDTH` and `GRID_HEIGHT`). The default direction is `DIRECTION_RIGHT`.
- `move(self, grow=False)`: 
  1. Compute new head: `new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])`
  2. Apply wrap-around: `new_head = (new_head[0] % GRID_WIDTH, new_head[1] % GRID_HEIGHT)`
  3. Check for self-collision:
     - If `grow` is True, check if `new_head` is in `self.body` (the entire current body).
     - If `grow` is False, check if `new_head` is in `self.body[:-1]` (all except the tail).
     - If collision, return `False` (do not update the body).
  4. Insert `new_head` at the beginning of `self.body`.
  5. If not `grow`, remove the last element (tail).
  6. Return `True` (move successful).
- `set_direction(self, direction)`: set the current direction.
- `get_head(self)`: return the head position.
- `get_body(self)`: return the entire body (list of coordinates).
- `get_length(self)`: return the length of the snake.

### 2. Tests (`tests/test_snake.py`)
- Set up the test environment by adding the `src` directory to `sys.path` (similar to `test_config.py`).
- Import `Snake` from `snake` and the necessary constants from `config`.
- Write test functions:
  - `test_initialization()`: check that a default snake has length 3, head at the center right? Actually, the default body should be: [(center_x, center_y), (center_x-1, center_y), (center_x-2, center_y)] and direction is `DIRECTION_RIGHT`.
  - `test_move_without_growth()`: create a snake, call `move(grow=False)`, and check that the head moved one step in the direction, the tail was removed, and the length is unchanged.
  - `test_move_with_growth()`: create a snake, call `move(grow=True)`, and check that the head moved and the length increased by one.
  - `test_wrap_around()`: create a snake at the edge (e.g., head at (0, y) moving left) and check that after moving, the head appears at the opposite edge (GRID_WIDTH-1, y).
  - `test_self_collision()`: create a snake with a body that will collide when moving (e.g., a snake of length 3 moving down into its own neck). Check that `move` returns `False`.

### 3. Running Tests
Use pytest to run the tests: `pytest tests/test_snake.py`

## Success Criteria
- `src/snake.py` exists and implements the `Snake` class as described.
- `tests/test_snake.py` exists and all tests pass.
- The snake class correctly handles movement, growth, wrap-around, and self-collision.

## Additional Notes
- The snake class should not depend on any other modules (except config for constants).
- The move method should not modify the body if a collision occurs (return False and leave body unchanged).
- The wrap-around uses modulo arithmetic. Ensure that negative coordinates are handled correctly (Python's modulo works as expected: -1 % 50 = 49).
- In tests, we can create snakes with specific bodies and directions to test edge cases.
