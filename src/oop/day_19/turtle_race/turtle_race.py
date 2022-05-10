import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=-150 + i * 50)
    all_turtles.append(tim)

user_bet = screen.textinput(title="Make you bet", prompt="Which turtle win the race? Enter the color: ")

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0, 15)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.tex
                turtle.setposition(0, 0)
                turtle.write("You win!")
            else:
                turtle.setposition(0, 0)
                turtle.write("You lost!")


screen.exitonclick()
