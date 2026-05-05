import pygame
import numpy as np

import config
import utils

DEBUG = True

class Tile:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y
        self.values = utils.create_random_matrix()

    @property
    def surface(self):
        return pygame.surfarray.make_surface(
            utils.rgb(self.values, True)
        )


if __name__ == '__main__':
    tile = Tile(10, 10)
    print(
        tile.values.dtype
    )
    print(tile._rgb_values)