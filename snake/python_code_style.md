# python style
## python code style
- keep files short. try to make everything as modular as possible.
- avoid comments in the code; instead, try to let the names speak for themselves.
- указывая фаил для редактирования указывай полный путь а не только имя (example "wrong - input_handler.py" "Right - snake/src/input_handler.py")




## python test style
- use for testing framework "unittest"
- do not leave behind failed tests; if the test is awaiting implementation, make it as a skip. and make an indication in the notes file, that the tests are skip, mark why and after which the skip needs to be removed.
- end test file with
  "
  if __name__ == "__main__":
      unittest.main()
  "
- so that all tests in the tests folder can be run with one command "python -m unittest"
