# Task: Fix Wall Display Rendering Bug

## Objective
Fix the wall display rendering issue where side walls are incorrectly indented after the top wall line.

## Background
The optional wall display feature has been implemented but has a visual bug: after drawing the top border, subsequent lines (including side walls) have an unwanted indentation. The walls should form a proper rectangular border around the playable grid.

## Issues to Address
- The renderer currently produces output like:
  ```
  ##############
   #          #
   #          #
   ##############
  ```
  But it should produce:
  ```
  ##############
  #            #
  #            #
  ##############
  ```
- The side walls should align exactly with the top and bottom walls, without leading spaces.

## Technical Context
- The wall display is controlled by `config.WALLS_ENABLED` (default: True)
- Wall symbol: `config.WALL_SYMBOL` (default: '#')
- Wall color: `config.WALL_COLOR` (ANSI escape code)
- Walls are drawn *outside* the grid cells (visual only, no gameplay effect)
- The renderer's `render()` method receives `grid_width` and `grid_height` parameters
- When walls are enabled, the total output width should be `grid_width + 2` characters (including left and right walls)
- Each line should start with the wall symbol (if walls enabled) and end with the wall symbol (if walls enabled), with exactly `grid_width` characters in between for the interior rows

## Expected Behavior
1. If `WALLS_ENABLED` is True:
   - Top border: wall symbol repeated `grid_width + 2` times
   - For each grid row y (0 to grid_height-1):
     - Print: wall symbol + interior (grid_width characters) + wall symbol
   - Bottom border: same as top border
2. If `WALLS_ENABLED` is False:
   - Only the grid content is printed (no borders)

## Additional Notes
- The bug likely involves incorrect handling of newlines or cursor positioning when drawing the side walls.
- Check the render loop logic: after printing the top border, ensure that subsequent rows start at column 0 (no indentation) before drawing the left wall.
- The existing unit tests in `test_renderer.py` should capture this behavior; verify they pass after the fix.
- Ensure ANSI color codes are applied correctly to walls.
- After fixing, run all unit tests (`python -m unittest`) to ensure no regressions.

## Referenced code quoting
The relevant code is in `snake/src/renderer.py`, specifically the `render()` method's wall-drawing logic.

## Implementation Guidance
- Review the current implementation's loop structure and print statements.
- Ensure that for interior rows, you explicitly print the left wall symbol at the start of the line (with color), then the grid content, then the right wall symbol (with color), then a newline.
- Avoid any extra spaces or indentation before the left wall.
- The top and bottom borders should be printed as full lines without any preceding spaces.
- Consider using string concatenation or formatting to build each line cleanly.
- The tests in `test_renderer.py` (especially `test_render_with_walls_enabled` and `test_wall_color_and_symbol_used`) will verify correct output; use them as a specification.

## Success Criteria
- All unit tests pass (49 tests, 1 skipped).
- Manual testing shows a properly aligned rectangular border when `WALLS_ENABLED` is True.
- No visual artifacts (extra spaces, misalignment) in the wall display.
- The wall display respects configuration options (symbol, color, enabled/disabled).
