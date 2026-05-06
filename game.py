import config
from Tile import Tile

from Player import Player
from EnemyRandom import EnemyRandom
from EnemyFollow import EnemyFollow

from TileMap import TileMap

import pygame

fps = 60

# pygame setup
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

tile_map = TileMap()
tile_map.blit(screen)

all_sprites = pygame.sprite.Group()
middle_tile = tile_map.tiles[config.TILE_NUMBER_HEIGHT // 2][config.TILE_NUMBER_WIDTH // 2]
top_left_tile = tile_map.tiles[0][0]


player = Player(middle_tile)
enemy_follow = EnemyFollow(top_left_tile,player)
enemyRandom = EnemyRandom(middle_tile)#do zmiany
all_sprites.add(enemy_follow)
all_sprites.add(enemyRandom)
all_sprites.add(player)

while running:
    dt = clock.tick(fps) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.QUIT:
            running = False

    move_direction = pygame.math.Vector2(0, 0)
    player.move_direction = move_direction

    pressed_keys = pygame.key.get_pressed()


    if all([
        pressed_keys[pygame.K_LEFT], pressed_keys[pygame.K_RIGHT]
    ]):
        move_direction.x = 0
    elif pressed_keys[pygame.K_LEFT]:
        move_direction.x = -1
    elif pressed_keys[pygame.K_RIGHT]:
        move_direction.x = 1

    if all([
        pressed_keys[pygame.K_UP], pressed_keys[pygame.K_DOWN]
    ]):
        move_direction.x = 0
    elif pressed_keys[pygame.K_UP]:
        move_direction.y = -1
    elif pressed_keys[pygame.K_DOWN]:
        move_direction.y = 1

    if any([move_direction.x, move_direction.y]):
        player.move_direction = move_direction
        player.look_direction = move_direction

    tile_map.blit(screen)
    all_sprites.update(dt)
    all_sprites.draw(screen)

    pygame.display.update()

pygame.quit()