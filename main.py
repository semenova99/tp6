import arcade
from game_state import GameState
import random

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 580


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.PURPLE_NAVY)

        self.player_position = SCREEN_WIDTH / 3
        self.bot_position = SCREEN_WIDTH / 3 * 2
        self.rock_button = None
        self.scissors_button = None
        self.paper_button = None
        self.buttons_list = None
        self.computer_pick_icon = None
        self.computer_pick_icon_list = None
        self.player_icons_list = None
        self.player_icon = None
        self.bot_icon = None

        self.state = GameState.NOT_STARTED
        self.pick = None
        self.computer_pick = None
        self.player_wins = 0
        self.computer_wins = 0
        self.result = None

    def setup(self):
        self.buttons_list = arcade.SpriteList()
        self.rock_button = arcade.Sprite("assets/srock.png", 0.5, self.player_position - 80, SCREEN_HEIGHT / 2 - 50)
        self.scissors_button = arcade.Sprite("assets/scissors.png", 0.5, self.player_position, SCREEN_HEIGHT / 2 - 50)
        self.paper_button = arcade.Sprite("assets/spaper.png", 0.5, self.player_position + 80, SCREEN_HEIGHT / 2 - 50)
        self.buttons_list.append(self.rock_button)
        self.buttons_list.append(self.scissors_button)
        self.buttons_list.append(self.paper_button)
        self.computer_pick_icon_list = arcade.SpriteList()
        self.computer_pick_icon = arcade.Sprite("assets/srock.png", 0.5, self.bot_position, SCREEN_HEIGHT / 2 - 50)
        self.computer_pick_icon_list.append(self.computer_pick_icon)

        self.player_icons_list = arcade.SpriteList()
        self.player_icon = arcade.Sprite("assets/faceBeard.png", 0.3, self.player_position, SCREEN_HEIGHT/2 + 50)
        self.bot_icon = arcade.Sprite("assets/compy.png", 1.3, self.bot_position, SCREEN_HEIGHT / 2 + 50)
        self.player_icons_list.append(self.player_icon)
        self.player_icons_list.append(self.bot_icon)

    def on_update(self, delta_time):
        if self.pick is not None and self.state is GameState.ROUND_ACTIVE:
            # check if player won:
            self.computer_pick = random_pick()
            self.computer_pick_icon.texture = arcade.load_texture(get_image_path(self.computer_pick))
            print(arcade.load_texture(get_image_path(self.computer_pick)))
            result = analyze_picks(self.pick, self.computer_pick)
            if result == 1:
                self.player_wins += 1
            elif result == -1:
                self.computer_wins += 1

            # set the state accordingly
            if self.computer_wins >= 3 or self.player_wins >= 3:
                self.state = GameState.GAME_OVER
            else:
                self.state = GameState.ROUND_DONE
                # show only the picked image
                self.set_visibility_buttons(False)

                if self.pick == "ROCK":
                    self.rock_button.visible = True
                elif self.pick == "PAPER":
                    self.paper_button.visible = True
                elif self.pick == "SCISSORS":
                    self.scissors_button.visible = True

    def on_draw(self):
        self.clear()
        if self.state == GameState.NOT_STARTED:
            self.draw_not_started()
        elif self.state == GameState.ROUND_ACTIVE:
            self.draw_round_active()
        elif self.state == GameState.ROUND_DONE:
            self.draw_round_done()
        elif self.state == GameState.GAME_OVER:
            self.draw_game_over()

    def draw_game_over(self):
        self.draw_game_ui()
        arcade.draw_text(
            "Appuyez sur espace pour débuter\nune nouvelle partie",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 + 200,
            arcade.color.WHITE,
            30,
            anchor_x="center",
            anchor_y="center",
            font_name="arial",
            multiline=True,
            width=SCREEN_WIDTH - 100,
            align="center",
        )


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
        self.draw_game_ui()

    def draw_game_ui(self):
        self.buttons_list.draw()
        self.player_icons_list.draw()
        if self.state == GameState.ROUND_DONE or self.state is GameState.GAME_OVER:
            self.computer_pick_icon_list.draw()
        arcade.draw_text(
            f"{self.player_wins} Victoires",
            self.player_position,
            100,
            arcade.color.WHITE,
            25,
            anchor_x="center",
            anchor_y="center",
            font_name="arial",
        )
        arcade.draw_text(
            f"{self.computer_wins} Victoires",
            self.bot_position,
            100,
            arcade.color.WHITE,
            25,
            anchor_x="center",
            anchor_y="center",
            font_name="arial",
        )

    def draw_round_done(self):
        self.draw_game_ui()
        arcade.draw_text(
            "Appuyez sur espace pour continuer la partie",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 + 200,
            arcade.color.WHITE,
            30,
            anchor_x="center",
            anchor_y="center",
            font_name="arial",
        )

        if self.result == 1:
            arcade.draw_text(
                "Vous avez gagné!",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT - 80,
                arcade.color.LIGHT_BLUE,
                25,
                anchor_x="center",
                anchor_y="center",
                font_name="arial",
            )
        elif self.result == -1:
            arcade.draw_text(
                "Vous avez perdu!",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT - 80,
                arcade.color.LIGHT_RED_OCHRE,
                25,
                anchor_x="center",
                anchor_y="center",
                font_name="arial",
            )
        elif self.result == 0:
            arcade.draw_text(
                "Egalité!",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT - 80,
                arcade.color.WHITE,
                25,
                anchor_x="center",
                anchor_y="center",
                font_name="arial",
            )

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
        if self.state == GameState.NOT_STARTED:
            if key == arcade.key.SPACE:
                self.state = GameState.ROUND_ACTIVE
        elif self.state == GameState.ROUND_DONE:
            if key == arcade.key.SPACE:
                self.result = None
                self.pick = None
                self.computer_pick = None
                self.state = GameState.ROUND_ACTIVE
                self.set_visibility_buttons(True)
        elif self.state == GameState.GAME_OVER:
            if key == arcade.key.SPACE:
                self.player_wins = 0
                self.computer_wins = 0
                self.set_visibility_buttons(True)
                self.result = None
                self.pick = None
                self.computer_pick = None
                self.state = GameState.ROUND_ACTIVE

    def on_mouse_press(self, x, y, button, modifiers):
        if self.state == GameState.ROUND_ACTIVE:
            if self.rock_button.collides_with_point((x, y)):
                self.pick = "ROCK"
            elif self.paper_button.collides_with_point((x, y)):
                self.pick = "PAPER"
            elif self.scissors_button.collides_with_point((x, y)):
                self.pick = "SCISSORS"

    def set_visibility_buttons(self, visible):
        self.rock_button.visible = visible
        self.scissors_button.visible = visible
        self.paper_button.visible = visible


def get_image_path(pick):
    if pick == "ROCK":
        return "assets/srock.png"
    elif pick == "PAPER":
        return "assets/spaper.png"
    elif pick == "SCISSORS":
        return "assets/scissors.png"

def analyze_picks(player_pick, computer_pick):
    if player_pick == computer_pick:
        return 0
    elif player_pick == "ROCK":
        return 1 if computer_pick == "SCISSORS" else -1
    elif player_pick == "PAPER":
        return 1 if computer_pick == "ROCK" else -1
    elif player_pick == "SCISSORS":
        return 1 if computer_pick == "PAPER" else -1


def random_pick():
    picks = ["ROCK", "PAPER", "SCISSORS"]
    return random.choice(picks)

def shadow_text(text, x, y, color, size, anchor_x="center", anchor_y="center"):
    arcade.draw_text(text, x + 1, y + 1, arcade.color.BLACK, size, anchor_x, anchor_y)
    arcade.draw_text(text, x, y, color, size, anchor_x, anchor_y)

def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Roche, papier, ciseaux")
    game.setup()
    arcade.run()


main()