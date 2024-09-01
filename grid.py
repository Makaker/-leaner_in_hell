import pygame


class Grid:
    def __init__(self, screen, w_screen, h_screen):
        self.screen = screen
        self.w_screen = w_screen
        self.h_screen = h_screen

    def draw_grid(self):
        n = 32
        start_line = 1
        for i in range(self.w_screen // 32):
            pygame.draw.line(self.screen, (27, 27, 27), (start_line * n, n), (start_line * n, self.h_screen), 1)
            pygame.draw.line(self.screen, (27, 27, 27), (0, n * start_line), (self.w_screen, n * start_line), 1)
            start_line += 1
