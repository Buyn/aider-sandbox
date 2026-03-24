# Task: Document Wall Display Feature

## Objective
Update README.md to include comprehensive documentation for the optional wall display feature.

## Background
The wall display feature has been implemented in config.py and renderer.py. It allows a visual border around the game grid, with configurable symbol and color. The feature is enabled by default. However, the README.md currently lacks any documentation about this feature.

## Issues to Address
- README.md does not mention the wall display configuration options (WALLS_ENABLED, WALL_SYMBOL, WALL_COLOR).
- Users are not informed about how to enable/disable walls or customize their appearance.
- The technical specification requires that the feature be documented.

## Additional Notes
- The documentation should be placed in a logical section of README.md, perhaps under "Configuration" or "Features".
- Explain that walls are purely visual and do not affect gameplay (snake still wraps).
- List the default values: WALLS_ENABLED=True, WALL_SYMBOL='#', WALL_COLOR='\033[93m' (bright yellow).
- Mention that these can be changed in config.py.
- Keep the documentation concise and clear, following the existing style of README.md.
- No code changes are required; only documentation.

## Referenced code quoting
N/A (documentation only)
