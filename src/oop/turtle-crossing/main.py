import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager, MOVE_INCREMENT
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
        if player.distance(car) < 20:
            game_is_on = False
            Scoreboard().loose()
        car.move()

    if player.ycor() == 300:
        player.goto(STARTING_POSITION)
        for car in cars:
            car.speed += MOVE_INCREMENT

    screen.update()

screen.exitonclick()
