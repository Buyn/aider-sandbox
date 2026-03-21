from .config import GRID_WIDTH, GRID_HEIGHT, DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT

class Snake:
    def __init__(self, body=None, direction=None):
        if body is None:
            center_x = GRID_WIDTH // 2
            center_y = GRID_HEIGHT // 2
            self.body = [(center_x, center_y), (center_x-1, center_y), (center_x-2, center_y)]
        else:
            self.body = body
        if direction is None:
            self.direction = DIRECTION_RIGHT
        else:
            self.direction = direction

    def move(self, grow=False):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        new_head = (new_head[0] % GRID_WIDTH, new_head[1] % GRID_HEIGHT)
        if grow:
            if new_head in self.body:
                return False
        else:
            if new_head in self.body[:-1]:
                return False
        self.body.insert(0, new_head)
        if not grow:
            self.body.pop()
        return True

    def set_direction(self, direction):
        self.direction = direction

    def get_head(self):
        return self.body[0]

    def get_body(self):
        return self.body    def get_length(self):
        return len(self.body)
