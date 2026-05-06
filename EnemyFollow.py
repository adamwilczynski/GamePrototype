import pygame
from Sprite import Sprite
from Tile import Tile


class EnemyFollow(Sprite):
    def __init__(self, tile, player_to_follow):
        super().__init__("./assets/enemyfollow.png", tile)
        self.player = player_to_follow
        self.speed = 80

    def update(self, dt):
        enemy_pos = pygame.math.Vector2(self.rect.center)
        player_pos = pygame.math.Vector2(self.player.rect.center)

        direction = player_pos - enemy_pos

        if direction.length_squared() > 0:
            # GŁÓWNA LOGIKA CHOWANIA:
            if self.player.is_hiding:
                # Ucieczka: wektor przeciwny (od gracza)
                self.move_direction = -direction.normalize()
            else:
                # Pościg: wektor do gracza
                self.move_direction = direction.normalize()

            self.look_direction = self.move_direction

        super().update(dt)