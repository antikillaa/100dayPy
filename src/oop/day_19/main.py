from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_back():
    tim.back(10)


def clockwise():
    tim.right(10)


def counter_clockwise():
    tim.left(10)


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=screen.clear)

screen.exitonclick()
