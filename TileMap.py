import itertools

import numpy as np
from Tile import Tile

import config

class TileMap:
    def __init__(self):
        self.tiles = []
        for y in range(config.TILE_NUMBER_HEIGHT):
            row = []
            for x in range(config.TILE_NUMBER_WIDTH):
                row.append(
                    Tile(x * config.TILE_SIZE, y * config.TILE_SIZE)
                )
            self.tiles.append(row)

    def iter_tiles_surfaces(self):
        for row in self.tiles:
            yield from row

    def blit(self, screen):
        for tile in self.iter_tiles_surfaces():
            screen.blit(tile.surface, (tile.x, tile.y))


if __name__ == "__main__":
    print(
        list(
            TileMap().tiles
        )
    )