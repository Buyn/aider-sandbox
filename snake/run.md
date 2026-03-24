# Task: Implement Optional Wall Display Feature

## Objective
Implement the optional wall display feature as specified in the technical specification. This is the final feature needed to complete the project.

## Background
All core game mechanics are implemented and verified:
- Snake movement, growth, wrap-around, self-collision
- Food spawning
- Pause, restart, exit functionality
- Rendering of snake and food with colors
- Input handling
- All unit tests pass (45 tests, 1 skipped)

The wall display is the only remaining feature. It must be:
- Enabled by default
- Configurable (enable/disable, symbol, color)
- Purely visual (walls do not affect game logic - snake still wraps)
- Drawn as a border around the playable grid (outside the grid cells)

## Implementation Requirements

### 1. Configuration (config.py)
Add configuration options for wall display:
- A boolean flag to enable/disable walls (default: enabled)
- A symbol character for walls (default: '#')
- A color ANSI code for walls (default: a distinct color like yellow)

These should be added as module-level constants following the existing pattern.

### 2. Rendering (renderer.py)
Update the `Renderer.render()` method to:
- Check the wall enable flag from config
- When enabled, draw a border around the playable grid:
  - The border should surround the grid cells, i.e., the top row at y=-1, bottom row at y=GRID_HEIGHT, left column at x=-1, right column at x=GRID_WIDTH.
  - Use the configured wall symbol and color for all border cells.
  - Ensure the border is drawn outside the grid cells so that it does not overlap with snake or food.
  - The border should be a full rectangle: top and bottom rows of length (GRID_WIDTH + 2), and left/right walls on each row.
- When disabled, render exactly as before (no border).
- The rendering of snake and food should remain unchanged.
- Remember to reset colors after drawing walls.

### 3. Documentation
- Update the project README (README.md) to describe the new wall display configuration options.
- Explain that walls are purely visual and do not affect gameplay.
- Mention the default values.

## Notes
- The renderer currently clears the screen and prints each cell. You will need to adjust the output to include the border. Consider printing the top border before the grid rows, then for each grid row print left border, grid cells, right border, then bottom border after the loop.
- The wall positions are outside the normal grid coordinate system (negative or beyond max indices). They are only for display.
- Ensure that the wall drawing does not interfere with the existing rendering logic for snake and food.
- The wall color should be distinct from snake and food colors; bright yellow is a good default.
- After implementation, run the full test suite to ensure no regressions. All existing tests should still pass because they do not depend on walls.
- Perform manual testing: toggle WALLS_ENABLED, change symbol and color, verify appearance and that gameplay is unaffected.

## Success Criteria
- All existing unit tests pass
- Manual testing shows walls correctly drawn when enabled, absent when disabled
- No changes to game logic (snake, food, collision, wrap-around)
- Configuration options work as expected
- Documentation updated

## Referenced Files
- snake/technical_specification.md (section 2.1, 3.5 for wall display details)
- snake/config.py (add constants)
- snake/renderer.py (modify render method)
- snake/README.md (update documentation)
