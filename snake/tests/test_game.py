import unittest
import sys
import os
# Add the project root (snake) to the Python path to ensure 'src' is importable
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from ..src.game import Game
from .. import config as real_config
from unittest.mock import patch, MagicMock

class TestGame(unittest.TestCase):
    def setUp(self):
        # Patch the classes in src.game
        self.patcher_snake = patch('src.game.Snake')
        self.patcher_food = patch('src.game.Food')
        self.patcher_renderer = patch('src.game.Renderer')
        self.patcher_input = patch('src.game.InputHandler')
        self.mock_snake_cls = self.patcher_snake.start()
        self.mock_food_cls = self.patcher_food.start()
        self.mock_renderer_cls = self.patcher_renderer.start()
        self.mock_input_cls = self.patcher_input.start()
        # Create mock instances
        self.mock_snake = MagicMock()
        self.mock_food = MagicMock()
        self.mock_renderer = MagicMock()
        self.mock_input = MagicMock()
        self.mock_snake_cls.return_value = self.mock_snake
        self.mock_food_cls.return_value = self.mock_food
        self.mock_renderer_cls.return_value = self.mock_renderer
        self.mock_input_cls.return_value = self.mock_input
        # Default mock behaviors
        self.mock_snake.get_body.return_value = []
        self.mock_snake.get_head.return_value = (0,0)
        self.mock_food.get_position.return_value = (5,5)
        # Ensure snake has a direction attribute for _key_to_direction
        self.mock_snake.direction = real_config.DIRECTION_RIGHT

    def tearDown(self):
        self.patcher_snake.stop()
        self.patcher_food.stop()
        self.patcher_renderer.stop()
        self.patcher_input.stop()

    def test_init(self):
        game = Game()
        self.mock_snake_cls.assert_called_once()
        self.mock_food_cls.assert_called_once()
        self.mock_renderer_cls.assert_called_once()
        self.mock_input_cls.assert_called_once()
        self.assertFalse(game.paused)
        self.assertFalse(game.game_over)
        self.mock_food.spawn.assert_called_once_with(self.mock_snake.get_body.return_value)

    def test_handle_key_pause(self):
        game = Game()
        game._handle_key(ord(' '))
        self.assertTrue(game.paused)
        game._handle_key(ord(' '))
        self.assertFalse(game.paused)

    def test_handle_key_restart_when_game_over(self):
        game = Game()
        game.game_over = True
        game._handle_key(ord('r'))
        self.assertFalse(game.game_over)
        self.assertFalse(game.paused)
        self.assertEqual(self.mock_snake_cls.call_count, 2)
        self.assertEqual(self.mock_food_cls.call_count, 2)
        self.assertEqual(self.mock_renderer_cls.call_count, 1)  # not recreated
        self.assertEqual(self.mock_input_cls.call_count, 1)    # not recreated
        self.assertEqual(self.mock_food.spawn.call_count, 2)

    def test_handle_key_direction_when_normal(self):
        game = Game()
        game._handle_key(ord('k'))  # 'k' should map to UP
        self.mock_snake.set_direction.assert_called_once_with(real_config.DIRECTION_UP)

    def test_handle_key_direction_when_paused(self):
        game = Game()
        game.paused = True
        game._handle_key(ord('k'))
        self.mock_snake.set_direction.assert_not_called()

    def test_handle_key_direction_when_game_over(self):
        game = Game()
        game.game_over = True
        game._handle_key(ord('k'))
        self.mock_snake.set_direction.assert_not_called()

    def test_handle_key_restart_when_not_game_over(self):
        game = Game()
        game._handle_key(ord('r'))
        self.mock_snake.set_direction.assert_not_called()
        self.assertEqual(self.mock_snake_cls.call_count, 1)  # only init
        self.assertFalse(game.game_over)
        self.assertFalse(game.paused)

    def test_update_game_when_paused(self):
        game = Game()
        game.paused = True
        game._update_game()
        self.mock_snake.move.assert_not_called()
        self.mock_renderer.render.assert_not_called()  # _update_game doesn't call render

    def test_update_game_when_not_paused_and_not_over(self):
        game = Game()
        game.paused = False
        game.game_over = False
        # No food eaten
        self.mock_snake.get_head.return_value = (0,0)
        self.mock_snake.get_body.return_value = []
        self.mock_food.get_position.return_value = (5,5)
        game._update_game()
        self.mock_snake.move.assert_called_once_with(grow=False)
        # renderer.render is called in run loop, not in _update_game, so not asserted here
        self.mock_food.spawn.assert_not_called()
        self.assertFalse(game.game_over)

    def test_update_game_food_eaten(self):
        game = Game()
        game.paused = False
        game.game_over = False
        # Set up so that next head will be on food
        self.mock_snake.direction = real_config.DIRECTION_RIGHT
        self.mock_snake.get_head.return_value = (2,3)
        self.mock_snake.get_body.return_value = [(1,3)]
        self.mock_food.get_position.return_value = (3,3)
        game._update_game()
        self.mock_snake.move.assert_called_once_with(grow=True)
        # renderer.render not called here
        self.mock_food.spawn.assert_called_once_with(self.mock_snake.get_body.return_value)
        self.assertFalse(game.game_over)

    def test_update_game_self_collision(self):
        game = Game()
        game.paused = False
        game.game_over = False
        self.mock_snake.get_head.return_value = (1,1)
        # Simulate collision: body includes head position in a later segment
        self.mock_snake.get_body.return_value = [(1,1), (1,1)]  # head and body segment at same position
        self.mock_food.get_position.return_value = (5,5)  # not eaten
        game._update_game()
        self.mock_snake.move.assert_called_once_with(grow=False)
        self.assertTrue(game.game_over)
        self.mock_food.spawn.assert_not_called()

    def test_update_game_when_game_over(self):
        game = Game()
        game.game_over = True
        game._update_game()
        self.mock_snake.move.assert_not_called()
        self.mock_renderer.render.assert_not_called()

    def test_restart(self):
        game = Game()
        # After init, call counts are 1
        self.assertEqual(self.mock_snake_cls.call_count, 1)
        self.assertEqual(self.mock_food_cls.call_count, 1)
        self.assertEqual(self.mock_renderer_cls.call_count, 1)
        self.assertEqual(self.mock_input_cls.call_count, 1)
        self.assertEqual(self.mock_food.spawn.call_count, 1)
        # Call restart
        game.restart()
        self.assertFalse(game.paused)
        self.assertFalse(game.game_over)
        self.assertEqual(self.mock_snake_cls.call_count, 2)
        self.assertEqual(self.mock_food_cls.call_count, 2)
        self.assertEqual(self.mock_renderer_cls.call_count, 1)  # not recreated
        self.assertEqual(self.mock_input_cls.call_count, 1)    # not recreated
        self.assertEqual(self.mock_food.spawn.call_count, 2)

if __name__ == '__main__':
    unittest.main()
