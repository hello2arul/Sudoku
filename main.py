import pygame
import time
from constants import WIDTH, HEIGHT, ROWS, COLS
from game_manager import GameManager
from board import Board

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

game_font = pygame.font.SysFont("comicsans", 40)

board = Board(screen, game_font, ROWS, COLS)
game_manager = GameManager(screen, game_font)

start_time = time.time()

while True:

    time_diff = (time.time() - start_time)
    game_manager.listen_for_events(board)
    game_manager.draw_window(board, time_diff)

    pygame.display.flip()
    clock.tick(60)