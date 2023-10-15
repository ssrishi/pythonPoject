from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PING PONG")

r_paddle = Paddle(370, 0)
l_paddle = Paddle(-370, 0)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # detect collision with wall to bounce back
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
    # detect collision with paddle to bounce back
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    # detect ball misses the paddle
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()    

screen.exitonclick()
