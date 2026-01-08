import arcade
from config import (SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, 
                    BOOL_ISFULLSCREEN, BACKGROUND_COLOR)
from views.main_menu import MainMenuView


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, BOOL_ISFULLSCREEN)
    window.background_color = BACKGROUND_COLOR

    menu_view = MainMenuView()
    window.show_view(menu_view)
    menu_view.setup()
    
    arcade.run()


if __name__ == "__main__":
    main()