from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
# MOVE_DISTANCE = 20


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.snake = []
        self.snake_length = 3
        self.create_snake()
        self.move_speed = 10
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(0, self.snake_length):
            self.add_segment((0 - (i * 20), 0))

    def add_segment(self, position):
        tim = Turtle(shape="square")
        self.speed(0)
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.snake.append(tim)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
            seg.clear()
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def up_snake(self):
        self.snake_length += 1
        self.add_segment(self.snake[-1].position())

    def move(self):
        for snake_part in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_part - 1].xcor()
            new_y = self.snake[snake_part - 1].ycor()
            self.snake[snake_part].goto(new_x, new_y)
        self.head.forward(self.move_speed)

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
