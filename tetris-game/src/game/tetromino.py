import pygame

TETROMINO_COLORS = {
    'I': (0, 255, 255),
    'O': (255, 255, 0),
    'T': (128, 0, 128),
    'S': (0, 255, 0),
    'Z': (255, 0, 0),
    'J': (0, 0, 255),
    'L': (255, 165, 0),
}


class Tetromino:
    def __init__(self, shape_type):
        self.shape_type = shape_type
        self.shape = self.get_shape_matrix(shape_type)
        self.rotation = 0
        self.x = 3  # starting x position
        self.y = 0  # starting y position
        self.color = TETROMINO_COLORS[shape_type]

    def get_shape_matrix(self, shape_type):
        # Define the rotation matrices for each shape
        SHAPES = {
            'I': [
                [[1, 1, 1, 1]],
                [[1], [1], [1], [1]],
            ],
            'O': [
                [[1, 1],
                 [1, 1]],
            ],
            'T': [
                [[0, 1, 0],
                 [1, 1, 1]],
                [[1, 0],
                 [1, 1],
                 [1, 0]],
                [[1, 1, 1],
                 [0, 1, 0]],
                [[0, 1],
                 [1, 1],
                 [0, 1]],
            ],
            'S': [
                [[0, 1, 1],
                 [1, 1, 0]],
                [[1, 0],
                 [1, 1],
                 [0, 1]],
            ],
            'Z': [
                [[1, 1, 0],
                 [0, 1, 1]],
                [[0, 1],
                 [1, 1],
                 [1, 0]],
            ],
            'J': [
                [[1, 0, 0],
                 [1, 1, 1]],
                [[1, 1],
                 [1, 0],
                 [1, 0]],
                [[1, 1, 1],
                 [0, 0, 1]],
                [[0, 1],
                 [0, 1],
                 [1, 1]],
            ],
            'L': [
                [[0, 0, 1],
                 [1, 1, 1]],
                [[1, 0],
                 [1, 0],
                 [1, 1]],
                [[1, 1, 1],
                 [1, 0, 0]],
                [[1, 1],
                 [0, 1],
                 [0, 1]],
            ],
        }
        return SHAPES[shape_type]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

    def get_coordinates(self):
        return self.shape[self.rotation]

    def draw(self, surface):
        for y, row in enumerate(self.get_coordinates()):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        surface,
                        self.color,
                        (
                            (self.x + x) * 30,
                            (self.y + y) * 30,
                            30,
                            30,
                        ),
                        0,
                    )

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1