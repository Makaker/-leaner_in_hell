import pygame
from settings import *

class Laser(pygame.sprite.Sprite):
    def __init__(self, start_pos, speed=3, length=224):
        super().__init__()
        self.speed = speed  # Скорость движения лазера
        self.length = length  # Длина лазера
        self.image = pygame.Surface((10, 2))  # Создание изображения лазера
        self.image.fill((2, 245, 15))  # Заполнение лазера цветом
        self.rect = self.image.get_rect(topleft=start_pos)  # Установка начальной позиции лазера
        self.start_x = start_pos[0]  # Сохранение начальной X-координаты

    def update_position(self, new_start_pos):
        # Обновление позиции лазера при движении игрока
        self.rect.x = new_start_pos[0] + (self.rect.x - self.start_x)
        self.start_x = new_start_pos[0]  # Обновляем начальную X-координату

    def destroy(self):
        # Условие уничтожения лазера, если он вышел за пределы длины луча
        if self.rect.x > self.start_x + self.length:
            self.kill()  # Удаление лазера из группы

    def update(self):
        self.rect.x += self.speed  # Перемещение лазера
        self.destroy()  # Проверка, нужно ли удалить лазер