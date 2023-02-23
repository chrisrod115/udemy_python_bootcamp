from turtle import Turtle, Screen
import random as rand

t = Turtle()
t.shape("arrow")

colors = ["orange red", "chartreuse", "dark gray", "hot pink", "cyan", "blue", "dark olive green", "linen",
          "blue violet", "gold"]


def make_shape(sides, color):
    t.color(color)
    for _ in range(sides):
        angle = 360 / sides
        t.forward(100)
        t.right(angle)


for num_sides in range(3, 11):
    color_style = rand.choice(colors)
    make_shape(num_sides, color_style)

screen = Screen()
screen.exitonclick()
 