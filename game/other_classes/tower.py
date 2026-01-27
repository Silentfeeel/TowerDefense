import arcade

class TowerSprite(arcade.Sprite):
    def __init__(self, image_path: str, scale: float, range_sprite: arcade.Sprite, whatlevel: int = 1):
        super().__init__(image_path, scale=scale)
        
        self.level = whatlevel
        self.range_sprite = range_sprite
        self.last_shot = 0.0

        if whatlevel == 1:
            self.damage = 100
            self.cooldown_time = 2
        elif whatlevel == 2:
            self.damage = 50
            self.cooldown_time = 2.5
        else:
            self.damage = 30
            self.cooldown_time = 2.5

    def on_update(self, delta_time: float = 1 / 60):
        self.last_shot += delta_time