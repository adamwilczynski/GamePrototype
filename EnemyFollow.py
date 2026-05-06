import pygame
from Sprite import Sprite
from Tile import Tile
import random


class EnemyFollow(Sprite):
    def __init__(self, tile, player_to_follow):
        super().__init__("./assets/enemyfollow.png", tile)
        self.player = player_to_follow
        self.speed = 80
        # Dodajemy flagę, by wiedzieć, czy już zaczęliśmy uciekać
        self.is_fleeing = False

    def update(self, dt):
        enemy_pos = pygame.math.Vector2(self.rect.center)
        player_pos = pygame.math.Vector2(self.player.rect.center)
        direction = player_pos - enemy_pos

        if self.player.is_hiding:
            # Jeśli gracz właśnie się schował i jeszcze nie wylosowaliśmy kierunku ucieczki
            if not self.is_fleeing:
                # Losujemy całkowicie nowy wektor
                random_dir = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
                if random_dir.length_squared() > 0:
                    self.move_direction = random_dir.normalize()

                self.is_fleeing = True  # Blokujemy ponowne losowanie w następnej klatce
        else:
            # Gracz się nie chowa - wracamy do trybu pościgu
            self.is_fleeing = False
            if direction.length_squared() > 0:
                self.move_direction = direction.normalize()

        self.look_direction = self.move_direction
        super().update(dt)