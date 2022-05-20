from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)
        self.shape("square")
        self.color("white")

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
