from Tile import Tile
from TileMap import TileMap

import pygame

FPS = 60

# pygame setup
pygame.init()
screen = pygame.display.set_mode((TileMap.SCREEN_WIDTH, TileMap.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    tile_map = TileMap()
    for tile in tile_map.iter_tiles_surfaces():
        screen.blit(tile.surface, (tile.x, tile.y))
    # screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 60

pygame.quit()