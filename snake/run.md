# Task:
## Objective
Fix the wall display rendering bug in `renderer.py` to ensure the visual border is perfectly aligned when `WALLS_ENABLED` is `True`.

## Background
The technical specification requires an optional visual wall border around the playable grid. The current implementation in `renderer.py` produces a misalignment: the side walls on each row appear shifted to the right relative to the top and bottom borders. This is likely due to extra whitespace or incorrect string construction in the row rendering loop.

## Issues to Address
- The top and bottom borders are drawn as a continuous line of wall symbols spanning `grid_width + 2` characters.
- Each grid row should start with a left wall symbol, then `grid_width` cells, then a right wall symbol, with no extra leading or trailing spaces.
- The current code builds each row by concatenating strings for the left wall, each cell, and the right wall. The misalignment suggests there may be an extra space or non-printing character causing the row to be offset.
- Ensure that when `WALLS_ENABLED` is `False`, no walls are drawn and the grid occupies the full terminal area.
- The fix must not break existing unit tests in `test_renderer.py`, which verify the presence of wall symbols at the start and end of each row.

## Additional Notes
- Consult `snake/technical_specification.md` sections 2.1 and 3.5 for the wall display requirements.
- The bug is visual; the unit tests may pass because they only check string patterns, not actual terminal alignment. After fixing, manually run the game (`python -m snake.src`) to verify that the walls form a perfect rectangle.
- Consider that ANSI color codes are non-printing; they should not affect alignment. Ensure that the printable characters (wall symbols and grid cells) are exactly `grid_width + 2` per row, matching the top/bottom border length.
- The `render` method should clear the screen and redraw the entire grid each frame. No changes to other modules are needed.

## Referenced code quoting
(No code quoting needed; refer to `snake/src/renderer.py`.)
