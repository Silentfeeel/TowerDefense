import arcade
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
ASSETS_PATH = os.path.join(BASE_PATH, "..", "..", "assets")

class LevelEasy(arcade.View):
    def __init__(self):
        super().__init__()
        
        self.map_sprite_list = arcade.SpriteList()
        self.another_sprite_list = arcade.SpriteList()
        self.cursor_sprite_list = arcade.SpriteList()
        self.green_circles_list = arcade.SpriteList()
        self.towers_sprite_list = arcade.SpriteList()
        self.hitchams_sprite_list = arcade.SpriteList()

        self.money = 234234234

        self.waves_cnt = 10
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
        circles_coords = ((478, 577), (478, 471),
                          (480, 348),(561, 246),
                          (722, 237),(855, 239),
                          (1089, 237),(1261, 240),
                          (1391, 238),(1449, 367),
                          (1452, 537),(1256, 745),
                          (694, 741)
        )

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
                        color=arcade.color.DARK_RED, 
                        font_size=40)

        self.map_sprite_list.draw()
        self.green_circles_list.draw()
        self.hitchams_sprite_list.draw()
        self.towers_sprite_list.draw()
        self.cursor_sprite_list.draw()

    def place_hitcham(self, tower_sprite):
        hitcham_sprite = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "green_circle.png"),
            scale=0.36
        )

        hitcham_sprite.center_x = tower_sprite.center_x
        hitcham_sprite.center_y = tower_sprite.center_y
        hitcham_sprite.alpha = 0

        self.hitchams_sprite_list.append(hitcham_sprite)

    def place_tower(self, circle_sprite, x, y):
        if self.money > 300:
            tower_sprite = arcade.Sprite(
                os.path.join(ASSETS_PATH, "pngs", "red_square.png"),
                scale=0.18
            )

            tower_sprite.center_x = circle_sprite.center_x
            tower_sprite.center_y = circle_sprite.center_y

            self.towers_sprite_list.append(tower_sprite)
            self.money -= 300

            self.place_hitcham(tower_sprite)

            circle_sprite.remove_from_sprite_lists()


    def on_mouse_press(self, x, y, button, modifiers):
        print(f"Клик в координатах: x={x}, y={y}")

        clicked_sprites_circles = arcade.get_sprites_at_point((x, y), self.green_circles_list)

        if clicked_sprites_circles:
            target_circle = clicked_sprites_circles[0]
            self.place_tower(target_circle, x, y)


    def on_mouse_motion(self, x, y, dx, dy):
        self.medival_cursor.center_x = x + 5
        self.medival_cursor.center_y = y - 5
        