import pygame

import config
from ImageArray import ImageArray


class Sprite(pygame.sprite.Sprite):
    def __init__(self, filename: str):
        super().__init__()

        self.image_array = ImageArray("./assets/player.png")
        self.image = self.image_array.image

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(
            topleft=(
                (config.TILE_NUMBER_WIDTH // 2) * config.TILE_SIZE,
                (config.TILE_NUMBER_HEIGHT // 2) * config.TILE_SIZE
            )
        )
