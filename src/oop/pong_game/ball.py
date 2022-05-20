from turtle import Turtle

STEP = 3


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 0)
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.increase_speed()
        self.y_move *= -1

    def bounce_x(self):
        self.increase_speed()
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

    def increase_speed(self):
        print("Speed UP!!!!")
        self.x_move += 2
        self.y_move += 2
