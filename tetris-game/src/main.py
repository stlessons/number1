import pygame
from game.board import Board
from game.tetromino import Tetromino
from game.utils import generate_random_tetromino

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("TETRIS")

# Game variables
board = Board()
current_tetromino = generate_random_tetromino()
clock = pygame.time.Clock()
fall_time = 0
fall_speed = 500  # milliseconds

def draw_window():
    WINDOW.fill((0, 0, 0))  # Clear the window
    board.draw(WINDOW)  # Draw the board
    current_tetromino.draw(WINDOW)  # Draw the current tetromino
    pygame.display.update()  # Update the display

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_tetromino.move_left()
            if event.key == pygame.K_RIGHT:
                current_tetromino.move_right()
            if event.key == pygame.K_DOWN:
                current_tetromino.move_down()
            if event.key == pygame.K_UP:
                current_tetromino.rotate()

def main():
    global fall_time
    global current_tetromino  # Add this line
    while True:
        fall_time += clock.get_rawtime()
        handle_input()
        
        if fall_time >= fall_speed:
            current_tetromino.move_down()
            if board.check_collision(current_tetromino):
                board.add_tetromino(current_tetromino)
                current_tetromino = generate_random_tetromino()
                board.clear_lines()
            fall_time = 0
        
        draw_window()
        clock.tick(60)  # Limit to 60 frames per second

if __name__ == "__main__":
    main()