import pygame
import sys
from constants import WIDTH, HEIGHT, CUBE_SIZE, GRAY, RED, BLACK, BLUE, WHITE, GREEN

class Cube:
    def __init__(self, screen, game_font, val, row, col, mutable=True):
        self.screen = screen
        self.game_font = game_font
        self.val = val
        self.temp_val = 0
        self.row = row
        self.col = col
        self.selected = False
        self.mutable = mutable

    def draw(self, color=None):
        x = self.row * CUBE_SIZE
        y = self.col * CUBE_SIZE

        if self.val == 0 and self.temp_val != 0:
            text = self.game_font.render(f"{self.temp_val}", True, GRAY)
            self.screen.blit(text, (x + 5, y + 5))

        elif self.val != 0:
            if color is None:
                color = BLUE if self.mutable else BLACK

            text = self.game_font.render(f"{self.val}", True, color)
            x_pos = x + (CUBE_SIZE // 2) - (text.get_width() // 2)
            y_pos = y + (CUBE_SIZE // 2) - (text.get_height() // 2)
            self.screen.blit(text, (x_pos, y_pos))

        
        # highlight the cube which is clicked
        if self.selected:
            pygame.draw.rect(self.screen, RED, (x, y, CUBE_SIZE, CUBE_SIZE), 3)

    def visualize_backtracking(self, color=GREEN):
        x = self.row * CUBE_SIZE
        y = self.col * CUBE_SIZE
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # fill the cube with white bg
        pygame.draw.rect(self.screen, WHITE, (x, y, CUBE_SIZE, CUBE_SIZE), 0)

        text = self.game_font.render(f"{self.val}", True, color)
        x_pos = x + (CUBE_SIZE // 2) - (text.get_width() // 2)
        y_pos = y + (CUBE_SIZE // 2) - (text.get_height() // 2)
        self.screen.blit(text, (x_pos, y_pos))

        pygame.draw.rect(self.screen, color, (x, y, CUBE_SIZE, CUBE_SIZE), 3)



    def set_val(self, val):
        self.val = val

    def set_temp(self, val):
        self.temp_val = val
