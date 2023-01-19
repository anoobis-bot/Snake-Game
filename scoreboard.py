from turtle import Turtle

# When printing the location of the scoreboard, it must be dynamic since the size of the screen may change
# This acts as the padding to move the scoreboard down so it doesn't go outside the screen
BOARD_HEIGHT = 60

SAVE_FOLDER = "sav"


class ScoreBoard(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(screen_height / 2 - BOARD_HEIGHT)

        self.user_score = 0
        self.high_score = None
        self.load_high_score()
        self.display_text_score()

    def add_score(self):
        """Adds 1 point to user's score"""
        self.user_score += 1
        self.display_text_score()

    def display_text_score(self):
        self.clear()
        self.write(arg=f"Score: {self.user_score} High Score: {self.high_score}", move=False, align="center",
                   font=("Arial", int(BOARD_HEIGHT / 2), "normal"))

    # This function was used at an earlier version when the game would stop after game over
    # def display_game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", move=False, align="center",
    #                font=("Arial", int(BOARD_HEIGHT / 2), "normal"))

    def reset_game(self):
        """Saves the highest score in the file if applicable and resets the user's score to 0"""
        if self.user_score > self.high_score:
            self.high_score = self.user_score
            self.save_high_score()
        self.user_score = 0
        self.display_text_score()

    def load_high_score(self):
        """Loads the current high score from the save file"""
        with open(f"{SAVE_FOLDER}\\data.txt") as file:
            self.high_score = int(file.read())

    def save_high_score(self):
        with open(f"{SAVE_FOLDER}\\data.txt", "w") as file:
            file.write(str(self.high_score))
