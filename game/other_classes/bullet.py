import arcade
import math

class BulletSprite(arcade.Sprite):
    def __init__(self, filename, scale, start_x, start_y, target_x, target_y, damage):
        super().__init__(filename, scale=scale)
        self.center_x = start_x
        self.center_y = start_y
        self.damage = damage
        self.speed = 10

        x_diff = target_x - start_x
        y_diff = target_y - start_y
        angle = math.atan2(y_diff, x_diff)

        self.angle = math.degrees(angle)

        self.change_x = math.cos(angle) * self.speed
        self.change_y = math.sin(angle) * self.speed