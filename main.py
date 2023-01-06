import time
from turtle import Screen
from snake import Snake

# Initializing screen
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

SNAKE_SPEED = 0.5


def main():

    snake = Snake()
    screen.update()

    while True:
        time.sleep(SNAKE_SPEED)
        snake.move_forward()
        screen.update()

    screen.mainloop()


main()
