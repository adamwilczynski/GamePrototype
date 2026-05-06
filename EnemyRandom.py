import pygame
import random
from Sprite import Sprite


class EnemyRandom(Sprite):
    def __init__(self, tile):
        super().__init__("./assets/enemydrone.png", tile)
        self.speed = 50
        self.change_direction_time = 0

    def update(self, dt):
        self.change_direction_time -= dt

        if self.change_direction_time <= 0:
            # Losujemy wektor i od razu go normalizujemy, jeśli nie jest zerowy
            dir_vec = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

            if dir_vec.length_squared() > 0:
                self.move_direction = dir_vec.normalize()

            self.change_direction_time = random.uniform(1, 3)

        # Wywołujemy super().update tylko RAZ na końcu
        super().update(dt)