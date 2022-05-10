import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.width(30)
tim.speed(0)

screen = Screen()
screen.colormode(255)

colours = ["royal blue", "chartreuse", "dark salmon", "dark slate blue", "dark turquoise", "yellow"]
angles = [0, 90, 180, 270]
walks = random.choice(range(1, 100))


def get_random_colour():
    return tuple((random.choice(range(0, 255)), random.choice(range(0, 255)), random.choice(range(0, 255))))


for _ in range(walks):
    tim.color((get_random_colour()))
    tim.forward(30)
    tim.setheading(random.choice(angles))


screen.exitonclick()
