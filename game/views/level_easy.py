import arcade
import os
import math
from other_classes.tower import TowerSprite
from other_classes.bullet import BulletSprite
from other_classes.enemy import EnemySprite

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
ASSETS_PATH = os.path.join(BASE_PATH, "..", "..", "assets")

ENEMY_PATH = [
    (-50, 650),
    (300, 650),
    (300, 300),
    (900, 300),
    (900, 600),
    (1300, 600),
    (1300, 400),
    (1600, 400)
]

class LevelEasy(arcade.View):
    def __init__(self):
        super().__init__()
        
        self.map_sprite_list = arcade.SpriteList()
        self.cursor_sprite_list = arcade.SpriteList()
        self.green_circles_list = arcade.SpriteList()
        self.towers_sprite_list = arcade.SpriteList()
        self.hitchams_sprite_list = arcade.SpriteList()
        self.bullets_list = arcade.SpriteList()
        self.enemies_list = arcade.SpriteList()

        self.money = 500
        self.spawn_timer = 0
        self.enemies_cooldown = 2.0
        
        self.setup()
        self.place_green_cirles()
    
    def setup(self):
        self.bg_img = arcade.load_texture(
            os.path.join(ASSETS_PATH, "pngs", "easy_map.png")
        )

        self.medival_cursor = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "medival_cursor.png"),
            scale=0.8
        )
        self.cursor_sprite_list.append(self.medival_cursor)

    def place_green_cirles(self):
        circles_coords = ((478, 577), (478, 471), (480, 348),(561, 246),
                          (722, 237),(855, 239), (1089, 237),(1261, 240),
                          (1391, 238),(1449, 367), (1452, 537),(1256, 745),
                          (694, 741))

        for coords in circles_coords:
            green_sprite = arcade.Sprite(
                os.path.join(ASSETS_PATH, "pngs", "green_circle.png"),
                scale=0.08
            )
            green_sprite.center_x = coords[0]
            green_sprite.center_y = coords[1]
            self.green_circles_list.append(green_sprite)

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(
            self.bg_img, 
            arcade.rect.XYWH(self.window.width // 2, self.window.height // 2, self.window.width, self.window.height)
        )

        arcade.draw_text(f"Количество монет: {self.money}", 
                    x=self.window.width - 700, 
                    y=self.window.height - 40, 
                    color=arcade.color.WHITE, 
                    font_size=40)

        self.map_sprite_list.draw()
        self.green_circles_list.draw()
        self.hitchams_sprite_list.draw()
        self.towers_sprite_list.draw()
        self.enemies_list.draw()
        self.bullets_list.draw()
        self.cursor_sprite_list.draw()

    def place_tower(self, circle_sprite, x, y):
        if self.money >= 300:
            hitcham_sprite = arcade.Sprite(
                os.path.join(ASSETS_PATH, "pngs", "green_circle.png"),
                scale=0.36
            )
            hitcham_sprite.center_x = circle_sprite.center_x
            hitcham_sprite.center_y = circle_sprite.center_y
            hitcham_sprite.alpha = 50 
            self.hitchams_sprite_list.append(hitcham_sprite)

            tower_sprite = TowerSprite(
                image_path=os.path.join(ASSETS_PATH, "pngs", "red_square.png"),
                scale=0.18,
                range_sprite=hitcham_sprite,
                whatlevel=1
            )
            tower_sprite.center_x = circle_sprite.center_x
            tower_sprite.center_y = circle_sprite.center_y

            self.towers_sprite_list.append(tower_sprite)
            self.money -= 300
            circle_sprite.remove_from_sprite_lists()

    def shoot(self, tower, enemy):
        bullet = BulletSprite(
            filename=os.path.join(ASSETS_PATH, "pngs", "red_square.png"),
            scale=0.05,
            start_x=tower.center_x,
            start_y=tower.center_y,
            target_x=enemy.center_x,
            target_y=enemy.center_y,
            damage=tower.damage
        )
        self.bullets_list.append(bullet)

    def on_update(self, delta_time):
        self.spawn_timer += delta_time
        if self.spawn_timer > self.enemies_cooldown:
            new_enemy = EnemySprite(ENEMY_PATH, scale=0.6)
            self.enemies_list.append(new_enemy)
            self.spawn_timer = 0

        self.enemies_list.update()

        for tower in self.towers_sprite_list:
            tower.on_update(delta_time)

            if tower.last_shot >= tower.cooldown_time:
                enemies_in_range = arcade.check_for_collision_with_list(
                    tower.range_sprite, 
                    self.enemies_list
                )

                if enemies_in_range:
                    target = enemies_in_range[0]
                    self.shoot(tower, target)
                    tower.last_shot = 0

        self.bullets_list.update()

        for bullet in self.bullets_list:
            if (bullet.center_x < 0 or bullet.center_x > self.window.width or 
                bullet.center_y < 0 or bullet.center_y > self.window.height):
                bullet.remove_from_sprite_lists()
                continue

            hit_enemies = arcade.check_for_collision_with_list(bullet, self.enemies_list)
            
            if hit_enemies:
                bullet.remove_from_sprite_lists()
                for enemy in hit_enemies:
                    enemy.hp -= bullet.damage
                    if enemy.hp <= 0:
                        enemy.remove_from_sprite_lists()
                        self.money += 50

    def on_mouse_press(self, x, y, button, modifiers):
        clicked_sprites_circles = arcade.get_sprites_at_point((x, y), self.green_circles_list)
        if clicked_sprites_circles:
            target_circle = clicked_sprites_circles[0]
            self.place_tower(target_circle, x, y)

    def on_mouse_motion(self, x, y, dx, dy):
        self.medival_cursor.center_x = x + 5
        self.medival_cursor.center_y = y - 5