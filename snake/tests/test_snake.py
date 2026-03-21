import unittest
from src.snake import Snake
import src.config as config

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.original_width = config.GRID_WIDTH
        self.original_height = config.GRID_HEIGHT
        config.GRID_WIDTH = 5
        config.GRID_HEIGHT = 5

    def tearDown(self):
        config.GRID_WIDTH = self.original_width
        config.GRID_HEIGHT = self.original_height

    def test_init_default(self):
        snake = Snake()
        self.assertEqual(snake.direction, config.DIRECTION_RIGHT)
        center_x = config.GRID_WIDTH // 2
        center_y = config.GRID_HEIGHT // 2
        expected_body = [(center_x, center_y), (center_x-1, center_y), (center_x-2, center_y)]
        self.assertEqual(snake.body, expected_body)
        self.assertEqual(snake.get_head(), expected_body[0])
        self.assertEqual(snake.get_body(), expected_body)  # get_body returns full body
        self.assertEqual(snake.get_length(), len(expected_body))

    def test_init_custom(self):
        custom_body = [(1,1), (1,2), (1,3)]
        custom_direction = config.DIRECTION_UP
        snake = Snake(body=custom_body, direction=custom_direction)
        self.assertEqual(snake.body, custom_body)
        self.assertEqual(snake.direction, custom_direction)
        self.assertEqual(snake.get_head(), custom_body[0])
        self.assertEqual(snake.get_body(), custom_body)
        self.assertEqual(snake.get_length(), len(custom_body))

    def test_move_no_grow(self):
        snake = Snake(body=[(2,2), (1,2), (0,2)], direction=config.DIRECTION_RIGHT)
        snake.move(grow=False)
        self.assertEqual(snake.get_head(), (3,2))
        self.assertEqual(snake.body, [(3,2), (2,2), (1,2)])
        self.assertEqual(snake.get_body(), [(3,2), (2,2), (1,2)])
        self.assertEqual(snake.get_length(), 3)

    def test_move_grow(self):
        snake = Snake(body=[(2,2), (1,2), (0,2)], direction=config.DIRECTION_RIGHT)
        snake.move(grow=True)
        self.assertEqual(snake.get_head(), (3,2))
        self.assertEqual(snake.body, [(3,2), (2,2), (1,2), (0,2)])
        self.assertEqual(snake.get_body(), [(3,2), (2,2), (1,2), (0,2)])
        self.assertEqual(snake.get_length(), 4)

    def test_set_direction(self):
        snake = Snake()
        snake.set_direction(config.DIRECTION_UP)
        self.assertEqual(snake.direction, config.DIRECTION_UP)
        snake.set_direction(config.DIRECTION_DOWN)
        self.assertEqual(snake.direction, config.DIRECTION_DOWN)
        snake.set_direction(config.DIRECTION_LEFT)
        self.assertEqual(snake.direction, config.DIRECTION_LEFT)
        snake.set_direction(config.DIRECTION_RIGHT)
        self.assertEqual(snake.direction, config.DIRECTION_RIGHT)

    def test_wrap_around_right(self):
        snake = Snake(body=[(config.GRID_WIDTH-1, 2), (config.GRID_WIDTH-2, 2)], direction=config.DIRECTION_RIGHT)
        snake.move(grow=False)
        self.assertEqual(snake.get_head(), (0,2))
        self.assertEqual(snake.get_body(), [(0,2), (config.GRID_WIDTH-1, 2)])

    def test_wrap_around_left(self):
        snake = Snake(body=[(0,2), (1,2)], direction=config.DIRECTION_LEFT)
        snake.move(grow=False)
        self.assertEqual(snake.get_head(), (config.GRID_WIDTH-1, 2))
        self.assertEqual(snake.get_body(), [(config.GRID_WIDTH-1, 2), (0,2)])

    def test_wrap_around_down(self):
        snake = Snake(body=[(2, config.GRID_HEIGHT-1), (2, config.GRID_HEIGHT-2)], direction=config.DIRECTION_DOWN)
        snake.move(grow=False)
        self.assertEqual(snake.get_head(), (2, 0))
        self.assertEqual(snake.get_body(), [(2, 0), (2, config.GRID_HEIGHT-1)])

    def test_wrap_around_up(self):
        snake = Snake(body=[(2,0), (2,1)], direction=config.DIRECTION_UP)
        snake.move(grow=False)
        self.assertEqual(snake.get_head(), (2, config.GRID_HEIGHT-1))
        self.assertEqual(snake.get_body(), [(2, config.GRID_HEIGHT-1), (2,0)])

    def test_no_self_collision_after_move(self):
        snake = Snake(body=[(2,2), (1,2), (0,2)], direction=config.DIRECTION_RIGHT)
        snake.move(grow=False)
        # Head should not be in body segments (excluding head)
        self.assertNotIn(snake.get_head(), snake.get_body()[1:])

if __name__ == '__main__':
    unittest.main()
