import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle crossing game")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()

screen.onkey(player.move, "Up")

cars = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.append(CarManager())

    for car in cars:
        if player.distance(car) < 1:
            game_is_on = False
            Scoreboard()
        car.move()

    screen.update()

screen.exitonclick()
