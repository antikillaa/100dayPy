import turtle
from turtle import Screen, Turtle

import pandas
from pandas import DataFrame

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)

data = pandas.read_csv("50_states.csv")

game_is_on = True
correct_states_list = []

while game_is_on:
    guess_state = (screen.textinput(title=f"{len(correct_states_list)}/50 States Correct",
                                    prompt="What's another state name?")).title()

    if guess_state == "Exit":
        new_csv = pandas.concat(correct_states_list)
        new_csv.to_csv("Correct States.csv")
        game_is_on = False

    if guess_state in data.state.values:
        state = data[data.state == guess_state]
        correct_states_list.append(state)
        turtle.speed(0)
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(state.x.item(), state.y.item())
        turtle.write(guess_state)

    if len(correct_states_list) == 49:
        game_is_on = False

turtle.exitonclick()
