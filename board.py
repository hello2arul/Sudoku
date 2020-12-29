import pygame
import sys
from cube import Cube
from constants import WIDTH, HEIGHT, ROWS, COLS, BLACK, CUBE_SIZE, RED, GREEN
from solver import find_empty, is_valid_state



class Board:
    board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

    def __init__(self, screen, game_font, rows=ROWS, cols=COLS):
        self.screen = screen
        self.game_font = game_font
        self.cubes = [[Cube(screen, game_font, self.board[i][j], i, j, self.board[i][j] == 0) 
                      for j in range(COLS)] 
                      for i in range(ROWS)]
        self.selected = None
        self.width = WIDTH
        self.height = HEIGHT - 60
        self.rows = rows
        self.cols = cols

    def draw(self):

        for i in range(self.rows + 1):
            thickness = 4 if i != 0 and i % 3 == 0 else 1
            # horizontal line
            pygame.draw.line(self.screen, BLACK, (0, i * CUBE_SIZE), (self.width, i * CUBE_SIZE), thickness)
            # vertical line
            pygame.draw.line(self.screen, BLACK, (i * CUBE_SIZE, 0), (i * CUBE_SIZE, self.height), thickness)        

        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw()


    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False
        
        self.cubes[row][col].selected = True
        self.selected = (row, col)


    def filter_pos(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            x = pos[0] // CUBE_SIZE
            y = pos[1] // CUBE_SIZE
            return (x, y)
        return None

    def place_val(self, val):
        if self.selected is not None:
            row, col = self.selected
            if self.cubes[row][col].mutable:
                if self.cubes[row][col].temp_val == 0:
                    self.cubes[row][col].set_temp(val)
                else:
                    self.cubes[row][col].set_val(val) 
                    self.update_board()
                   
                    return is_valid_state(self.board, row, col, self.cubes[row][col].val)

        return True

    def clear_cell(self):
        row, col = self.selected
        if self.cubes[row][col].mutable:
            self.cubes[row][col].set_val(0)
            self.cubes[row][col].set_temp(0)

    def is_game_over(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].val == 0:
                    return False

        return True

    def update_board(self):
        self.board = [[self.cubes[i][j].val for j in range(self.cols)] for i in range(self.rows)]

    def solve(self):
        self.update_board()
        empty = find_empty(self.board)

        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if is_valid_state(self.board, row, col, num):
                self.board[row][col] = num
                self.cubes[row][col].set_val(num)
                self.cubes[row][col].visualize_backtracking()
                pygame.display.flip()
                pygame.time.delay(200)

                if self.solve():
                    return True

                self.board[row][col] = 0
                self.cubes[row][col].visualize_backtracking(RED)
                self.cubes[row][col].set_val(0)
                pygame.display.flip()
                pygame.time.delay(200)
        
        return False




    

