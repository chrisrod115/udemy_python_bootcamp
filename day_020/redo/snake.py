from turtle import Turtle

TURTLE_SHAPE = "square"
TURTLE_COLOR = "white"
INIT_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
BOUNDARIES = [270, -270]


class Snake:
    def __init__(self):
        self.segments = []
        self.add_snake()
        self.head = self.segments[0]
        self.position = self.head.position()


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
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def hit_wall(self):
        if (self.head.xcor() >= (290 or -290)) or (self.head.ycor() >= (290 or -290)):
            return True
