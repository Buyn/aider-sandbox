# Next Action: Implement Renderer Module and Tests

## Objective
Implement the `Renderer` class in `src/renderer.py` with the following functionality:
- The renderer is responsible for drawing the game state to the terminal using ANSI escape codes.
- It should have a method `render(snake, food, grid_width, grid_height)` that clears the screen and draws:
  - The snake: each segment of the snake body (including head) as a colored block character.
  - The food: as a colored dot character.
- The snake body should be drawn with one color (e.g., green) and the head with a different color (e.g., light green).
- The food should be drawn with a distinct color (e.g., red).
- The renderer should use the grid dimensions to position each cell.
- The renderer should not draw any borders; just the snake and food on a blank background.
- The renderer should handle the terminal cursor positioning and screen clearing.

Additionally, write unit tests in `tests/test_renderer.py` to verify:
- The renderer can be instantiated.
- The `render` method calls the necessary terminal output functions (we can mock `sys.stdout` to capture the output).
- The output contains the correct ANSI codes for colors and cursor positioning.
- The snake and food are drawn at the correct positions with the correct characters and colors.

## Implementation Plan

### 1. Renderer Class (`src/renderer.py`)
- Import necessary constants from `config` for colors and characters: `GRID_WIDTH`, `GRID_HEIGHT`, `COLOR_SNAKE_BODY`, `COLOR_SNAKE_HEAD`, `COLOR_FOOD`, `CHAR_SNAKE_BODY`, `CHAR_SNAKE_HEAD`, `CHAR_FOOD`.
- Define the `Renderer` class.
- `render(self, snake, food, grid_width, grid_height)`:
  1. Clear the screen and move cursor to home: `print("\033[2J\033[H", end='')`.
  2. For each y in range(grid_height):
     - For each x in range(grid_width):
       - If (x,y) == snake.get_head(): output `COLOR_SNAKE_HEAD + CHAR_SNAKE_HEAD + "\033[0m"`.
       - Else if (x,y) in snake.get_body(): output `COLOR_SNAKE_BODY + CHAR_SNAKE_BODY + "\033[0m"`.
       - Else if (x,y) == food.get_position(): output `COLOR_FOOD + CHAR_FOOD + "\033[0m"`.
       - Else: output a space.
     - After each row, output a newline.
  3. Ensure the output is flushed (print with flush=True or sys.stdout.flush()).

### 2. Tests (`tests/test_renderer.py`)
- Set up the test environment by adding the `src` directory to `sys.path`.
- Import `Renderer` from `renderer`, `Snake` from `snake`, `Food` from `food`, and the necessary constants from `config`.
- Write test functions:
  - `test_render_instantiation()`: check that `Renderer()` creates an instance.
  - `test_render_output()`: 
    - Create a snake with a known body (e.g., `body=[(0,0), (1,0)]` and head at (0,0)).
    - Create a food at a known position (e.g., `(1,1)`).
    - Call `renderer.render(snake, food, 2, 2)` and capture stdout.
    - Build the expected string: clear screen code, then for each cell in a 2x2 grid, the appropriate ANSI codes and characters.
    - Assert that the captured output equals the expected string.
  - Additional tests for edge cases (e.g., snake of length 1, food at same position as snake head? but that shouldn't happen in the game, but the renderer should draw the head on top of food? Actually, if the food is at the same position as the head, we draw the head because we check head first. So we can test that.
- Run the tests with `pytest tests/test_renderer.py`.

### 3. Running Tests
Use pytest to run the tests: `pytest tests/test_renderer.py`

## Success Criteria
- `src/renderer.py` exists and implements the `Renderer` class as described.
- `tests/test_renderer.py` exists and all tests pass.
- The renderer correctly draws the snake (head and body with different colors) and food on a grid of the given size, with no borders.

## Notes
- The config module must provide the required constants. If any are missing, they must be added to `config.py` and tested in `test_config.py`. However, since `config.py` is already implemented and tested, we assume they are present. If not, we will need to update `config.py` and `test_config.py` accordingly.
- The renderer should not modify the snake or food objects; it only reads their state.
- The clear screen and cursor home ANSI codes are `\033[2J\033[H`.
- Remember to reset the color after each cell with `\033[0m` to avoid color bleeding.
