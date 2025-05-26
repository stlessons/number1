from .tetromino import Tetromino
import random

def check_collision(board, tetromino, offset):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                board_x = x + tetromino.x + offset[0]
                board_y = y + tetromino.y + offset[1]
                if board_x < 0 or board_x >= len(board[0]) or board_y >= len(board):
                    return True
                if board_y >= 0 and board[board_y][board_x]:
                    return True
    return False

def clear_lines(board):
    lines_to_clear = [i for i, row in enumerate(board) if all(row)]
    for i in lines_to_clear:
        del board[i]
        board.insert(0, [0 for _ in range(len(board[0]))])
    return len(lines_to_clear)

def generate_random_tetromino():
    shape = random.choice(['I', 'O', 'T', 'S', 'Z', 'J', 'L'])
    return Tetromino(shape)