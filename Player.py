import pygame

import config

from ImageArray import ImageArray
from Sprite import Sprite
from Tile import Tile


class Player(Sprite):
    def __init__(self, tile: Tile):
        super().__init__("./assets/player.png", tile)
        self.look_direction = pygame.math.Vector2(0, 0)
        self.speed = 100
        self.is_hiding = False
        self.invincibility_timer = 0

    def update(self, dt):
        # 1. Odliczanie ochrony
        if self.invincibility_timer > 0:
            self.invincibility_timer -= dt

        # 2. Sprawdzanie klawisza spacji
        keys = pygame.key.get_pressed()
        self.is_hiding = keys[pygame.K_SPACE]

        if self.is_hiding:
            # Zatrzymujemy ruch
            self.move_direction = pygame.math.Vector2(0, 0)
            # Tu nie wywołujemy super().update, żeby animacja nie szła dalej
        else:
            # Normalny ruch i animacja
            super().update(dt)
            self.image = self.image_array.updated_image(self.look_direction)

        # --- FINALNE USTAWIANIE WIDOCZNOŚCI ---
        # Musi być na samym końcu, żeby nadpisać obrazek z animacji
        if self.is_hiding:
            self.image.set_alpha(0)  # Całkowicie niewidoczny
        elif self.invincibility_timer > 0:
            # Miganie po trafieniu (co 100ms)
            alpha = 255 if int(pygame.time.get_ticks() / 100) % 2 == 0 else 0
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255) # W pełni widoczny