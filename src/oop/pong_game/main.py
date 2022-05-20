import time
from turtle import Screen

from src.oop.pong_game.ball import Ball
from src.oop.pong_game.paddle import Paddle
from src.oop.pong_game.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(8, 25)

right_paddle = Paddle(position=(350, 0))
left_paddle = Paddle(position=(-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    elif ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    elif ball.xcor() > 380:
        ball.reset_position()
        score.r_point()

    elif ball.xcor() < -380:
        ball.reset_position()
        score.l_point()



screen.exitonclick()
