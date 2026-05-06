import pygame

import config

from ImageArray import ImageArray
from Sprite import Sprite
from Tile import Tile


class Player(Sprite):
    def __init__(self, tile: Tile):
        super().__init__("./assets/player.png", tile)
        self.look_direction = pygame.math.Vector2(0, 0)
        self.speed = 100
        self.is_hiding = False

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.is_hiding = keys[pygame.K_SPACE]

        if self.is_hiding:
            # 1. Zatrzymujemy ruch
            self.move_direction = pygame.math.Vector2(0, 0)

            # 2. Wykonujemy ruch (który wyniesie 0), ale OMIJAMY super().update(dt),
            # aby klasa Sprite nie nadpisała nam obrazka nową klatką animacji.
            # Musimy jednak ręcznie wywołać przemieszczenie (choć tu będzie 0).
            self.rect.x += self.move_direction.x * self.speed * dt
            self.rect.y += self.move_direction.y * self.speed * dt
        else:
            # 3. Jeśli się nie chowamy, pozwalamy Sprite'owi robić swoje (ruch + animacja)
            super().update(dt)
            self.image = self.image_array.updated_image(self.move_direction)

    def check_collision(self, all_sprites):
        pass
