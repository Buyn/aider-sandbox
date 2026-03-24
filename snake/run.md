# Task:
## Objective
Fix the wall display rendering bug in renderer.py to ensure proper alignment of the border.

## Background
The wall display feature (WALLS_ENABLED, WALL_SYMBOL, WALL_COLOR) has been implemented, but there is an alignment issue: after drawing the top wall, the subsequent rows have an indentation that causes the side walls to be shifted relative to the top/bottom walls. The border should form a continuous rectangle around the playable grid.

## Issues to Address
- Review the `Renderer.render()` method, especially the loop that draws each row of the grid.
- Ensure that when walls are enabled:
  - The top border is a full line of wall symbols of length `grid_width + 2` (including both side corners).
  - For each grid row, the line starts with a wall symbol (colored), then the grid content (snake and food), then ends with a wall symbol (colored). No extra spaces before the left wall.
  - The bottom border (if drawn) matches the top border.
- Verify that wall color is applied correctly to all wall segments and reset after each segment.
- Ensure that when walls are disabled, no border is drawn at all.
- The existing unit tests in `test_renderer.py` should pass after the fix; they define the expected behavior.

## Additional Notes
- The walls are purely visual and do not affect gameplay (snake wraps around).
- The grid coordinates: (0,0) is top-left. Rows are printed from y=0 to y=grid_height-1.
- Be careful with ANSI escape codes: color should wrap only the wall symbols, not the grid content.
- After fixing, run the unit tests to confirm all pass (49 tests, 1 skipped). Also perform manual integration testing to visually verify the border alignment.

## Referenced code quoting
N/A (the programmer should refer to renderer.py and test_renderer.py for implementation details)
