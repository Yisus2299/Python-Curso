from turtle import Screen
from paddles import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")  # background color
screen.setup(800, 600)  # screen size
screen.title("PONG GAME")  # window title
screen.tracer(0)  # disable automatic animation updates

paddle_right = Paddle(350, 0)  # right paddle
paddle_left = Paddle(-350, 0)  # left paddle
ball = Ball()
scoreboard = Scoreboard()


screen.listen()

screen.onkeypress(paddle_left.paddle_up, "Up")
screen.onkeypress(paddle_left.paddle_down, "Down")
screen.onkeypress(paddle_right.paddle_up, "w")
screen.onkeypress(paddle_right.paddle_down, "s")

game_is_on = True
scoreboard.update_scoreboard()  # initialize scoreboard display
while game_is_on:
    time.sleep(ball.speed)
    screen.update()  # update the screen when using tracer(0)
    ball.move()
    
    # detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
    # detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()




















screen.exitonclick()
