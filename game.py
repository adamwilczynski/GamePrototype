import config
from Tile import Tile
from Player import Player
from TileMap import TileMap

import pygame

fps = 60
time_to_next_action = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

tile_map = TileMap()
tile_map.blit(screen)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while running:
    dt = clock.tick(fps) / 1000.0
    time_to_next_action -= dt
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.QUIT:
            running = False

    direction = pygame.math.Vector2(0, 0)
    player.direction = direction
    if time_to_next_action <= 0:
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            direction.x = -1
        elif pressed_keys[pygame.K_RIGHT]:
            direction.x = 1
        if pressed_keys[pygame.K_UP]:
            direction.y = -1
        elif pressed_keys[pygame.K_DOWN]:
            direction.y = 1
        if any([direction.x, direction.y]):
            player.direction = direction
            time_to_next_action = config.SECONDS_BETWEEN_ACTIONS


    tile_map.blit(screen)
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()

pygame.quit()