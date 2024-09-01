import pygame
from laser import Laser
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('image/pers/pers_r.bmp').convert_alpha()  # Загрузка изображения игрока
        self.rect = self.image.get_rect(bottomleft=pos)  # Установка начальной позиции игрока
        self.speed = 32  # Скорость перемещения игрока
        self.step_count = 17  # Количество шагов
        self.lasers = pygame.sprite.Group()  # Группа для хранения лазеров

    def get_input(self, event):
        # Обработка ввода с клавиатуры
        if self.step_count > 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and self.rect.x > 0:
                    self.rect.x -= self.speed  # Перемещение влево
                    self.step_count -= 1  # Уменьшение количества шагов
                elif event.key == pygame.K_d and self.rect.x < screen_width - tile_size:
                    self.rect.x += self.speed  # Перемещение вправо
                    self.step_count -= 1  # Уменьшение количества шагов
                elif event.key == pygame.K_w and self.rect.y > tile_size:
                    self.rect.y -= self.speed  # Перемещение вверх
                    self.step_count -= 1  # Уменьшение количества шагов
                elif event.key == pygame.K_s and self.rect.y < screen_height - tile_size:
                    self.rect.y += self.speed  # Перемещение вниз
                    self.step_count -= 1  # Уменьшение количества шагов
                if event.key == pygame.K_SPACE:
                    self.shoot_laser()  # Выстрел лазером

    def shoot_laser(self):
        # Создание нового лазера и добавление его в группу
        laser_start_pos = self.rect.center
        self.lasers.add(Laser(laser_start_pos, length=224))  # Длина лазера указывается при создании

    def update_step_count(self, fl_skip):
        # Обновление количества шагов при пропуске хода
        if fl_skip:
            self.step_count = 17

    def update(self, events):
        # Обновление состояния игрока
        for event in events:
            self.get_input(event)  # Обработка ввода
        self.lasers.update()  # Обновление состояния лазеров
