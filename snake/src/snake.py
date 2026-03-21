import config

class Snake:
    def __init__(self, body=None, direction=None):
        if body is None:
            center_x = config.GRID_WIDTH // 2
            center_y = config.GRID_HEIGHT // 2
            self.body = [(center_x, center_y), (center_x-1, center_y), (center_x-2, center_y)]
        else:
            self.body = body
        if direction is None:
            self.direction = config.DIRECTION_RIGHT
        else:
            self.direction = direction

    def move(self, grow=False):
        head_x, head_y = self.get_head()
        if self.direction == config.DIRECTION_UP:
            new_head = (head_x, (head_y - 1) % config.GRID_HEIGHT)
        elif self.direction == config.DIRECTION_DOWN:
            new_head = (head_x, (head_y + 1) % config.GRID_HEIGHT)
        elif self.direction == config.DIRECTION_LEFT:
            new_head = ((head_x - 1) % config.GRID_WIDTH, head_y)
        elif self.direction == config.DIRECTION_RIGHT:
            new_head = ((head_x + 1) % config.GRID_WIDTH, head_y)
        else:
            raise ValueError(f"Unknown direction: {self.direction}")

        new_body = [new_head] + self.body
        if not grow:
            new_body.pop()
        self.body = new_body

    def set_direction(self, direction):
        # Prevent 180-degree turns
        if (self.direction == config.DIRECTION_UP and direction == config.DIRECTION_DOWN) or \
           (self.direction == config.DIRECTION_DOWN and direction == config.DIRECTION_UP) or \
           (self.direction == config.DIRECTION_LEFT and direction == config.DIRECTION_RIGHT) or \
           (self.direction == config.DIRECTION_RIGHT and direction == config.DIRECTION_LEFT):
            return
        self.direction = direction

    def get_head(self):
        return self.body[0]

    def get_body(self):
        return self.body

    def get_length(self):
        return len(self.body)
