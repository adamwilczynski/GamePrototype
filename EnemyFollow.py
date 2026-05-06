import pygame
from Sprite import Sprite
from Tile import Tile


class EnemyFollow(Sprite):
    def __init__(self, tile, player_to_follow):
        super().__init__("./assets/enemyfollow.png", tile)
        self.player = player_to_follow  # Zapamiętujemy gracza
        self.speed = 80

    def update(self, dt):
        # Obliczamy kierunek na podstawie zapamiętanego obiektu
        enemy_pos = pygame.math.Vector2(self.rect.center)
        player_pos = pygame.math.Vector2(self.player.rect.center)

        direction = player_pos - enemy_pos
        if direction.length_squared() > 0:
            self.move_direction = direction.normalize()

        super().update(dt)