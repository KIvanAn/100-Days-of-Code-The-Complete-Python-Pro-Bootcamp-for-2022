import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right_paddle miss ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect left_paddle miss ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
