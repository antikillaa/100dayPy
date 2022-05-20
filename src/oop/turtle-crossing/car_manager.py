import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(1, 2)
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(320, random.choice(range(-240, 240)))
        self.setheading(180)

    def move(self):
        self.forward(MOVE_INCREMENT)
