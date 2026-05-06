from Tile import Tile

import config

class TileMap:
    def __init__(self):
        self.tiles = []
        for tile_y in range(config.TILE_NUMBER_HEIGHT):
            row = []
            for tile_x in range(config.TILE_NUMBER_WIDTH):
                row.append(
                    Tile(tile_x, tile_y)
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