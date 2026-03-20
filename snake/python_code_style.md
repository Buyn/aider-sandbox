# python style
## python code style
- keep files short. try to make everything as modular as possible.

## python test style
- use for testing framework "unittest"
- do not leave behind failed tests; if the test is awaiting implementation, make it as a skip. and make an indication in the notes file, that the tests are skip, mark why and after which the skip needs to be removed.
- end test file with
  "
  if __name__ == "__main__":
      unittest.main()
  "
- so that all tests in the tests folder can be run with one command "python -m unittest"
