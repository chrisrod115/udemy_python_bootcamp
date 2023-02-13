import turtle as t
import random as rand
tim = t.Turtle()

directions = [0, 90, 180, 270]
t.colormode(255)


def rand_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    tup = (r, g, b)
    return tup


t.pensize(15)
t.speed("fastest")

for _ in range(50):
    t.setheading(rand.choice(directions))
    t.pencolor(rand_color())
    t.forward(20)


screen = t.Screen()
screen.exitonclick()
