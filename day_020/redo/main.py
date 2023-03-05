from turtle import Turtle, Screen
import time

HEIGHT = 600
WIDTH = 600
SCREEN_COLOR = "black"
TURTLE_SHAPE = "square"
TURTLE_COLOR = "white"

INIT_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
SEGMENTS = []

screen = Screen()
screen.setup(height=HEIGHT, width=WIDTH)
screen.bgcolor(SCREEN_COLOR)

for segment in INIT_COORDINATES:
    turtle = Turtle(shape=TURTLE_SHAPE)
    turtle.color(TURTLE_COLOR)
    turtle.penup()
    turtle.goto(segment)
    SEGMENTS.append(turtle)


screen.tracer(0)

playing = True
while playing:
    screen.update()
    for i in range(len(INIT_COORDINATES)-1, 0, -1):
        new_xloc = SEGMENTS[i-1].xcor()
        new_yloc = SEGMENTS[i-1].ycor()
        SEGMENTS[i].goto(new_xloc, new_yloc)
    SEGMENTS[0].forward(10)
    time.sleep(0.1)

screen.exitonclick()
