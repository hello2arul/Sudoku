import pygame
import sys
import time
from constants import WHITE, BLACK, RED, WIDTH

class GameManager:
    def __init__(self, screen, game_font):
        self.screen = screen
        self.game_font = game_font
        self.wrong_moves = 0
        self.key = None


    def draw_window(self, board, seconds):
        self.screen.fill(WHITE)
        
        text = self.game_font.render(f"Time: {self.get_time(seconds)}", True, BLACK)
        self.screen.blit(text, (WIDTH - 160, 560))

        text = self.game_font.render("X " * self.wrong_moves, True, RED)
        self.screen.blit(text, (20, 560))

        board.draw()


    def listen_for_events(self, board):
        self.board = board

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                   self.key = 1
                if event.key == pygame.K_2:
                   self.key = 2
                if event.key == pygame.K_3:
                   self.key = 3
                if event.key == pygame.K_4:
                   self.key = 4
                if event.key == pygame.K_5:
                   self.key = 5
                if event.key == pygame.K_6:
                   self.key = 6
                if event.key == pygame.K_7:
                   self.key = 7
                if event.key == pygame.K_8:
                   self.key = 8
                if event.key == pygame.K_9:
                    self.key = 9

                if event.key == pygame.K_DELETE:
                    board.clear_cell()
                    self.key = None

                if event.key == pygame.K_SPACE:
                    board.solve()

                if event.key == pygame.K_RETURN:
                    row, col = board.selected
                    if board.cubes[row][col].temp_val != 0:
                        print(board.place_val(board.cubes[row][col].temp_val))
                        if board.place_val(board.cubes[row][col].temp_val):
                            print("Correct Move")
                        else:
                            print("OOps")
                            self.wrong_moves += 1
                            if self.wrong_moves == 14:
                                self.wrong_moves = 1

                        if board.is_game_over():
                            self.game_over()
                    self.key = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                filtered_pos = board.filter_pos(pos)

                if filtered_pos:
                    print(filtered_pos)
                    board.select(filtered_pos[0], filtered_pos[1])



        if board.selected and self.key != None:
            board.place_val(self.key)
            self.key = None

    def get_time(self, seconds):
        second = int(seconds % 60)
        mintues = second // 60
        hr = mintues // 60
        return f" {mintues}:{second}"

    def game_over(self):
        print("Game Over")
        pygame.quit()
        sys.exit()


