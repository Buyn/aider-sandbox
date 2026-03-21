    def test_move_no_grow(self):
        snake = Snake(body=[(2, 2), (1, 2), (0, 2)], direction=config.DIRECTION_RIGHT)
        snake.move(grow=False)
        
        # Head moves to (2, 3), tail (0, 2) is removed
        expected_body = [(2, 3), (2, 2), (1, 2)]
        self.assertEqual(snake.get_body(), expected_body)
