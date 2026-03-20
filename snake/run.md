# Next Action: Fix Unit Tests for Input Handler

## Objective
Fix the failing unit tests in `tests/test_input_handler.py` by correcting the mock patch targets. The tests currently fail with `_curses.error: must call initscr() first` because the patches are applied to the wrong module. The `InputHandler` class uses the `curses` module imported at the top of `src/input_handler.py`, so the tests must patch `curses` functions in that module's namespace.

## Problem Description
The test methods use decorators like:

## Implementation Plan                                                                       
                                                                                             
                                                                                             
                                                                                             
### 1. Update test patch targets                                                             
                                                                                             
In `tests/test_input_handler.py`, change all patch decorators from:                          
                                                                                             

@patch('curses.initscr')                                                                     

@patch('curses.endwin')                                                                      

@patch('curses.noecho')                                                                      

@patch('curses.cbreak')                                                                      

                                                                                             
to:                                                                                          
                                                                                             

@patch('snake.src.input_handler.curses.initscr')                                             

@patch('snake.src.input_handler.curses.endwin')                                              

@patch('snake.src.input_handler.curses.noecho')                                              

@patch('snake.src.input_handler.curses.cbreak')                                              

                                                                                             
                                                                                             
                                                                                             
Ensure this change is applied to all test methods that use these patches (all tests in       
`TestInputHandler`).                                                                         
                                                                                             
                                                                                             
                                                                                             
### 2. Run tests                                                                             
                                                                                             
Execute the test suite: `python -m unittest` or `python -m unittest                          
tests.test_input_handler`.                                                                   
                                                                                             
Verify that all 5 previously failing tests now pass, and no new failures are introduced.     
                                                                                             
                                                                                             
                                                                                             
### 3. Confirm full test suite passes                                                        
                                                                                             
Run all tests: `python -m unittest` from the project root.                                   
                                                                                             
All tests should pass.                                                                       
                                                                                             
                                                                                             
                                                                                             
## Success Criteria                                                                          
                                                                                             
- All tests in `tests/test_input_handler.py` pass.                                           
                                                                                             
- The overall test suite has no failures.                                                    
                                                                                             
                                                                                             
                                                                                             
## Notes                                                                                     
                                                                                             
- The `InputHandler` implementation is already correct; only the test mocking needs          
adjustment.                                                                                  
                                                                                             
- After fixing these tests, the project will have a green test suite, allowing safe          
implementation of `game.py`.                                                                 
                                                                                             

