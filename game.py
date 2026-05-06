import math

import config
from BackgroundMusic import SpeedControlledBGM

from Player import Player
from EnemyRandom import EnemyRandom
from EnemyFollow import EnemyFollow
from Glitch import Glitch

from TileMap import TileMap

import pygame


def calculate_fps(health):
    return min(
        math.floor(
            config.MAX_FPS * (health / 100)
        ),
        config.MAX_FPS
    )

health = config.MAX_HEALTH
fps = config.MAX_FPS

# pygame setup
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2)
# bgm = SpeedControlledBGM("./assets/core_ambient.wav", speed=1.0, volume=0.5)
# bgm.play()

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
glitch = Glitch(tile_map)

all_sprites.add(enemy_follow)
all_sprites.add(enemyRandom)
all_sprites.add(player)
all_sprites.add(glitch)
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

    if pygame.sprite.collide_mask(player, glitch):
        glitch.relocate()
        health = min(config.MAX_HEALTH, health + 10)
        # Opcjonalnie: print("Zebrałeś glitcha!") lub player.points += 1
        # --- RYSOWANIE ---
    if not player.is_hiding and player.invincibility_timer <= 0:
        # Sprawdzamy kolizję z dronem lub losowym przeciwnikiem
        if pygame.sprite.collide_mask(player, enemy_follow) or \
                pygame.sprite.collide_mask(player, enemyRandom):
            health -= 10  # Spadek zdrowia
            player.invincibility_timer = 1.0

    tile_map.blit(screen)
    all_sprites.update(dt)
    all_sprites.draw(screen)

    pygame.display.update()

    health -= dt * config.HEALTH_DEPLETION
    fps = calculate_fps(health)


    # bgm.set_speed(10 * health / config.MAX_HEALTH)

    if health <= 0:
        running = False

pygame.quit()