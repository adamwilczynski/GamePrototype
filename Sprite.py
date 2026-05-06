import pygame

from Tile import Tile
import config
from ImageArray import ImageArray


class Sprite(pygame.sprite.Sprite):
    speed = 0

    def __init__(
            self,
            filename: str,
            tile: Tile
    ):
        super().__init__()

        self.move_direction = pygame.math.Vector2(0, 0)


        self.image_array = ImageArray(filename)
        self.image = self.image_array.updated_image(self.move_direction)

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(
            topleft=(
                tile.x,
                tile.y
            )
        )

    def update(self, dt):
        self.rect.x += self.move_direction.x * self.speed * dt
        self.rect.y += self.move_direction.y * self.speed * dt

        if self.rect.x >= config.SCREEN_WIDTH:
            self.rect.x = config.SCREEN_WIDTH - config.TILE_SIZE
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y >= config.SCREEN_HEIGHT:
            self.rect.y = config.SCREEN_HEIGHT - config.TILE_SIZE
        if self.rect.y < config.TILE_MAP_START_Y:
            self.rect.y = config.TILE_MAP_START_Y

        self.image = self.image_array.updated_image(None)




