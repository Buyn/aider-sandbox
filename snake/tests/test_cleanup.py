import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the project root (snake) to the Python path to ensure 'src' is importable
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.game import Game
import src.config as config
from src import __main__ as main_module

class TestCleanup(unittest.TestCase):
    @patch('src.__main__.Game')
    def test_entry_point_calls_cleanup_once_on_normal_exit(self, mock_game_cls):
        # Create mock game instance with input_handler.cleanup
        mock_game = MagicMock()
        mock_game.input_handler = MagicMock()
        mock_game_cls.return_value = mock_game
        # Make run return normally (it's an infinite loop, but we'll patch it to return)
        mock_game.run.return_value = None

        # Call main
        main_module.main()

        # Verify cleanup called exactly once
        mock_game.input_handler.cleanup.assert_called_once()

    @patch('src.__main__.Game')
    def test_entry_point_calls_cleanup_on_exception(self, mock_game_cls):
        mock_game = MagicMock()
        mock_game.input_handler = MagicMock()
        mock_game_cls.return_value = mock_game
        mock_game.run.side_effect = KeyboardInterrupt

        with self.assertRaises(KeyboardInterrupt):
            main_module.main()

        mock_game.input_handler.cleanup.assert_called_once()

    @patch('src.game.InputHandler')
    @patch('src.game.Renderer')
    @patch('src.game.Food')
    @patch('src.game.Snake')
    def test_game_run_does_not_call_cleanup(self, mock_input_cls, mock_renderer_cls, mock_food_cls, mock_snake_cls):
        # Setup mock snake
        mock_snake = MagicMock()
        mock_snake.get_head.return_value = (0,0)
        mock_snake.get_body.return_value = []
        mock_snake.direction = config.DIRECTION_RIGHT
        mock_snake_cls.return_value = mock_snake

        # Setup mock food
        mock_food = MagicMock()
        mock_food.get_position.return_value = (5,5)
        mock_food_cls.return_value = mock_food

        # Setup mock renderer
        mock_renderer = MagicMock()
        mock_renderer_cls.return_value = mock_renderer

        # Setup mock input
        mock_input = MagicMock()
        mock_input.get_key.return_value = None
        mock_input_cls.return_value = mock_input

        # Create game instance
        game = Game()
        # The input_handler is already a mock from the patch; its cleanup is a MagicMock

        # Patch time.sleep to raise exception after first call to break loop
        with patch('time.sleep', side_effect=KeyboardInterrupt):
            try:
                game.run()
            except KeyboardInterrupt:
                pass

        # Ensure cleanup was not called from game.run
        game.input_handler.cleanup.assert_not_called()

if __name__ == '__main__':
    unittest.main()
