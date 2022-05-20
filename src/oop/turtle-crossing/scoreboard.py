from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 0)
        self.write(f"Game over", align="center", font=FONT)
