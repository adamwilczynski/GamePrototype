import math

import config

from Player import Player
from EnemyRandom import EnemyRandom
from EnemyFollow import EnemyFollow
from Glitch import Glitch

from TileMap import TileMap

import pygame
import wave

import numpy as np

import wave
import numpy as np
import pygame

import wave
import numpy as np
import pygame

def load_wav_sound(filename, speed=1.0, volume=1.0, mixer_channels=16):
    if speed <= 0:
        raise ValueError("speed must be > 0")

    volume = max(0.0, min(1.0, float(volume)))

    with wave.open(filename, "rb") as wf:
        src_channels = wf.getnchannels()
        sample_rate = wf.getframerate()
        sample_width = wf.getsampwidth()
        frame_count = wf.getnframes()
        raw = wf.readframes(frame_count)

    if sample_width != 2:
        raise ValueError("This function expects 16-bit PCM WAV files")

    if pygame.mixer.get_init() is None:
        pygame.mixer.pre_init(
            frequency=sample_rate,
            size=-16,
            channels=2,
            allowedchanges=0
        )
        pygame.init()
        pygame.mixer.set_num_channels(mixer_channels)
        pygame.mixer.set_reserved(1)

    _, _, mixer_channels_actual = pygame.mixer.get_init()

    data = np.frombuffer(raw, dtype=np.int16)

    if src_channels > 1:
        data = data.reshape(-1, src_channels)

    if speed != 1.0:
        old_idx = np.arange(len(data), dtype=np.float32)
        new_length = max(1, int(len(data) / speed))
        new_idx = np.linspace(0, len(data) - 1, new_length, dtype=np.float32)

        if data.ndim == 1:
            data = np.interp(new_idx, old_idx, data).astype(np.int16)
        else:
            data = np.stack(
                [np.interp(new_idx, old_idx, data[:, ch]) for ch in range(data.shape[1])],
                axis=1
            ).astype(np.int16)

    if mixer_channels_actual == 2 and data.ndim == 1:
        data = np.column_stack((data, data))
    elif mixer_channels_actual == 1 and data.ndim == 2:
        data = data.mean(axis=1).astype(np.int16)

    sound = pygame.sndarray.make_sound(data)
    sound.set_volume(volume)
    return sound

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

bg_sound = load_wav_sound("./assets/core_ambient.wav", speed=0.8, volume=0.8     )
background_channel = pygame.mixer.Channel(0)
background_channel.play(bg_sound, loops=-1)

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
        sound = load_wav_sound("./assets/glitch.wav", 4)
        sound.play()
        health = min(config.MAX_HEALTH, health + 10)
        # Opcjonalnie: print("Zebrałeś glitcha!") lub player.points += 1
        # --- RYSOWANIE ---
    if not player.is_hiding and player.invincibility_timer <= 0:
        # Sprawdzamy kolizję z dronem lub losowym przeciwnikiem
        if pygame.sprite.collide_mask(player, enemy_follow) or \
                pygame.sprite.collide_mask(player, enemyRandom):
            health -= 5 # Spadek zdrowia
            player.invincibility_timer = 1.0

    tile_map.blit(screen)
    all_sprites.update(dt)
    all_sprites.draw(screen)

    pygame.display.update()

    health -= dt * config.HEALTH_DEPLETION
    fps = calculate_fps(health)


    if health <= 0:
        running = False

pygame.quit()