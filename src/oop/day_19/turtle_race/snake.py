from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(0, 3):
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.goto(0 - (i * 20), 0)
            self.snake.append(tim)

    def move(self):
        for snake_part in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_part - 1].xcor()
            new_y = self.snake[snake_part - 1].ycor()
            self.snake[snake_part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
