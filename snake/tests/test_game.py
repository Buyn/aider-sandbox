import unittest
from unittest.mock import patch, MagicMock
from snake.src.game import Game
from snake.src import config
from snake.src import snake
from snake.src import food
class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initialization(self):
        self.assertIsInstance(self.game.snake, snake.Snake)
        self.assertIsInstance(self.game.food, food.Food)
        self.assertIsInstance(self.game.renderer, renderer.Renderer)
        self.assertIsInstance(self.game.input_handler, input_handler.InputHandler)
        self.assertFalse(self.game.paused)
        self.assertFalse(self.game.game_over)
        self.assertEqual(self.game.direction, self.game.snake.direction)

    def test_restart(self):
        # Change state
        self.game.paused = True
        self.game.game_over = True
        # Modify snake and food to ensure restart resets them
        old_snake = self.game.snake
        old_food = self.game.food
        self.game.restart()
        self.assertFalse(self.game.paused)
        self.assertFalse(self.game.game_over)
        self.assertNotEqual(self.game.snake, old_snake)
        self.assertNotEqual(self.game.food, old_food)
        # Check snake is reset to initial state
        self.assertEqual(self.game.snake.get_length(), 3)
        center_x = config.GRID_WIDTH // 2
        center_y = config.GRID_HEIGHT // 2
        self.assertEqual(self.game.snake.get_head(), (center_x, center_y))
        # Check food is not on snake
        self.assertNotIn(self.game.food.get_position(), self.game.snake.get_body())

    @patch('snake.src.game.time.sleep')
    def test_run_loop_processes_input_and_moves(self, mock_sleep):
        # Mock input_handler to return a sequence of keys then raise KeyboardInterrupt to break loop
        input_sequence = [
            'right',  # move right
            'pause',  # pause
            'right',  # ignored while paused
            'pause',  # unpause
            'up',     # change direction to up (if not reversing)
            'r',      # restart
            KeyboardInterrupt  # break loop
        ]
        self.game.input_handler.get_key = MagicMock(side_effect=input_sequence)

        # Mock renderer to avoid actual rendering        self.game.renderer.render = MagicMock()

        # Initial snake heading right at center
        center_x = config.GRID_WIDTH // 2
        center_y = config.GRID_HEIGHT // 2
        initial_body = [(center_x, center_y), (center_x-1, center_y), (center_x-2, center_y)]
        self.game.snake.body = initial_body
        self.game.snake.direction = config.DIRECTION_RIGHT

        # Place food ahead of snake so it will be eaten
        food_ahead = (center_x + 1, center_y)
        self.game.food.position = food_ahead
        try:
            self.game.run()
        except KeyboardInterrupt:
            pass

        # After first 'right' input (but we are moving right already, so direction unchanged)
        # Then pause, then another right (ignored), then unpause, then up (change direction to up)
        # Then restart, then loop breaks
        # We'll check that renderer was called multiple times
        self.assertGreaterEqual(self.game.renderer.render.call_count, 3)

    @patch('snake.src.game.time.sleep')
    def test_run_loop_grows_when_eating_food(self, mock_sleep):
        # Mock input to just break immediately after one iteration
        self.game.input_handler.get_key.side_effect = [KeyboardInterrupt]
        self.game.renderer.render = MagicMock()

        # Place food directly ahead of snake        center_x = config.GRID_WIDTH // 2
        center_y = config.GRID_HEIGHT // 2
        self.game.snake.body = [(center_x, center_y), (center_x-1, center_y), (center_x-2, center_y)]
        self.game.snake.direction = config.DIRECTION_RIGHT
        food_ahead = (center_x + 1, center_y)
        self.game.food.position = food_ahead
        self.game.run()

        # Snake should have grown (length 4) because it ate food
        self.assertEqual(self.game.snake.get_length(), 4)
        # Food should have been respawned
        self.assertNotEqual(self.game.food.position, food_ahead)

    @patch('snake.src.game.time.sleep')
    def test_run_loop_detects_self_collision(self, mock_sleep):
        self.game.input_handler.get_key.side_effect = [KeyboardInterrupt]
        self.game.renderer.render = MagicMock()

        # Create a snake that will collide with itself on next move
        # Snake body: [(2,2), (2,3), (2,4)] heading down (0,1)
        # Next head: (2,5) -> no collision yet. Let's set up a collision.
        # Instead, make snake: [(2,2), (2,3), (2,4), (2,5)] heading up (0,-1)
        # Next head: (2,4) which is in body[1:] -> collision
        self.game.snake.body = [(2,2), (2,3), (2,4), (2,5)]
        self.game.snake.direction = config.DIRECTION_UP  # (0,-1)
        # Place food nowhere near to avoid eating
        self.game.food.position = (0,0)

        self.game.run()

        self.assertTrue(self.game.game_over)

    @patch('snake.src.game.time.sleep')
    def test_run_loop_handles_wrap_around(self, mock_sleep):
        self.game.input_handler.get_key.side_effect = [KeyboardInterrupt]
        self.game.renderer.render = MagicMock()

        # Snake at right edge moving right should wrap to left edge
        self.game.snake.body = [(config.GRID_WIDTH-1, 10), (config.GRID_WIDTH-2, 10), (config.GRID_WIDTH-3, 10)]
        self.game.snake.direction = config.DIRECTION_RIGHT
        # Place food at left edge same row to be eaten after wrap
        food_position = (0, 10)
        self.game.food.position = food_position
        self.game.run()

        # Snake should have moved to (0,10) and eaten food, so grown        self.assertEqual(self.game.snake.get_head(), (0, 10))
        self.assertEqual(self.game.snake.get_length(), 4)
        # Food should have respawned
        self.assertNotEqual(self.game.food.position, food_position)

    @patch('snake.src.game.time.sleep')
    def test_run_loop_prevents_reversing_direction(self, mock_sleep):
        self.game.input_handler.get_key.side_effect = [KeyboardInterrupt]
        self.game.renderer.render = MagicMock()

        # Snake moving right
        self.game.snake.direction = config.DIRECTION_RIGHT
        # Try to set direction to left (should be ignored)
        self.game.input_handler.get_key.return_value = 'left'
        self.game.run()

        # Direction should still be right
        self.assertEqual(self.game.snake.direction, config.DIRECTION_RIGHT)

        # Now try to set direction to up (should work)
        self.game.input_handler.get_key.return_value = 'up'
        self.game.run()
        self.assertEqual(self.game.snake.direction, config.DIRECTION_UP)

    @patch('snake.src.game.time.sleep')
    def test_run_loop_toggles_pause_correctly(self, mock_sleep):
        self.game.input_handler.get_key.side_effect = ['pause', 'pause', KeyboardInterrupt]
        self.game.renderer.render = MagicMock()

        self.game.run()

        # Should have paused then unpaused
        self.assertFalse(self.game.paused)

    @patch('snake.src.game.time.sleep')
    def test_run_loop_restarts_on_r_key(self, mock_sleep):
        self.game.input_handler.get_key.side_effect = ['r', KeyboardInterrupt]
        self.game.renderer.render = MagicMock()

        # Modify game state
        self.game.paused = True
        self.game.game_over = True
        old_snake = self.game.snake
        old_food = self.game.food

        self.game.run()

        # Should have reset
        self.assertFalse(self.game.paused)
        self.assertFalse(self.game.game_over)
        self.assertNotEqual(self.game.snake, old_snake)
        self.assertNotEqual(self.game.food, old_food)


if __name__ == "__main__":
    unittest.main()
