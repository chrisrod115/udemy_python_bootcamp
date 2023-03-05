from turtle import Turtle

COLOR = "white"
INIT_LOCATION = [(-270, 20), (-270, 0), (-270, -20)]
SHAPE = "square"


class Players:
    def __init__(self):
        self.location = []
        self.add_segment()


    def add_segment(self):
        for location in INIT_LOCATION:
            pass


    def create_segment(self, position):
        new_segment = Turtle(shape=SHAPE)
        new_segment.penup()
        new_segment.color(COLOR)
        new_segment.goto(position[])