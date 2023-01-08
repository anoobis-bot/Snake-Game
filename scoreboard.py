from turtle import Turtle

BOARD_HEIGHT = 60


class ScoreBoard(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(screen_height / 2 - BOARD_HEIGHT)

        self.user_score = 0
        self.display_text_score(self.user_score)

    def add_score(self):
        self.user_score += 1
        self.display_text_score(self.user_score)

    def display_text_score(self, score):
        self.clear()
        self.write(arg=f"Score: {score}", move=False, align="center",
                   font=("Arial", int(BOARD_HEIGHT / 2), "normal"))
