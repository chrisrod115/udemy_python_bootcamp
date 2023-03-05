from turtle import Turtle

INIT_POSITION_RIGHT = (350, 0)


class Paddle:
    def __init__(self):
        self.segments = []
        self.paddle_right()
        self.right_paddle = self.segments[0]

    def paddle_right(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.shapesize(stretch_len=1, stretch_wid=5)
        new_segment.penup()
        new_segment.goto(INIT_POSITION_RIGHT)
        self.segments.append(new_segment)

    def go_up(self):
        new_y = self.right_paddle.ycor()
        self.right_paddle.goto(self.right_paddle.xcor(), new_y)

