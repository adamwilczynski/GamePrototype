import pygame
import numpy as np

import config
import graphic_tools

DEBUG = True

class Tile:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y
        self.values = np.random.choice([False, True], size=(config.TILE_SIZE, config.TILE_SIZE))

    @property
    def surface(self):
        return pygame.surfarray.make_surface(
            graphic_tools.rgb(self.values, True)
        )


if __name__ == '__main__':
    tile = Tile(10, 10)
    print(
        tile.values.dtype
    )
    print(tile._rgb_values)