import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.color("red")
tim.speed(0)

colours = ["royal blue", "chartreuse", "dark salmon", "dark slate blue", "dark turquoise", "yellow"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range (2, 15):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
