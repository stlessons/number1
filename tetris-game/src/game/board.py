import pygame


class Board:
    def __init__(self):
        self.width = 10
        self.height = 20
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.cell_size = 30

    def check_collision(self, tetromino):
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    board_x = x + tetromino.x
                    board_y = y + tetromino.y

                    # Check boundaries
                    if (board_x < 0 or board_x >= self.width or
                            board_y >= self.height):
                        return True

                    # Check collision with placed pieces
                    if board_y >= 0 and self.grid[board_y][board_x]:
                        return True
        return False

    def add_tetromino(self, tetromino):
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    board_y = tetromino.y + y
                    board_x = tetromino.x + x
                    # Only add if within bounds
                    if (0 <= board_x < self.width and 
                        0 <= board_y < self.height):
                        self.grid[board_y][board_x] = 1

    def draw(self, surface):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                pygame.draw.rect(
                    surface,
                    (128, 128, 128) if cell else (50, 50, 50),
                    (x * self.cell_size, y * self.cell_size,
                     self.cell_size, self.cell_size),
                    0 if cell else 1
                )

    def clear_lines(self):
        lines_cleared = 0
        y = self.height - 1
        while y >= 0:
            # Check if line is full
            if all(self.grid[y]):
                # Move all lines above down
                for move_y in range(y, 0, -1):
                    self.grid[move_y] = self.grid[move_y - 1][:]
                # Clear top line
                self.grid[0] = [0 for _ in range(self.width)]
                lines_cleared += 1
            else:
                y -= 1
        return lines_cleared