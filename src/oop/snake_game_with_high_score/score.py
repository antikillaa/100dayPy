from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = None
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.speed(0)
        self.get_high_score()
        self.update_score()

    def get_high_score(self):
        with open("score.txt") as file:
            score = file.read()
            self.high_score = int(score)

    def update_score(self):
        self.write(f"Your score is: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

