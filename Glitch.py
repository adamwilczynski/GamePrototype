import pygame
import random
import config
from Sprite import Sprite


class Glitch(Sprite):
    def __init__(self, tile_map):
        self.tile_map = tile_map
        # Losujemy startowy kafelek korzystając z wymiarów z configu
        random_tile = self._get_random_tile()

        # Inicjalizujemy Sprite'a na pozycji tego kafelka
        super().__init__("./assets/glitch.png", random_tile)

    def _get_random_tile(self):
        # Losujemy indeksy wiersza i kolumny
        y = random.randint(0, config.TILE_NUMBER_HEIGHT - 1)
        x = random.randint(0, config.TILE_NUMBER_WIDTH - 1)
        # Zwracamy obiekt Tile z Twojej listy self.tiles
        return self.tile_map.tiles[y][x]

    def relocate(self):
        # Pobieramy nowy losowy kafelek
        new_tile = self._get_random_tile()
        # Aktualizujemy pozycję rect (x i y z obiektu Tile)
        self.rect.topleft = (new_tile.x, new_tile.y)