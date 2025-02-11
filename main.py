import arcade
from game_state import GameState

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 580


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.PURPLE_NAVY)

        self.player_position = SCREEN_WIDTH / 3
        self.bot_position = SCREEN_WIDTH / 3 * 2
        self.state = GameState.NOT_STARTED
        self.rock_button = None
        self.scissors_button = None
        self.paper_button = None
        self.buttons_list = None

    def setup(self):
        self.buttons_list = arcade.SpriteList()
        self.rock_button = arcade.Sprite("assets/srock.png", 0.5, self.player_position - 80, SCREEN_HEIGHT / 2 - 50)
        self.scissors_button = arcade.Sprite("assets/scissors.png", 0.5, self.player_position, SCREEN_HEIGHT / 2 - 50)
        self.paper_button = arcade.Sprite("assets/spaper.png", 0.5, self.player_position + 80, SCREEN_HEIGHT / 2 - 50)
        self.buttons_list.append(self.rock_button)
        self.buttons_list.append(self.scissors_button)
        self.buttons_list.append(self.paper_button)


    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear()
        if self.state == GameState.NOT_STARTED:
            self.draw_not_started()
        elif self.state == GameState.ROUND_ACTIVE:
            self.draw_round_active()

    def draw_round_active(self):
        arcade.draw_text(
            "Appuyez sur une image pour faire une attaque!",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT - 80,
            arcade.color.WHITE,
            25,
            anchor_x="center",
            anchor_y="center",
            font_name="arial",
        )
        self.buttons_list.draw()


    def draw_not_started(self):
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

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.state = GameState.ROUND_ACTIVE

def shadow_text(text, x, y, color, size, anchor_x="center", anchor_y="center"):
    arcade.draw_text(text, x + 1, y + 1, arcade.color.BLACK, size, anchor_x, anchor_y)
    arcade.draw_text(text, x, y, color, size, anchor_x, anchor_y)

def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Roche, papier, ciseaux")
    game.setup()
    arcade.run()


main()