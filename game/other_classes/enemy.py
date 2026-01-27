import arcade
import math


class EnemySprite(arcade.Sprite):
    def __init__(self, path_points, scale=1.0):
        super().__init__(scale=scale)
        self.path = path_points
        self.current_point_index = 0
        self.speed = 2.0
        self.hp = 100
        
        self.walk_textures = []
        for i in range(8):
            texture = arcade.load_texture(f":resources:images/animated_characters/zombie/zombie_walk{i}.png")
            self.walk_textures.append(texture)
        
        self.texture = self.walk_textures[0]
        self.cur_texture_index = 0
        self.animation_timer = 0.0

        start_x, start_y = self.path[0]
        self.center_x = start_x
        self.center_y = start_y

    def update_animation(self, delta_time: float = 1/60):
        self.animation_timer += delta_time
        if self.animation_timer > 0.1:
            self.cur_texture_index += 1
            if self.cur_texture_index >= len(self.walk_textures):
                self.cur_texture_index = 0
            self.texture = self.walk_textures[self.cur_texture_index]
            self.animation_timer = 0

    def update(self, delta_time: float = 1/60):
        self.update_animation(delta_time)

        if self.current_point_index >= len(self.path):
            self.remove_from_sprite_lists()
            return

        target_x, target_y = self.path[self.current_point_index]
        
        dx = target_x - self.center_x
        dy = target_y - self.center_y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < self.speed:
            self.current_point_index += 1
        else:
            angle = math.atan2(dy, dx)
            
            self.center_x += math.cos(angle) * self.speed
            self.center_y += math.sin(angle) * self.speed