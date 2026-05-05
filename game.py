import config
from Tile import Tile
from Player import Player
from TileMap import TileMap

import pygame

FPS = 10

# pygame setup
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

tile_map = TileMap()
tile_map.blit(screen)

all_sprites = pygame.sprite.Group()
# player = Player()
# all_sprites.add(player)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    direction = pygame.math.Vector2(0, 0)
    if pressed_keys[pygame.K_LEFT]:
        direction.x = -1
    elif pressed_keys[pygame.K_RIGHT]:
        direction.x = 1
    if pressed_keys[pygame.K_UP]:
        direction.y = -1
    elif pressed_keys[pygame.K_DOWN]:
        direction.y = 1
    # player.direction = direction

    tile_map.blit(screen)
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()