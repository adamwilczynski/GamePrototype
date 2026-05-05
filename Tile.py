import pygame
import numpy as np

import config

DEBUG = True

class Tile:
    palette = np.array([
        [0, 0, 0],  # Black
        [255, 255, 255], #White
    ], dtype=np.uint8)


    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y
        self.values = np.random.choice([False, True], size=(config.TILE_SIZE, config.TILE_SIZE))

    @property
    def _rgb_values(self):
        rgb_values = self.palette[self.values.astype(np.uint8)]

        if DEBUG:
            # Set frame borders to True
            rgb_values[0, :] = True  # Top row
            rgb_values[-1, :] = True  # Bottom row
            rgb_values[:, 0] = True  # Left column
            rgb_values[:, -1] = True  # Right column
        return rgb_values

    @property
    def surface(self):
        return pygame.surfarray.make_surface(self._rgb_values)


if __name__ == '__main__':
    tile = Tile(10, 10)
    print(
        tile.values.dtype
    )
    print(tile._rgb_values)