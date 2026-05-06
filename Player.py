import pygame

import config

from ImageArray import ImageArray
from Sprite import Sprite
from Tile import Tile


class Player(Sprite):
    def __init__(self, tile: Tile):
        super().__init__("./assets/player.png", tile)

        self.speed = 100

    def check_collision(self, all_sprites):
        pass
