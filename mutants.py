import pygame
from settings import MUTANTS_MAP


class Mutant(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.image.load('image/pers/enemy2.bmp').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))


map_mutants = MUTANTS_MAP
