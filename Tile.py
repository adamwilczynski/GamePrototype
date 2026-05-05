import pygame
import numpy as np

class Tile:
    TILE_SIZE = 64
    palette = np.array([
        [0, 0, 0],  # Black
        [255, 255, 255], #White
    ], dtype=np.uint8)


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.values = np.random.choice([False, True], size=(self.TILE_SIZE, self.TILE_SIZE))

    @property
    def _rgb_values(self):
        return self.palette[self.values.astype(np.uint8)]

    @property
    def surface(self):
        return pygame.surfarray.make_surface(self._rgb_values)


if __name__ == '__main__':
    tile = Tile(10, 10)
    print(
        tile.values.dtype
    )
    print(tile._rgb_values)