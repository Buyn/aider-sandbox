# Task:
## Objective
Implement the optional wall display feature as specified in snake/technical_specification.md section 2.1 and 3.5.

## Background
All core gameplay features are implemented and all unit tests pass (45 tests, 1 skipped). The project is ready for the final feature: visual walls around the playable grid.

## Requirements
- Add configuration options in `config.py`:
  - `WALLS_ENABLED` (default: True)
  - `WALL_SYMBOL` (default: '#')
  - `WALL_COLOR` (ANSI color code, default to be determined)
- Update `renderer.py` to draw a border of wall symbols around the playable grid when `WALLS_ENABLED` is True.
- Walls must be purely visual and must NOT affect game logic (snake movement, food spawning, collision detection all remain unchanged).
- The walls should be drawn *outside* the playable grid cells (i.e., surrounding the grid, not occupying grid cells).
- Ensure all existing unit tests continue to pass after changes.
- Consider whether any new unit tests are needed for wall rendering (optional but recommended if renderer interface changes significantly).
- Update `snake/README.md` to document the new wall display configuration options.

## Implementation Notes
- The renderer currently receives `grid_width` and `grid_height` and iterates over grid cells. The wall border should be drawn around these cells, so the total display area will be slightly larger (grid_width+2 by grid_height+2 characters).
- Use ANSI color codes for walls consistent with the existing color scheme in config.py.
- The wall display is enabled by default per specification.
- Do not modify snake.py, food.py, input_handler.py, or game.py for this feature; only config.py and renderer.py (and documentation).
- After implementation, perform manual integration testing to verify:
  - Walls appear correctly when enabled
  - Walls do not interfere with gameplay
  - Walls can be disabled via configuration
  - Colors and symbol are configurable

## Additional Notes
- The programmer should refer to snake/technical_specification.md for full details on visuals and ANSI color usage.
- The programmer should also check snake/progress.md for the current project status and completion criteria.
- Keep changes minimal and focused; avoid touching unrelated code.
