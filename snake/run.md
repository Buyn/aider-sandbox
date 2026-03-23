# Task: Implement Optional Wall Display Feature

## Objective
Implement the optional wall display feature as specified in the technical specification. This feature adds a visual border around the playable grid using configurable symbols and colors. The walls are purely cosmetic and do not affect gameplay.

## Background
The project is nearly complete. All core functionality is implemented and tested. The only remaining feature from the specification is the optional wall display. The technical specification (section 2.1 and 3.5) describes this feature.

## Requirements
1. **Configuration** (in `config.py`):
   - Add `WALLS_ENABLED` (boolean, default `True`)
   - Add `WALL_SYMBOL` (string, default `'#'`)
   - Add `WALL_COLOR` (ANSI color code, should match the style of other color constants)

2. **Rendering** (in `renderer.py`):
   - Modify the `render` method to accept the new wall configuration (via `config` or parameters)
   - When `WALLS_ENABLED` is `True`, draw a border around the grid:
     - The border should be drawn *outside* the playable grid cells (coordinates from 0 to GRID_WIDTH-1 and 0 to GRID_HEIGHT-1)
     - Top border: y = -1, x from -1 to GRID_WIDTH (inclusive)
     - Bottom border: y = GRID_HEIGHT, x from -1 to GRID_WIDTH (inclusive)
     - Left border: x = -1, y from 0 to GRID_HEIGHT-1 (inclusive)
     - Right border: x = GRID_WIDTH, y from 0 to GRID_HEIGHT-1 (inclusive)
     - Use `WALL_SYMBOL` and `WALL_COLOR` for all border cells
   - Ensure the border does not interfere with the rendering of snake, food, or the grid itself
   - The border should be drawn before or after the grid? It doesn't matter as long as it's visible. Typically draw border first so grid content appears on top.

3. **Game Logic**:
   - No changes to game logic are required. The walls are visual only.
   - Ensure that snake movement, food spawning, collision detection continue to use the grid coordinates (0..GRID_WIDTH-1, 0..GRID_HEIGHT-1) without considering walls.

4. **Testing**:
   - Existing unit tests should continue to pass (they don't test renderer output directly, but ensure no regression)
   - Consider adding unit tests for renderer to verify wall drawing when enabled/disabled. However, this is optional if manual testing confirms correct behavior.
   - Perform manual integration testing: run the game with walls enabled and disabled, verify the border appears correctly and does not affect gameplay.

5. **Documentation**:
   - Update `README.md` to describe the new wall display feature and configuration options.
   - Ensure `config.py` has clear comments for the new constants.

## Implementation Notes
- The renderer currently receives `grid_width` and `grid_height` as parameters. It also has access to `config` module. Use whichever is convenient.
- The border coordinates are outside the normal grid. When printing, you'll need to position the cursor accordingly. The renderer already clears the screen and iterates over grid cells. You'll need to add additional loops or conditions to draw the border.
- Be careful with ANSI color codes: apply `WALL_COLOR` to wall symbols and reset after.
- The border should be drawn even if the snake or food is at the edge? No, because the border is outside the grid. The grid cells themselves are unaffected.
- The border is a simple rectangle. You can draw it by:
  - First drawing the top and bottom rows (including corners)
  - Then drawing the left and right columns (excluding corners already drawn)
- Alternatively, you can extend the rendering loop to cover a slightly larger area (from -1 to GRID_HEIGHT in y, and -1 to GRID_WIDTH in x) and conditionally draw walls at the border coordinates.

## Verification
After implementation:
1. Run `python -m unittest` from the `snake` directory. All tests should pass.
2. Run the game with `python -m snake.src`. Verify:
   - With default config (walls enabled), a border of `#` symbols appears around the grid.
   - The border color matches `config.WALL_COLOR`.
   - The snake and food appear inside the border.
   - The snake can wrap from one edge to the opposite without any visual glitch.
   - Pause, restart, and game over work correctly.
3. Disable walls by setting `WALLS_ENABLED = False` in `config.py` and verify the border disappears.
4. Change `WALL_SYMBOL` and `WALL_COLOR` and verify changes take effect.

## Deliverables
- Modified `config.py` with new constants.
- Modified `renderer.py` with wall drawing logic.
- (Optional) New or updated tests for renderer.
- Updated `README.md` with feature description.
- Updated `progress.md` and `review_and_comments.md` as appropriate (the programmer should not edit these; the reviewer will update them after verification).

## Notes
- Keep the changes minimal and focused. Do not refactor unrelated code.
- Ensure backward compatibility: the default should be walls enabled, matching the specification.
- The feature is optional and configurable; the game should work correctly with or without walls.
