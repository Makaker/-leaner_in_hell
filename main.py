import pygame
import sys
from settings import *  # Импорт настроек из файла settings
from grid import Grid  # Импорт класса Grid для отображения сетки
from player import Player  # Импорт класса Player
from ray import Ray  # Импорт класса Ray
from step_count import Step_count  # Импорт класса Step_count
from skip_step import Skip_step  # Импорт класса Skip_stepф
import mutants


class Game:
    def __init__(self):
        # Инициализация всех компонентов игры
        self.grid = Grid(screen, screen_width, screen_height)  # Создаем сетку

        self.player_sprite = Player((tile_size, tile_size * 7))  # Создаем игрока
        self.player = pygame.sprite.GroupSingle(self.player_sprite)  # Группа для игрока

        # настройки здоровья и осков
        self.lives = 5
        self.lives_surface = pygame.image.load('image/pers/pers_lives.bmp').convert_alpha()
        self.lives_x_start_pos = 10

        self.score = 0
        self.font = pygame.font.Font(None, 36)

        self.mutants = mutants.MUTANTS_MAP
        self.mutants_size = tile_size
        self.blocks_mutants = pygame.sprite.Group()
        self.create_obstacle_mutants()

        self.ray = Ray(screen, self.player_sprite.rect.topright)  # Создаем луч

        self.step_count = Step_count(screen)  # Создаем объект для отслеживания шагов

        self.skip_step = Skip_step(screen)  # Создаем объект для кнопки пропуска хода

    def create_obstacle_mutants(self):
        for row_index, row in enumerate(self.mutants):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = col_index * self.mutants_size
                    y = row_index * self.mutants_size
                    mutant = mutants.Mutant(self.mutants_size, x, y)
                    self.blocks_mutants.add(mutant)

    def collision_check(self):
        # Проверяем, существует ли игрок
        if self.player.sprite is not None:
            # Проверяем наличие лазеров у игрока
            if self.player.sprite.lasers:
                for laser in self.player.sprite.lasers:
                    if pygame.sprite.spritecollide(laser, self.blocks_mutants, True):
                        laser.kill()
                        self.score += 10


            # Проверяем столкновение игрока с мутантами
            if pygame.sprite.spritecollide(self.player_sprite, self.blocks_mutants, True):
                self.lives -= 1
                self.player_sprite.kill()

                # Перемещаем игрока на начальную позицию перед повторным добавлением
                self.player_sprite.rect.topleft = (tile_size, tile_size * 7)
                self.player.add(self.player_sprite)

                if self.lives <= 0:
                    pygame.quit()
                    sys.exit()

    def display_lives(self):
        for live in range(self.lives - 1):
            x = self.lives_x_start_pos + (live * self.lives_surface.get_size()[0] + 10)
            screen.blit(self.lives_surface, (x, 0))

    def display_score(self):
        surface_score = self.font.render(f'Score: {self.score}', False, (82, 133, 74))
        score_rect = surface_score.get_rect(topleft=(170, 0))
        screen.blit(surface_score, score_rect)

    def run(self, events):
        # Обновление состояния игры и отрисовка
        self.collision_check()
        self.blocks_mutants.draw(screen)

        self.display_lives()
        self.display_score()

        if self.player_sprite.alive():
            self.player.update(events)  # Обновляем игрока
            self.player.sprite.lasers.draw(screen)  # Отображаем лазеры игрока
            self.player_sprite.update_step_count(self.skip_step.is_clicked)  # Обновляем количество шагов
            self.player.draw(screen)  # Отображаем игрока

        self.ray.get_input(events)  # Обрабатываем ввод для луча
        self.ray.update_position(self.player_sprite.rect.topright)  # Обновляем позицию луча
        self.ray.draw_ray()  # Отображаем луч

        self.step_count.update_count(self.player_sprite.step_count)  # Обновляем счетчик шагов
        self.step_count.draw()  # Отображаем счетчик шагов

        self.skip_step.check_click(events)  # Проверяем клики на кнопке пропуска хода
        self.skip_step.draw()  # Отображаем кнопку пропуска хода

        self.grid.draw_grid()  # Отображаем сетку


if __name__ == '__main__':
    pygame.init()  # Инициализация Pygame
    screen = pygame.display.set_mode((screen_width, screen_height))  # Установка размеров экрана
    pygame.display.set_caption('CleanerInHell')  # Установка заголовка окна
    pygame.display.set_icon(pygame.image.load('image/pers/icon.bmp'))  # Установка иконки окна
    clock = pygame.time.Clock()  # Создание объекта для управления частотой кадров
    game = Game()  # Создание объекта игры

    while True:
        events = pygame.event.get()  # Получение списка событий
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()  # Завершение работы Pygame
                sys.exit()  # Выход из программы

        screen.fill((170, 27, 27))  # Очистка экрана с заданным цветом
        game.run(events)  # Запуск игрового цикла

        pygame.display.flip()  # Обновление экрана
        clock.tick(FPS)  # Ограничение частоты кадров
