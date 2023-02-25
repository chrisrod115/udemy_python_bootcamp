from turtle import Turtle, Screen
from players import Players
import random as rand

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")

player = Players()



screen.exitonclick()