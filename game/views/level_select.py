import arcade
import os


class LevelSelect(arcade.View):
    def __init__(self):
        super().__init__()

        level_select_sprite_list = arcade.SpriteList()
        cursor_sprite_list = arcade.SpriteList()

    def setup(self):
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        ASSETS_PATH = os.path.join(BASE_PATH, "..", "..", "assets")

        self.medival_cursor = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "medival_cursor.png"),
            scale=1.0
        )
        self.cursor_sprite_list.append(self.medival_cursor)
        
        self.bg_img = arcade.load_texture(
            os.path.join(ASSETS_PATH, "pngs", "dark_bg.png")
        )
        
        self.papirus_easy = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "papirus_lvl_select_easy.png"),
            scale=1
        )
        
        self.papirus_normal = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "papirus_lvl_select_normal.png"),
            scale=1
        )

        self.papirus_hard = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "papirus_lvl_select_hard.png"),
            scale=1
        )

    def on_draw(self):
        self.clear()



    def on_mouse_motion(self, x, y, dx, dy):
        self.medival_cursor.center_x = x
        self.medival_cursor.center_y = y