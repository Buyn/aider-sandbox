import unittest
# Change relative import to absolute import starting from src
import src.config as config
from src.snake import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.original_width = config.GRID_WIDTH
        self.original_height = config.GRID_HEIGHT
        config.GRID_WIDTH = 5
        config.GRID_HEIGHT = 5
        
        # Mocking direction constants for testing movement logic independently
        self.DIR_UP = (-1, 0)
        self.DIR_DOWN = (1, 0)
        self.DIR_LEFT = (0, -1)
        self.DIR_RIGHT = (0, 1)
        
        config.DIRECTION_UP = self.DIR_UP
        config.DIRECTION_DOWN = self.DIR_DOWN
        config.DIRECTION_LEFT = self.DIR_LEFT
        config.DIRECTION_RIGHT = self.DIR_RIGHT

    def tearDown(self):
        config.GRID_WIDTH = self.original_width
        config.GRID_HEIGHT = self.original_height
        # Restore original direction constants if they were modified, though usually they are just read.
        # Assuming config.py defines them, we only need to restore grid size.

    def test_init_default(self):
        snake = Snake()
        center_x = config.GRID_WIDTH // 2  # 2
        center_y = config.GRID_HEIGHT // 2 # 2
        
        expected_body = [(center_x, center_y), (center_x-1, center_y), (center_x-2, center_y)]
        
        self.assertEqual(snake.get_body(), expected_body)
        self.assertEqual(snake.direction, config.DIRECTION_RIGHT)

    def test_init_custom(self):
        custom_body = [(1, 1), (1, 0)]
        custom_direction = config.DIRECTION_UP
        snake = Snake(body=custom_body, direction=custom_direction)
        
        self.assertEqual(snake.get_body(), custom_body)
        self.assertEqual(snake.direction, custom_direction)

    def test_move_no_grow(self):
        snake = Snake(body=[(2, 2), (1, 2), (0, 2)], direction=config.DIRECTION_RIGHT)
        snake.move(grow=False)
        
        # Head moves to (2, 3), tail (0, 2) is removed
        expected_body = [(2, 3), (2, 2), (1, 2)]
        self.assertEqual(snake.get_body(), expected_body)

    def test_move_grow(self):
        snake = Snake(body=[(2, 2), (1, 2), (0, 2)], direction=config.DIRECTION_RIGHT)
        snake.move(grow=True)
        
        # Head moves to (2, 3), tail (0, 2) is kept (snake grows)
        expected_body = [(2, 3), (2, 2), (1, 2), (0, 2)]
        self.assertEqual(snake.get_body(), expected_body)

    def test_set_direction(self):
        snake = Snake(direction=config.DIRECTION_RIGHT)
        
        # Should accept valid direction change
        snake.set_direction(config.DIRECTION_UP)
        self.assertEqual(snake.direction, config.DIRECTION_UP)
        
        # Should reject moving in opposite direction (e.g., trying to go down when moving right)
        snake.set_direction(config.DIRECTION_DOWN)
        self.assertEqual(snake.direction, config.DIRECTION_UP) # Should remain UP

        # Should accept moving perpendicular
        snake.set_direction(config.DIRECTION_LEFT)
        self.assertEqual(snake.direction, config.DIRECTION_LEFT)

    def test_wrap_around_right(self):
        # Grid width is 5. Max X index is 4.
        snake = Snake(body=[(2, 4)], direction=config.DIRECTION_RIGHT) # Head at right edge
        snake.move(grow=False)
        
        # Head wraps from X=4 to X=0, Y remains 4
        expected_body = [(2, 0), (2, 4)]
        self.assertEqual(snake.get_body(), expected_body)

    def test_wrap_around_left(self):
        # Grid width is 5. Min X index is 0.
        snake = Snake(body=[(2, 0)], direction=config.DIRECTION_LEFT) # Head at left edge
        snake.move(grow=False)
        
        # Head wraps from X=0 to X=4, Y remains 2
        expected_body = [(2, 4), (2, 0)]
        self.assertEqual(snake.get_body(), expected_body)

    def test_wrap_around_down(self):
        # Grid height is 5. Max Y index is 4.
        snake = Snake(body=[(4, 2)], direction=config.DIRECTION_DOWN) # Head at bottom edge
        snake.move(grow=False)
        
        # Head wraps from Y=4 to Y=0, X remains 4
        expected_body = [(0, 2), (4, 2)]
        self.assertEqual(snake.get_body(), expected_body)

    def test_wrap_around_up(self):
        # Grid height is 5. Min Y index is 0.
        snake = Snake(body=[(0, 2)], direction=config.DIRECTION_UP) # Head at top edge
        snake.move(grow=False)
        
        # Head wraps from Y=0 to Y=4, X remains 0
        expected_body = [(4, 2), (0, 2)]
        self.assertEqual(snake.get_body(), expected_body)

    def test_no_self_collision_after_move(self):
        # Snake body: [(2, 2), (1, 2), (0, 2)]
        snake = Snake(body=[(2, 2), (1, 2), (0, 2)], direction=config.DIRECTION_RIGHT)
        
        # Move right: Head becomes (2, 3). Body excluding tail is [(2, 3), (2, 2), (1, 2)]. Tail (0, 2) is removed.
        snake.move(grow=False)
        
        # New body: [(2, 3), (2, 2), (1, 2)]. Head (2, 3) does not collide with remaining body [(2, 2), (1, 2)].
        self.assertFalse(snake.check_self_collision())
        
        # Test case where collision might happen if length > 3 and head moves into body segment that isn't the tail.
        snake_colliding_long = Snake(body=[(2, 2), (2, 3), (1, 3), (0, 3)], direction=config.DIRECTION_UP)
        # Move up: Head moves to (1, 3). Tail (0, 3) is removed. New body: [(1, 3), (2, 3), (1, 3)]. Head (1, 3) collides with segment at index 2.
        snake_colliding_long.move(grow=False)
        self.assertTrue(snake_colliding_long.check_self_collision())


if __name__ == '__main__':
    unittest.main()
