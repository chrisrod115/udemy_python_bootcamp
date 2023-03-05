from turtle import Screen
from paddle import Paddle


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")

paddle = Paddle()

screen.listen()
screen.onkeypress(paddle.go_up(), "Up")



screen.exitonclick()