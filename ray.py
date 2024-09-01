import pygame

class Ray:
    def __init__(self, screen, pos, length=224):
        self.screen = screen  # Экран, на котором рисуется луч
        self.pos = pos  # Начальная позиция луча
        self.length = length  # Длина луча
        self.ray = pygame.Surface((self.length, 32))  # Создание изображения луча
        self.rect = self.ray.get_rect()  # Прямоугольник для определения границ луча
        self.ray.fill((14, 56, 37))  # Заполнение луча цветом
        self.ray.set_alpha(70)  # Установка прозрачности луча
        self.flag_ray = 1  # Флаг для отображения луча

    def get_input(self, events):
        # Обработка ввода для изменения состояния луча
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    self.flag_ray += 1  # Переключение состояния луча

    def update_position(self, pos):
        self.pos = pos  # Обновление позиции луча

    def draw_ray(self):
        # Отображение луча на экране
        if self.flag_ray % 2 == 0:
            self.screen.blit(self.ray, self.pos)  # Отображаем луч, если флаг указывает на это

    def get_end_position(self):
        # Возвращаем конечную позицию луча (X-координата начала + длина луча)
        return (self.pos[0] + self.length, self.pos[1])