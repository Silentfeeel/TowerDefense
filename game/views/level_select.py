import arcade
import os


class LevelSelect(arcade.View):
    def __init__(self):
        super().__init__()

        self.level_select_sprite_list = arcade.SpriteList()
        self.cursor_sprite_list = arcade.SpriteList()

        self.setup()

    def setup(self):
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        ASSETS_PATH = os.path.join(BASE_PATH, "..", "..", "assets")

        self.medival_cursor = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "medival_cursor.png"),
            scale=0.8
        )
        self.cursor_sprite_list.append(self.medival_cursor)
        
        self.bg_img = arcade.load_texture(
            os.path.join(ASSETS_PATH, "pngs", "dark_bg.png")
        )
        
        self.papirus_easy = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "papirus_lvl_select_easy.png"),
            scale=0.5
        )

        self.papirus_easy.center_x = (self.window.width / 2) / 2
        self.papirus_easy.center_y = self.window.height / 2
        
        self.papirus_normal = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "papirus_lvl_select_normal.png"),
            scale=0.5
        )

        self.papirus_normal.center_x = self.window.width / 2
        self.papirus_normal.center_y = self.window.height / 2

        self.papirus_hard = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "papirus_lvl_select_hard.png"),
            scale=0.5
        )

        self.papirus_hard.center_x = self.window.width - ((self.window.width / 2) / 2)
        self.papirus_hard.center_y = self.window.height / 2

        self.back_to_main_menu_btn = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "level_select_back_to_main_menu_btn.png"),
            scale=0.2
        )

        self.back_to_main_menu_btn.center_x = self.window.width / 2
        self.back_to_main_menu_btn.center_y = ((self.window.height / 2) / 2) / 2

        self.level_select_sprite_list.append(self.papirus_easy)
        self.level_select_sprite_list.append(self.papirus_normal)
        self.level_select_sprite_list.append(self.papirus_hard)
        self.level_select_sprite_list.append(self.back_to_main_menu_btn)

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(
            self.bg_img, 
            arcade.rect.XYWH(self.window.width // 2, self.window.height // 2, self.window.width, self.window.height)
        )

        self.level_select_sprite_list.draw()
        self.cursor_sprite_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        clicked_sprites = arcade.get_sprites_at_point((x, y), self.level_select_sprite_list)

        for sprite in clicked_sprites:
            if sprite == self.back_to_main_menu_btn:
                from views.main_menu import MainMenuView

                main_view = MainMenuView()

                self.window.show_view(main_view)
            elif sprite == self.papirus_easy:
                from views.level_easy import LevelEasy

                self.level_easy = LevelEasy()

                self.window.show_view(self.level_easy)
            elif sprite == self.start_btn:
                pass

    def on_mouse_motion(self, x, y, dx, dy):
        self.medival_cursor.center_x = x + 5
        self.medival_cursor.center_y = y - 5