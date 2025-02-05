import arcade
from game_state import GameState

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 580


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.state = GameState.NOT_STARTED

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear()
        if(self.state == GameState.NOT_STARTED):
            arcade.set_background_color(arcade.color.PURPLE_NAVY)
            arcade.draw_text(
                "Roche, Papier, Ciseaux",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT - 80 - 5,
                arcade.color.BLACK,
                50,
                anchor_x="center",
                anchor_y="center",
                font_name="arial",
                bold=True,
                italic=True,
            )
            arcade.draw_text(
                "Roche, Papier, Ciseaux",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT - 80,
                arcade.color.WHITE,
                50,
                anchor_x="center",
                anchor_y="center",
                font_name="arial",
                bold=True,
                italic=True,
            )
            arcade.draw_text(
                "Appuyez sur espace pour commencer",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
                arcade.color.WHITE,
                30,
                anchor_x="center",
                anchor_y="center",
                font_name="arial",
            )

def shadow_text(text, x, y, color, size, anchor_x="center", anchor_y="center"):
    arcade.draw_text(text, x + 1, y + 1, arcade.color.BLACK, size, anchor_x, anchor_y)
    arcade.draw_text(text, x, y, color, size, anchor_x, anchor_y)

def main():
    Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Yalta")
    arcade.run()


main()