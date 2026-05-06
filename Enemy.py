from Sprite import Sprite
import pygame
import random


class Enemy(Sprite):
    def __init__(self, tile):
        # super().__init__("./assets/player.png")
        # 1. Przekazujemy ścieżkę do drona
        super().__init__("./assets/enemydrone.png", tile)

        # 2. USTAWIAMY PRĘDKOŚĆ (w Sprite domyślnie jest 0)
        self.speed = 50

        self.change_direction_time = 0

        self.speed = 50
        # Inicjalizujemy move_direction (zgodnie z nazwą w klasie Sprite)
        self.move_direction = pygame.math.Vector2(0, 0)

    def update(self, dt):
        super().update(dt)
        self.change_direction_time -= dt

        if self.change_direction_time <= 0:
            new_x = random.uniform(-1, 1)
            new_y = random.uniform(-1, 1)

            # 3. ZMIANA: Używamy self.move_direction zamiast self.direction
            self.move_direction = pygame.math.Vector2(new_x, new_y)

            if self.move_direction.length() > 0:
                self.move_direction = self.move_direction.normalize()

            # Kierunek patrzenia (look_direction) też warto ustawić,
            # żeby ImageArray wiedziało w którą stronę obrócić grafikę
            self.look_direction = self.move_direction

            self.change_direction_time = random.uniform(1, 3)

        # 4. Wywołujemy update ze Sprite, który używa self.move_direction do ruchu
        super().update(dt)