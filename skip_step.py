import pygame
from settings import *


class Skip_step:
    def __init__(self, screen):
        self.screen = screen
        self.button = pygame.Surface((130, tile_size))
        self.default_color = (90, 124, 166)
        self.hover_color = (120, 150, 200)
        self.button.fill(self.default_color)
        self.rect = self.button.get_rect(topleft=(1040, 0))
        self.flag_mouse_over = False
        self.is_clicked = False  # Переименовал атрибут

        pygame.font.init()
        self.font = pygame.font.Font(None, 36)  # Использует встроенный шрифт. Размер шрифта 36

    def mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.flag_mouse_over = True
        else:
            self.flag_mouse_over = False

    def check_click(self, events):
        mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(mouse_pos):
                self.is_clicked = True
            else:
                self.is_clicked = False

    def draw(self):
        self.mouse_over()

        # Изменяем цвет кнопки в зависимости от состояния
        if self.flag_mouse_over:
            self.button.fill(self.hover_color)
        else:
            self.button.fill(self.default_color)

        # Отображаем текст на кнопке
        text_surface = self.font.render('Next step', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.button.blit(text_surface, (text_rect.x - self.rect.x, text_rect.y - self.rect.y))

        # Отображаем кнопку на экране
        self.screen.blit(self.button, self.rect.topleft)
