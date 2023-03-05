from turtle import Screen
import time
from snake import Snake

HEIGHT = 600
WIDTH = 600
SCREEN_COLOR = "black"

screen = Screen()
screen.setup(height=HEIGHT, width=WIDTH)
screen.bgcolor(SCREEN_COLOR)
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


playing = True
while playing:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

screen.exitonclick()
