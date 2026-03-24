# Task:
## Objective
Implement the optional wall display feature as specified in the technical specification.

## Background
The snake game currently has no visual border around the playable grid. The specification requires an optional wall display: a border of wall symbols around the grid that is purely visual and does not affect gameplay (snake wraps around). The wall display should be enabled by default and configurable via config.py.

## Requirements
- Add configuration options in `config.py`:
  - `WALLS_ENABLED` (bool, default True)
  - `WALL_SYMBOL` (str, default '#')
  - `WALL_COLOR` (ANSI color code, default appropriate color)
- Update `renderer.py` to draw walls around the grid when `WALLS_ENABLED` is True. The walls should be drawn outside the playable grid cells (i.e., at coordinates -1 and grid_width/grid_height for borders). The walls are purely visual and do not occupy grid cells; they do not affect snake movement, food spawning, or collision detection.
- Ensure that the wall rendering does not interfere with the existing rendering of snake and food.
- The walls should be drawn using the configured symbol and color.
- Add unit tests for wall rendering if needed (e.g., test that walls are drawn when enabled, not drawn when disabled, correct symbol and color). However, if the renderer interface remains unchanged, existing tests may not need updates; but consider adding tests for the new configuration options and rendering behavior.
- Perform integration testing to verify that walls appear correctly and that gameplay is unaffected.

## Additional Notes
- The wall display is optional and should be configurable. The default is enabled.
- The walls are not part of the game grid; they are drawn around it. The snake still wraps at the grid boundaries (0 to width-1, 0 to height-1).
- The renderer currently clears the screen and redraws the entire grid each frame. The wall drawing should be integrated into this process.
- Consider performance: drawing a border of ~50x2 + 48x2 = ~196 characters is negligible.
- Ensure that the wall color and symbol are configurable and that the renderer uses ANSI color codes appropriately.
- The configuration options should be defined in `config.py` with appropriate defaults.
- No changes to game logic (snake movement, collision, food spawning) are required.
- Update documentation (snake/README.md) to describe the wall display feature and configuration options. (This may be a separate task after implementation.)

## Referenced code quoting
Refer to `snake/technical_specification.md` sections 2.1 (Functional Requirements - Optional wall display), 3.3 (Game Loop - no changes needed), 3.5 (Rendering - wall drawing), and 3.7 (Project folder structure).
