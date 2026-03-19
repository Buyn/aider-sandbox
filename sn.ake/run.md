# Next Action: Implement Configuration Module and Tests

## Objective
Create the `config.py` module within the `src/` directory that defines all configurable parameters as specified in the TECHNICAL_SPECIFICATION.md. Additionally, set up the project structure and write unit tests to verify the configuration.

## Rationale
The configuration module is the foundation for the entire game. All other modules (snake, food, renderer, input_handler, game) will depend on these settings. Implementing it first ensures that subsequent development has a single source of truth for all constants.

## Requirements from Specification
From Section 3.2 Configuration:
- `GRID_WIDTH = 50`
- `GRID_HEIGHT = 50`
- `TICKS_PER_SECOND = 2` (or `MOVE_INTERVAL = 0.5` seconds)
- Colors (ANSI escape codes) for snake body, snake head, food, and background.
- Key mappings: a dictionary mapping keys to directions (e.g., `KEY_UP = 'k'` or `'KEY_UP'` from curses).
- Any other tunable parameters.

Also, from Section 2.1 Functional Requirements:
- Grid size 50x50 cells (configurable) -> `GRID_WIDTH`, `GRID_HEIGHT`.
- Game speed: constant 2 moves per second (configurable) -> `TICKS_PER_SECOND`.
- Visuals: ANSI characters with colors -> color constants.
- Controls: arrow keys, vim keys (h, j, k, l), and ESDF -> key mappings.

## Implementation Plan

### 1. Project Structure
Create the following directories and files:
. Project Structure                                                                       

Create the following directories and files:                                               

                                                                                          
sn.ake/                                                                                   
                                                                                          
├── src/                                                                                  
│   ├── __init__.py                                                                       
│   ├── config.py                                                                         
│   ├── snake.py                                                                          
│   ├── food.py                                                                           
│   ├── renderer.py                                                                       
│   ├── input_handler.py                                                                  
│   └── game.py                                                                           
├── tests/                                                                                
│   ├── __init__.py                                                                       
│   └── test_config.py                                                                    
├── run.md                                                                                
└── progress.md                                                                           
                                                                                          

2. config.py Content                                                                      

Define constants and direction tuples. Since we plan to use curses for input (as          
recommended), we can import curses to access arrow key constants. Example:                

                                                                                          
@@ -1,7 +1,14 @@                                                                          
-# Snake Game Technical Specification                                                     
+# src/config.py                                                                          
                                                                                          
-## 1. Project Overview                                                                   
-A console-based Snake game for Linux using ANSI characters and colors. The game will be  
implemented in Python with a modular architecture.                                        
+# Grid dimensions                                                                        
+GRID_WIDTH = 50                                                                          
+GRID_HEIGHT = 50                                                                         
                                                                                          
-## 2. Requirements                                                                       
+# Game speed: moves per second                                                           
+TICKS_PER_SECOND = 2                                                                     
+# Optional: MOVE_INTERVAL = 1.0 / TICKS_PER_SECOND                                       
                                                                                          
-### 2.1 Functional Requirements                                                          
-- The game area is a grid of 50x50 cells (configurable).                                 
-- The snake moves continuously in the current direction.                                 
-- The snake grows when it eats food.                                                     
-- The snake dies if it collides with itself.                                             
-- The snake wraps around when hitting the grid boundaries (no wall collisions).          
-- Food appears at random locations not occupied by the snake.                            
-- Controls: arrow keys, vim keys (h, j, k, l), and ESDF for direction.                   
-- Pause functionality: space bar toggles pause.                                          
-- After game over, pressing 'r' restarts the game.                                       
-- No scoring system (no points displayed).                                               
+# ANSI color codes (foreground)                                                          
+COLOR_SNAKE_BODY = '\033[32m'   # Green                                                  
+COLOR_SNAKE_HEAD = '\033[92m'   # Bright green                                           
+COLOR_FOOD = '\033[31m'         # Red                                                    
+COLOR_BACKGROUND = '\033[0m'    # Reset/default                                          
                                                                                          
-### 2.2 Non-Functional Requirements                                                      
-- Platform: Linux only.                                                                  
-- Use external libraries for input handling (e.g., `curses`, `readchar`, `keyboard`).    
-- Game speed: constant 2 moves per second (configurable).                                
-- Visuals: ANSI characters with colors:                                                  
-  - Snake body: '█' (full block)                                                         
-  - Snake head: 'O'                                                                      
-  - Food: '●'                                                                            
-  - No borders around the game area.                                                     
-- The game should run in a terminal that supports ANSI colors and cursor control.        
+# Characters                                                                             
+CHAR_SNAKE_BODY = '█'                                                                    
+CHAR_SNAKE_HEAD = 'O'                                                                    
+CHAR_FOOD = '●'                                                                          
                                                                                          
-## 3. Technical Design                                                                   
+# Direction vectors                                                                      
+DIRECTION_UP = (0, -1)                                                                   
+DIRECTION_DOWN = (0, 1)                                                                  
+DIRECTION_LEFT = (-1, 0)                                                                 
+DIRECTION_RIGHT = (1, 0)                                                                 
                                                                                          
-### 3.1 Architecture                                                                     
-The project will be organized into the following modules:                                
+# Key mappings: map key codes to direction vectors.                                      
+# We include both character keys and curses key constants.                               
+import curses                                                                            
                                                                                          
-- `config.py`: Configuration settings (grid size, speed, colors, key mappings, etc.).    
-- `snake.py`: Snake class representing the snake's body, movement, growth, and collision 
detection.                                                                                
-- `food.py`: Food class for spawning and managing food items.                            
-- `renderer.py`: Handles all terminal output, including drawing the snake, food, and     
handling colors.                                                                          
-- `input_handler.py`: Captures keyboard input in a non-blocking manner, supporting the   
required key sets.                                                                        
-- `game.py`: Main game loop, orchestrating the game state, input, rendering, and timing. 
-- and test files                                                                         
-                                                                                         
-### 3.2 Configuration                                                                    
-All configurable parameters will be stored in `config.py` as constants or a configuration
class/object. This includes:                                                              
-- `GRID_WIDTH = 50`                                                                      
-- `GRID_HEIGHT = 50`                                                                     
-- `TICKS_PER_SECOND = 2` (or `MOVE_INTERVAL = 0.5` seconds)                              
-- Colors (ANSI escape codes) for snake body, snake head, food, and background.           
-- Key mappings: a dictionary mapping keys to directions (e.g., `KEY_UP = 'k'` or `'KEY_UP'` 
from curses).                                                                                
-- Any other tunable parameters.                                                             
-                                                                                            
-### 3.3 Game Loop                                                                           
-The main loop will:                                                                         
-1. Process input (non-blocking) and update direction accordingly.                           
-2. If not paused, update snake position based on current direction.                         
-3. Check for collisions (self-collision) and food consumption.                              
-4. If food eaten, grow snake and spawn new food.                                            
-5. Render the current state to the terminal.                                                
-6. Sleep to maintain the configured speed.                                                  
-                                                                                            
-### 3.4 Input Handling                                                                      
-- Use a library like `curses` (standard) or `readchar` (third-party) to capture key presses 
without requiring Enter.                                                                     
-- Support both arrow keys and the specified character keys (h, j, k, l, e, s, d, f).        
-- Map keys to directions: up, down, left, right.                                            
-- Also handle space (pause) and 'r' (restart).                                              
-                                                                                            
-### 3.5 Rendering                                                                           
-- Use ANSI escape codes to clear the screen and position the cursor.                        
-- Draw each cell of the snake and food using the appropriate character and color.           
-- The entire grid is redrawn each frame (or use incremental updates if performance requires,
but for 50x50 it's fine).                                                                    
-- No borders; just the snake and food on a blank background.                                
-                                                                                            
-### 3.6 Game State                                                                          
-- The `Game` class will hold:                                                               
-  - `snake`: instance of `Snake`                                                            
-  - `food`: instance of `Food`                                                              
-  - `direction`: current movement direction                                                 
-  - `paused`: boolean                                                                       
-  - `game_over`: boolean                                                                    
-  - `config`: reference to configuration                                                    
-                                                                                            
-## 4. Dependencies                                                                          
-- Python 3.x                                                                                
-- Linux environment                                                                         
-- Recommended: `curses` (built-in) for input and terminal control.                          
-- Alternatively: `readchar` (pip install readchar) for simpler key reading.                 
-- testig framework                                                                          
-                                                                                            
-## 5. Platform                                                                              
-- Linux only. The code may use terminal-specific features (e.g., `curses` with ncurses) that
are not portable to Windows without adjustments.                                             
-                                                                                            
-## 6. Implementation Steps                                                                  
-1. Set up project structure with `src/` directory and modules.                              
-2. Create `config.py` with all settings.                                                    
-3. Implement `snake.py` with movement, growth, and wrap-around logic.                       
-4. Implement `food.py` with random spawning avoiding snake body.                            
-5. Implement `renderer.py` with ANSI color output.                                          
-6. Implement `input_handler.py` to capture keys.                                            
-7. Implement `game.py` with main loop and state management.                                 
-8. Create a main entry point (e.g., `main.py` or `__main__.py`).                            
-9. Test and refine.                                                                         
-                                                                                            
-## 7. Future Considerations (Optional)                                                      
-- High score tracking.                                                                      
-- Adjustable difficulty (speed increase).                                                   
-- Multiple food types.                                                                      
-- Sound effects (if terminal supports).                                                     
+KEY_MAPPING = {                                                                             
+    # Arrow keys (curses constants)                                                         
+    curses.KEY_UP: DIRECTION_UP,                                                            
+    curses.KEY_DOWN: DIRECTION_DOWN,                                                        
+    curses.KEY_LEFT: DIRECTION_LEFT,                                                        
+    curses.KEY_RIGHT: DIRECTION_RIGHT,                                                      
+    # Vim keys                                                                              
+    'k': DIRECTION_UP,                                                                      
+    'j': DIRECTION_DOWN,                                                                    
+    'h': DIRECTION_LEFT,                                                                    
+    'l': DIRECTION_RIGHT,                                                                   
+    # ESDF keys                                                                             
+    'e': DIRECTION_UP,                                                                      
+    's': DIRECTION_DOWN,                                                                    
+    'd': DIRECTION_RIGHT,                                                                   
+    'f': DIRECTION_LEFT,                                                                    
+}                                                                                           
                                                                                             

3. Tests for config.py                                                                       

Create tests/test_config.py to verify all constants and mappings. Example:                   

                                                                                             
@@ -1,32 +1,32 @@                                                                            
-# Snake Game Technical Specification                                                        
+# tests/test_config.py                                                                      
+import sys                                                                                  
+import os                                                                                   
                                                                                             
-## 1. Project Overview                                                                      
-A console-based Snake game for Linux using ANSI characters and colors. The game will be     
implemented in Python with a modular architecture.                                           
+# Add src directory to path to import config                                                
+sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))   
                                                                                             
-## 2. Requirements                                                                          
+from config import (                                                                        
+    GRID_WIDTH, GRID_HEIGHT, TICKS_PER_SECOND,                                              
+    COLOR_SNAKE_BODY, COLOR_SNAKE_HEAD, COLOR_FOOD, COLOR_BACKGROUND,                       
+    CHAR_SNAKE_BODY, CHAR_SNAKE_HEAD, CHAR_FOOD,                                            
+    DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT,                          
+    KEY_MAPPING                                                                             
+)                                                                                           
+import curses                                                                               
                                                                                             
-### 2.1 Functional Requirements                                                             
-- The game area is a grid of 50x50 cells (configurable).                                    
-- The snake moves continuously in the current direction.                                    
-- The snake grows when it eats food.                                                        
-- The snake dies if it collides with itself.                                                
-- The snake wraps around when hitting the grid boundaries (no wall collisions).             
-- Food appears at random locations not occupied by the snake.                               
-- Controls: arrow keys, vim keys (h, j, k, l), and ESDF for direction.                      
-- Pause functionality: space bar toggles pause.                                             
-- After game over, pressing 'r' restarts the game.                                          
-- No scoring system (no points displayed).                                                  
+def test_grid_dimensions():                                                                 
+    assert GRID_WIDTH == 50                                                                 
+    assert GRID_HEIGHT == 50                                                                
                                                                                             
-### 2.2 Non-Functional Requirements                                                         
-- Platform: Linux only.                                                                     
-- Use external libraries for input handling (e.g., `curses`, `readchar`, `keyboard`).       
-- Game speed: constant 2 moves per second (configurable).                                   
-- Visuals: ANSI characters with colors:                                                     
-  - Snake body: '█' (full block)                                                            
-  - Snake head: 'O'                                                                         
-  - Food: '●'                                                                               
-  - No borders around the game area.                                                        
-- The game should run in a terminal that supports ANSI colors and cursor control.           
+def test_speed():                                                                           
+    assert TICKS_PER_SECOND == 2                                                            
                                                                                             
-## 3. Technical Design                                                                      
+def test_colors():                                                                          
+    assert COLOR_SNAKE_BODY == '\033[32m'                                                   
+    assert COLOR_SNAKE_HEAD == '\033[92m'                                                   
+    assert COLOR_FOOD == '\033[31m'                                                         
+    assert COLOR_BACKGROUND == '\033[0m'                                                    
                                                                                             
-### 3.1 Architecture                                                                        
-The project will be organized into the following modules:                                   
+def test_characters():                                                                      
+    assert CHAR_SNAKE_BODY == '█'                                                           
+    assert CHAR_SNAKE_HEAD == 'O'                                                           
+    assert CHAR_FOOD == '●'                                                                 
                                                                                             
-- `config.py`: Configuration settings (grid size, speed, colors, key mappings, etc.).       
-- `snake.py`: Snake class representing the snake's body, movement, growth, and collision    
detection.                                                                                   
-- `food.py`: Food class for spawning and managing food items.                               
-- `renderer.py`: Handles all terminal output, including drawing the snake, food, and        
handling colors.                                                                             
-- `input_handler.py`: Captures keyboard input in a non-blocking manner, supporting the      
required key sets.                                                                           
-- `game.py`: Main game loop, orchestrating the game state, input, rendering, and timing.    
-- and test files                                                                            
+def test_direction_constants():                                                             
+    assert DIRECTION_UP == (0, -1)                                                          
+    assert DIRECTION_DOWN == (0, 1)                                                         
+    assert DIRECTION_LEFT == (-1, 0)                                                        
+    assert DIRECTION_RIGHT == (1, 0)                                                        
                                                                                             
+def test_key_mapping():                                                                     
+    # Check arrow keys                                                                      
+    assert KEY_MAPPING[curses.KEY_UP] == DIRECTION_UP                                       
+    assert KEY_MAPPING[curses.KEY_DOWN] == DIRECTION_DOWN                                   
+    assert KEY_MAPPING[curses.KEY_LEFT] == DIRECTION_LEFT                                   
+    assert KEY_MAPPING[curses.KEY_RIGHT] == DIRECTION_RIGHT                                 
+    # Check vim keys                                                                        
+    assert KEY_MAPPING['k'] == DIRECTION_UP                                                 
+    assert KEY_MAPPING['j'] == DIRECTION_DOWN                                               
+    assert KEY_MAPPING['h'] == DIRECTION_LEFT                                               
-                                                                                            
-### 3.3 Game Loop                                                                           
-The main loop will:                                                                         
-1. Process input (non-blocking) and update direction accordingly.                           
-2. If not paused, update snake position based on current direction.                         
-3. Check for collisions (self-collision) and food consumption.                              
-4. If food eaten, grow snake and spawn new food.                                            
-5. Render the current state to the terminal.                                                
-6. Sleep to maintain the configured speed.                                                  
-                                                                                            
-### 3.4 Input Handling                                                                      
-- Use a library like `curses` (standard) or `readchar` (third-party) to capture key presses 
without requiring Enter.                                                                     
-- Support both arrow keys and the specified character keys (h, j, k, l, e, s, d, f).        
-- Map keys to directions: up, down, left, right.                                            
-- Also handle space (pause) and 'r' (restart).                                              
-                                                                                            
-### 3.5 Rendering                                                                           
-- Use ANSI escape codes to clear the screen and position the cursor.                        
-- Draw each cell of the snake and food using the appropriate character and color.           
-- The entire grid is redrawn each frame (or use incremental updates if performance requires,
but for 50x50 it's fine).                                                                    
-- No borders; just the snake and food on a blank background.                                
-                                                                                            
-### 3.6 Game State                                                                          
-- The `Game` class will hold:                                                               
-  - `snake`: instance of `Snake`                                                            
-  - `food`: instance of `Food`                                                              
-  - `direction`: current movement direction                                                 
-  - `paused`: boolean                                                                       
-  - `game_over`: boolean                                                                    
-  - `config`: reference to configuration                                                    
-                                                                                            
-## 4. Dependencies                                                                          
-- Python 3.x                                                                                
-- Linux environment                                                                         
-- Recommended: `curses` (built-in) for input and terminal control.                          
-- Alternatively: `readchar` (pip install readchar) for simpler key reading.                 
-- testig framework                                                                          
-                                                                                            
-## 5. Platform                                                                              
-- Linux only. The code may use terminal-specific features (e.g., `curses` with ncurses) that
are not portable to Windows without adjustments.                                             
-                                                                                            
-## 6. Implementation Steps                                                                  
-1. Set up project structure with `src/` directory and modules.                              
-2. Create `config.py` with all settings.                                                    
-3. Implement `snake.py` with movement, growth, and wrap-around logic.                       
-4. Implement `food.py` with random spawning avoiding snake body.                            
-5. Implement `renderer.py` with ANSI color output.                                          
-6. Implement `input_handler.py` to capture keys.                                            
-7. Implement `game.py` with main loop and state management.                                 
-8. Create a main entry point (e.g., `main.py` or `__main__.py`).                            
-9. Test and refine.                                                                         
-                                                                                            
-## 7. Future Considerations (Optional)                                                      
-- High score tracking.                                                                      
-- Adjustable difficulty (speed increase).                                                   
-- Multiple food types.                                                                      
-- Sound effects (if terminal supports).                                                     
+def test_key_mapping():                                                                     
+    # Check arrow keys                                                                      
+    assert KEY_MAPPING[curses.KEY_UP] == DIRECTION_UP                                       
+    assert KEY_MAPPING[curses.KEY_DOWN] == DIRECTION_DOWN                                   
+    assert KEY_MAPPING[curses.KEY_LEFT] == DIRECTION_LEFT                                   
+    assert KEY_MAPPING[curses.KEY_RIGHT] == DIRECTION_RIGHT                                 
+    # Check vim keys                                                                        
+    assert KEY_MAPPING['k'] == DIRECTION_UP                                                 
+    assert KEY_MAPPING['j'] == DIRECTION_DOWN                                               
+    assert KEY_MAPPING['h'] == DIRECTION_LEFT                                               
+    assert KEY_MAPPING['l'] == DIRECTION_RIGHT                                              
+    # Check ESDF keys                                                                       
+    assert KEY_MAPPING['e'] == DIRECTION_UP                                                 
+    assert KEY_MAPPING['s'] == DIRECTION_DOWN                                               
+    assert KEY_MAPPING['d'] == DIRECTION_RIGHT                                              
+    assert KEY_MAPPING['f'] == DIRECTION_LEFT                                               
                                                                                             

4. Running Tests                                                                             

We'll use pytest. Ensure it is installed (pip install pytest). Run tests with:               

                                                                                             
pytest tests/                                                                                
                                                                                             

All tests should pass.                                                                       


Success Criteria                                                                             

 • src/config.py exists and defines all required constants exactly as specified.             
 • tests/test_config.py exists and passes all tests.                                         
 • Project structure matches the spec (src/ with modules, tests/ with test files).           


Additional Notes                                                                             

 • The config module should be importable without side effects (no execution on import).     
 • We use curses constants in KEY_MAPPING. This ties the config to the curses library, but   
   since we plan to use curses for input, that's acceptable. If we later switch to another   
   library, we may need to adjust the mapping in input_handler.py rather than config.        
   However, the spec says key mappings should be in config, so we include them here.         
 • The ANSI color codes are standard; they will work in most Linux terminals.                
 • We'll address path issues in tests by adding the src directory to sys.path. In a more     
   robust setup, we would install the package or use a proper test runner configuration. For 
   now, this is sufficient.                                                                  


Next After This                                                                              

Once config is implemented and tested, proceed to implement the Snake class in snake.py with 
movement, growth, wrap-around, and collision detection, along with its unit tests.           

                                                                            
