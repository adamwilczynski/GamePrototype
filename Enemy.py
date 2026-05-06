from Sprite import Sprite

class Enemy(Sprite):
    def __init__(self):
        super().__init__("./assets/player.png")

        self.speed = 600

    def update(self, dt):
        super().update(dt)
