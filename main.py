import time
from turtle import Screen
from snake import Snake
from food import Food

# Initializing screen
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

REFRESH_SPEED = 0.1

EAT_DIST_THRESHOLD = 15


def main():

    snake = Snake()
    food = Food(screen_size_width=SCREEN_WIDTH, screen_size_height=SCREEN_HEIGHT)
    screen.update()

    screen.listen()
    screen.onkeypress(key="Up", fun=snake.up_direction)
    screen.onkeypress(key="Down", fun=snake.down_direction)
    screen.onkeypress(key="Left", fun=snake.left_direction)
    screen.onkeypress(key="Right", fun=snake.right_direction)

    while True:
        time.sleep(REFRESH_SPEED)

        snake.move_forward()
        if snake.snake_head.distance(food) < EAT_DIST_THRESHOLD:
            food.new_location()

        screen.update()

    screen.mainloop()


main()
