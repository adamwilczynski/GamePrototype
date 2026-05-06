import pygame

import config

from ImageArray import ImageArray
from Sprite import Sprite


class Player(Sprite):
    def __init__(self):
        super().__init__("./assets/player.png")

        self.speed = 800

    def check_collision(self, all_sprites):
        pass
