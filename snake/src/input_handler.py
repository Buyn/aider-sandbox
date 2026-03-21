import curses
from .config import KEY_MAPPING

class InputHandler:
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        self.stdscr.nodelay(True)

    def get_key(self):
        ch = self.stdscr.getch()
        if ch == -1:
            return None
        # Check if the key code is directly in the mapping (for special keys like curses.KEY_UP)
        if ch in KEY_MAPPING:
            return KEY_MAPPING[ch]
        # If it's a character key (ASCII), convert to character and look up
        if 0 <= ch < 256:
            key_char = chr(ch)
            if key_char in KEY_MAPPING:
                return KEY_MAPPING[key_char]
        return None

    def cleanup(self):
        curses.endwin()
