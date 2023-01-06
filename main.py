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

REFRESH_SPEED = 0.1


def main():

    snake = Snake()
    screen.update()

    screen.listen()
    screen.onkeypress(key="Up", fun=snake.up_direction)
    screen.onkeypress(key="Down", fun=snake.down_direction)
    screen.onkeypress(key="Left", fun=snake.left_direction)
    screen.onkeypress(key="Right", fun=snake.right_direction)

    while True:
        time.sleep(REFRESH_SPEED)
        snake.move_forward()
        screen.update()

    screen.mainloop()


main()
