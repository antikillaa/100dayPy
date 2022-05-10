import random
from turtle import Turtle, Screen

from src.oop.day_18.hirst_painting import colour_list

tim = Turtle()
tim.shape("arrow")
tim.width(10)
tim.speed(3)
tim.pencolor()
screen = Screen()
screen.colormode(255)

colours = colour_list.colours
tim.penup()
tim.setposition(-400, -300)


def draw_raw():
    for _ in range(10):
        tim.color(random.choice(colours))
        tim.pendown()
        tim.circle(5)
        tim.penup()
        tim.forward(50)


def go_up_row():
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)


for _ in range(10):
    draw_raw()
    go_up_row()


screen.exitonclick()
