import arcade
import os
import webbrowser
from config import MUSIC_VOLUME, GITHUB_REPO_PAGE
from views.level_select import LevelSelect

class MainMenuView(arcade.View):
    def __init__(self):
        super().__init__()

        self.main_menu_buttons = arcade.SpriteList()
        self.cursor_sprite_list = arcade.SpriteList()

        self.main_theme_music = None
        self.music_player = None
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
            os.path.join(ASSETS_PATH, "pngs", "main_menu_bg.png")
        )

        self.main_menu_title = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "main_menu_game_title.png"),
            scale=1.0
        )
        
        self.start_btn = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "start_game_btn.png"),
            scale=0.8
        )

        self.exit_game_btn = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "exit_game_btn.png"),
            scale=0.8
        )

        self.github_logo = arcade.Sprite(
            os.path.join(ASSETS_PATH, "pngs", "github-mark.png"),
            scale=0.4
        )

        self.start_btn.center_x = self.window.width // 2
        self.start_btn.center_y = self.window.height // 2 - 120

        self.exit_game_btn.center_x = self.window.width // 2
        self.exit_game_btn.center_y = self.window.height // 2 - 400

        self.main_menu_title.center_x = self.window.width // 2
        self.main_menu_title.center_y = self.window.height - 280

        self.github_logo.center_x = 50
        self.github_logo.center_y = 50

        self.main_menu_buttons.append(self.start_btn)
        self.main_menu_buttons.append(self.exit_game_btn)
        self.main_menu_buttons.append(self.main_menu_title)
        self.main_menu_buttons.append(self.github_logo)

        music_path = os.path.join(ASSETS_PATH, "music", "main_theme.mp3")
        self.main_theme_music = arcade.load_sound(music_path)
        self.music_player = arcade.play_sound(self.main_theme_music, volume=MUSIC_VOLUME, loop=True)

    def on_show_view(self):
        self.window.set_mouse_visible(False)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(
            self.bg_img, 
            arcade.rect.XYWH(self.window.width // 2, self.window.height // 2, self.window.width, self.window.height)
        )

        self.main_menu_buttons.draw()
        self.cursor_sprite_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        clicked_sprites = arcade.get_sprites_at_point((x, y), self.main_menu_buttons)

        for sprite in clicked_sprites:
            if sprite == self.exit_game_btn:
                arcade.exit()
            elif sprite == self.github_logo:
                webbrowser.open(GITHUB_REPO_PAGE)
            elif sprite == self.start_btn:
                level_select_view = LevelSelect()
                self.window.show_view(level_select_view)
                pass

    def on_mouse_motion(self, x, y, dx, dy):
        self.medival_cursor.center_x = x + 5
        self.medival_cursor.center_y = y - 5
