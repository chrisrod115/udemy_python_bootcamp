from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorekeeper import Scorekeeper
import time

INITIAL_POSITION = [(-350, 0), (350, 0)]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
score = Scorekeeper()

ball = Ball()
l_paddle = Paddle(position=INITIAL_POSITION[0])
r_paddle = Paddle(position=INITIAL_POSITION[1])

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.listen()

playing = True
while playing:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 277 or ball.ycor() < -277:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        score.left_point()

    if ball.xcor() < -400:
        ball.reset_position()
        score.right_point()

screen.exitonclick()
