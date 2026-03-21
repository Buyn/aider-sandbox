from . import config
import curses

class InputHandler:
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        self.stdscr.nodelay(True)  # Make getch non-blocking

    def get_key(self):
        key = self.stdscr.getch()
        if key == -1:
            return None
        return key

    def cleanup(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
