import sys
import os
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from input_handler import InputHandler
from config import KEY_MAPPING, ACTION_PAUSE, ACTION_RESTART
import curses

class TestInputHandler(unittest.TestCase):
    @patch('snake.src.input_handler.curses.initscr')
    @patch('snake.src.input_handler.curses.endwin')
    @patch('snake.src.input_handler.curses.noecho')
    @patch('snake.src.input_handler.curses.cbreak')
    def test_input_handler_instantiation(self, mock_cbreak, mock_noecho, mock_endwin, mock_initscr):
        mock_stdscr = MagicMock()
        mock_initscr.return_value = mock_stdscr
        handler = InputHandler()
        self.assertIsNotNone(handler)
        mock_initscr.assert_called_once()
        mock_noecho.assert_called_once()
        mock_cbreak.assert_called_once()
        mock_stdscr.keypad.assert_called_once_with(True)
        mock_stdscr.nodelay.assert_called_once_with(True)

    @patch('snake.src.input_handler.curses.initscr')
    @patch('snake.src.input_handler.curses.endwin')
    @patch('snake.src.input_handler.curses.noecho')
    @patch('snake.src.input_handler.curses.cbreak')
    def test_get_key_with_mapped_key(self, mock_cbreak, mock_noecho, mock_endwin, mock_initscr):
        mock_stdscr = MagicMock()
        mock_initscr.return_value = mock_stdscr
        handler = InputHandler()
        # Test with a character key: 'k' -> DIRECTION_UP
        mock_stdscr.getch.return_value = ord('k')
        result = handler.get_key()
        self.assertEqual(result, (0, -1))
        # Test with a curses constant: curses.KEY_UP
        mock_stdscr.getch.return_value = curses.KEY_UP
        result = handler.get_key()
        self.assertEqual(result, (0, -1))

    @patch('snake.src.input_handler.curses.initscr')
    @patch('snake.src.input_handler.curses.endwin')
    @patch('snake.src.input_handler.curses.noecho')
    @patch('snake.src.input_handler.curses.cbreak')
    def test_get_key_special_actions(self, mock_cbreak, mock_noecho, mock_endwin, mock_initscr):
        mock_stdscr = MagicMock()
        mock_initscr.return_value = mock_stdscr
        handler = InputHandler()
        # Test space (pause)
        mock_stdscr.getch.return_value = ord(' ')
        result = handler.get_key()
        self.assertEqual(result, ACTION_PAUSE)
        # Test 'r' (restart)
        mock_stdscr.getch.return_value = ord('r')
        result = handler.get_key()
        self.assertEqual(result, ACTION_RESTART)

    @patch('snake.src.input_handler.curses.initscr')
    @patch('snake.src.input_handler.curses.endwin')
    @patch('snake.src.input_handler.curses.noecho')
    @patch('snake.src.input_handler.curses.cbreak')
    def test_get_key_with_unmapped_key(self, mock_cbreak, mock_noecho, mock_endwin, mock_initscr):
        mock_stdscr = MagicMock()
        mock_initscr.return_value = mock_stdscr
        handler = InputHandler()
        mock_stdscr.getch.return_value = ord('x')  # not in mapping
        result = handler.get_key()
        self.assertIsNone(result)
        # Also test with an integer not in mapping
        mock_stdscr.getch.return_value = 999
        result = handler.get_key()
        self.assertIsNone(result)

    @patch('snake.src.input_handler.curses.initscr')
    @patch('snake.src.input_handler.curses.endwin')
    @patch('snake.src.input_handler.curses.noecho')
    @patch('snake.src.input_handler.curses.cbreak')
    def test_get_key_no_key(self, mock_cbreak, mock_noecho, mock_endwin, mock_initscr):
        mock_stdscr = MagicMock()
        mock_initscr.return_value = mock_stdscr
        handler = InputHandler()
        mock_stdscr.getch.return_value = -1
        result = handler.get_key()
        self.assertIsNone(result)

    @patch('snake.src.input_handler.curses.initscr')
    @patch('snake.src.input_handler.curses.endwin')
    @patch('snake.src.input_handler.curses.noecho')
    @patch('snake.src.input_handler.curses.cbreak')
    def test_cleanup(self, mock_cbreak, mock_noecho, mock_endwin, mock_initscr):
        mock_stdscr = MagicMock()
        mock_initscr.return_value = mock_stdscr
        handler = InputHandler()
        handler.cleanup()
        mock_endwin.assert_called_once()

if __name__ == "__main__":
    unittest.main()
