# Task:
## Objective
Fix the wall display rendering bug in renderer.py.

## Background
The optional wall display feature has been implemented but has a visual alignment issue. According to the review, "The walls are displayed incorrectly. Specifically, after the top wall, on the next line there is an indentation equal to the first wall, causing side walls to be shifted."

## Issues to Address
- The side walls (left and right borders) are not properly aligned with the top and bottom borders.
- The wall rendering should produce a clean rectangular border around the playable grid.
- The bug is purely visual; gameplay mechanics (wrap-around) are unaffected.
- The implementation must support configurable wall symbol (WALL_SYMBOL) and color (WALL_COLOR), and respect WALLS_ENABLED flag.
- The fix must not break any existing unit tests (49 tests, 1 skipped).

## Additional Notes
- The renderer.py file is 1527 bytes and was last modified on 2026-03-24 15:13:02.
- The wall display is optional and purely visual; it does not occupy grid cells or affect snake movement/food spawning.
- The grid size is configurable (GRID_WIDTH, GRID_HEIGHT). The border should be drawn outside the grid cells.
- The current implementation likely has an off-by-one error or incorrect string formatting when drawing the side walls. Pay attention to how the left wall symbol, grid content, and right wall symbol are concatenated per row.
- After fixing, manually test with different wall symbols (e.g., '#', '|', '=') and both WALLS_ENABLED True/False to ensure correct behavior.

## Referenced code quoting
N/A (the programmer should examine renderer.py directly)
