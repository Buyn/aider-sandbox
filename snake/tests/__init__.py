import sys
import os

# Add the parent directory (snake) to sys.path to allow importing src as a top-level module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
