import numpy as np
import pygame

import config
from graphic_tools import read_asset


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.direction = pygame.math.Vector2()

        image_mask = read_asset("./assets/player.png")

        self.image = pygame.surfarray.make_surface(
            np.random.choice([False, True], size=(config.TILE_SIZE, config.TILE_SIZE))
        )
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(
            topleft=(
                (config.TILE_NUMBER_WIDTH // 2) * config.TILE_SIZE,
                (config.TILE_NUMBER_HEIGHT // 2) * config.TILE_SIZE
            )
        )

    def update(self):
        self.rect.x += self.direction.x * config.TILE_SIZE
        self.rect.y += self.direction.y * config.TILE_SIZE

        if self.rect.x >= config.SCREEN_WIDTH:
            self.rect.x = config.SCREEN_WIDTH - config.TILE_SIZE
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y >= config.SCREEN_HEIGHT:
            self.rect.y = config.SCREEN_HEIGHT - config.TILE_SIZE
        if self.rect.y < 0:
            self.rect.y = 0


    def check_collision(self, all_sprites):
        pass
