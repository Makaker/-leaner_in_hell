import pygame
from settings import*

class Step_count:
    def __init__(self, screen):
        self.screen = screen

        pygame.font.init()
        self.font = pygame.font.Font(None, 36)  # Использует встроенный шрифт. Размер шрифта 36

    def update_count(self, new_count):
        self.count = new_count  # Обновляем количество шагов

    def draw(self):
        text_surface = self.font.render(f'Steps: {self.count}', True, (82, 133, 74))
        self.screen.blit(text_surface, (screen_width - 150, 0))  # Отображаем текст
