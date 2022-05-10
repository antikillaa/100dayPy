import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.width(20)
tim.speed(0)

screen = Screen()
screen.colormode(255)


def get_random_colour():
    return tuple((random.choice(range(0, 255)), random.choice(range(0, 255)), random.choice(range(0, 255))))


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(get_random_colour())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


draw_spirograph(5)

screen.exitonclick()
