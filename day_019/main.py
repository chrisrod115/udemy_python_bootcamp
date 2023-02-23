from turtle import Turtle, Screen
import random as rand

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(20)


def move_backward():
    t.backward(20)


def rotate_left():
    t.left(30)


def rotate_right():
    t.right(30)


# key_dict = {
#     'w': move_forward(),
#     's': move_backward(),
#     'a': rotate_left(),
#     'd': rotate_right(),
# }

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=rotate_left)
screen.onkey(key='d', fun=rotate_right)

screen.exitonclick()
