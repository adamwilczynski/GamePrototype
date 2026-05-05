import itertools

import numpy as np
from Tile import Tile

class TileMap:
    TARGET_SCREEN_WIDTH = 1920
    TARGET_SCREEN_HEIGHT = 1080

    TILE_NUMBER_WIDTH = TARGET_SCREEN_WIDTH // Tile.TILE_SIZE
    TILE_NUMBER_HEIGHT = TARGET_SCREEN_HEIGHT // Tile.TILE_SIZE

    # TILE_NUMBER_WIDTH = 4
    # TILE_NUMBER_HEIGHT = 2

    SCREEN_WIDTH = TILE_NUMBER_WIDTH * Tile.TILE_SIZE
    SCREEN_HEIGHT = TILE_NUMBER_HEIGHT * Tile.TILE_SIZE

    def __init__(self):
        self.tiles = []
        for y in range(self.TILE_NUMBER_HEIGHT):
            row = []
            for x in range(self.TILE_NUMBER_WIDTH):
                row.append(
                    Tile(x * Tile.TILE_SIZE, y * Tile.TILE_SIZE)
                )
            self.tiles.append(row)

    def iter_tiles_surfaces(self):
        for row in self.tiles:
            yield from row



if __name__ == "__main__":
    print(
        list(
            TileMap().tiles
        )
    )