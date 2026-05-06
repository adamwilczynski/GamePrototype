import pygame

import config

from ImageArray import ImageArray
from Sprite import Sprite


class Player(Sprite):
    def __init__(self):
        super().__init__("./assets/player.png")

        self.direction = pygame.math.Vector2()


    def update(self):
        self.rect.x += self.direction.x * config.TILE_SIZE
        self.rect.y += self.direction.y * config.TILE_SIZE

        if self.rect.x >= config.SCREEN_WIDTH:
            self.rect.x = config.SCREEN_WIDTH - config.TILE_SIZE
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y >= config.SCREEN_HEIGHT:
            self.rect.y = config.SCREEN_HEIGHT - config.TILE_SIZE
        if self.rect.y < config.TILE_MAP_START_Y:
            self.rect.y = config.TILE_MAP_START_Y

        self.image_array.update()
        self.image = self.image_array.image


    def check_collision(self, all_sprites):
        pass
