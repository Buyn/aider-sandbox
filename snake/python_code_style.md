# python style
## python code exempls style in .md files
- if you give an example of code not for inserting into .py, always start each line of the example with the ">" symbol or format it as a comment with the "#" symbol.

## python code style
- When specifying the insertion code, always indicate the full name of the file into which this code should be inserted.
- keep files short. try to make everything as modular as possible.
- avoid comments in the code; instead, try to let the names speak for themselves.
- specifying the file to edit, indicating the full path and not just the file name (example "wrong - input_handler.py" "Right - snake/src/input_handler.py")

## python test style
- use for testing framework "unittest"
- do not leave behind failed tests; if the test is awaiting implementation, make it as a skip. and make an indication in the notes file, that the tests are skip, mark why and after which the skip needs to be removed.
- end test file with
  "
  if __name__ == "__main__":
      unittest.main()
  "
- so that all tests in the tests folder can be run with one command "python -m unittest"
