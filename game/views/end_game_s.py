import os
import arcade


class EndGame(arcade.View):
    def __init__(self, money, death_cnts):
        super().__init__()
        self.money = money
        self.death_cnts = death_cnts

        self.cursor_sprite_list = arcade.SpriteList()
        self.back_to_main_menu_btn_list = arcade.SpriteList()

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
            os.path.join(ASSETS_PATH, "pngs", "end_game_bg_s.png")
        )

        self.back_to_main_menu_btn = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "level_select_back_to_main_menu_btn.png"),
            scale=0.2
        )

        self.back_to_main_menu_btn.center_x = self.window.width / 2 / 2 / 2 / 2
        self.back_to_main_menu_btn.center_y = ((self.window.height / 2) / 2) / 2

        self.back_to_main_menu_btn_list.append(self.back_to_main_menu_btn)

    def on_draw(self):
        arcade.draw_texture_rect(
            self.bg_img, 
            arcade.rect.XYWH(self.window.width // 2, self.window.height // 2, self.window.width, self.window.height)
        )

        self.back_to_main_menu_btn_list.draw()
        self.cursor_sprite_list.draw()


    def on_mouse_press(self, x, y, button, modifiers):
        clicked_sprites = arcade.get_sprites_at_point((x, y), self.back_to_main_menu_btn_list)

        for sprite in clicked_sprites:
            if sprite == self.back_to_main_menu_btn:
                from views.main_menu import MainMenuView

                main_view = MainMenuView()

                self.window.show_view(main_view)