#!/usr/bin/env python3
import sys
from .game import Game

def main():
    game = None
    try:
        game = Game()
        game.run()
    finally:
        if game is not None:
            game.input_handler.cleanup()

if __name__ == "__main__":
    main()
