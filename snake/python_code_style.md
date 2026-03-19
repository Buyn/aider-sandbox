# python style
## python code style
- keep files short. try to make everything as modular as possible.

## python test style
- use for testing framework "unittest"
- end test file with
  "
  if __name__ == "__main__":
      unittest.main()
  "
- so that all tests in the tests folder can be run with one command "python -m unittest"
