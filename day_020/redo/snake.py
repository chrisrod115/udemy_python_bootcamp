from turtle import Turtle

TURTLE_SHAPE = "square"
TURTLE_COLOR = "white"
INIT_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.add_snake()

    def add_snake(self):
        for segment in INIT_COORDINATES:
            new_segment = Turtle(shape=TURTLE_SHAPE)
            new_segment.color(TURTLE_COLOR)
            new_segment.penup()
            new_segment.goto(segment)
            self.segments.append(new_segment)

    def move_snake(self):
        for i in range(len(INIT_COORDINATES) - 1, 0, -1):
            new_x_loc = self.segments[i - 1].xcor()
            new_y_loc = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x_loc, new_y_loc)
        self.segments[0].forward(20)

    def up(self):
        self.segments[0].left(90)

    def down(self):
        self.segments[0].left(90)

    def left(self):
        self.segments[0].left(90)

    def right(self):
        self.segments[0].left(90)

