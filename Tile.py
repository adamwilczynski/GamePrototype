import pygame
import numpy as np

import config
import utils

class Tile:
    def __init__(self, tile_x, tile_):
        self.tile_x: int = tile_x
        self.tile_y: int = tile_
        self.values = utils.create_random_matrix()

    @property
    def x(self):
        return self.tile_x * config.TILE_SIZE

    @property
    def y(self):
        return config.TILE_MAP_START_Y + self.tile_y * config.TILE_SIZE  # First row belongs to the UI

    @property
    def surface(self):
        return pygame.surfarray.make_surface(
            utils.rgb(self.values, config.DEBUG)
        )


if __name__ == '__main__':
    tile = Tile(10, 10)
    print(
        tile.values.dtype
    )
    print(tile._rgb_values)