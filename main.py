import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Initializing screen
# One think to note is how the Screen class defines the coordinate system. It divides the given size of the screen
# into 2. The negative and the positive. This means that the coordinate of the upper right part of the screen
# (given a width of 600 and height of 600) is (300, 300) while the lower left would be (-300, -300) and so on...
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
# To make movements in synch, the control for
# refreshing the screen is given to the programmer
screen.tracer(0)
# time.sleep() method was used to pause a 'while loop' that refreshes the screen
# REFRESH SPEED is the time argument for the time.sleep().
# The lower the value, the vaster the refresh rate
REFRESH_SPEED = 0.1

# The default size of a turtle is 20 by 20 pixels. The snake's head is left unchanged
# while the food is scaled by FOOD_SIZE_SCALE. This constant variable's value estimates
# The euclidean pixel distance between the food and the snake's head WHEN the sprites collide
# It is also used as the distance threshold when the snake crashed on to itself or the wall
COLLISION_DIST_THRESHOLD = 15


def reset_game(snake, scoreboard):
    # For modularity. This will be called when the snake dies.
    snake.reset_snake()
    scoreboard.reset_game()


def main():

    # instantiating objects
    snake = Snake()
    food = Food(screen_size_width=SCREEN_WIDTH, screen_size_height=SCREEN_HEIGHT)
    scoreboard = ScoreBoard(screen_height=SCREEN_HEIGHT)
    screen.update()

    # setting up listeners for key presses
    screen.listen()
    screen.onkeypress(key="Up", fun=snake.up_direction)
    screen.onkeypress(key="Down", fun=snake.down_direction)
    screen.onkeypress(key="Left", fun=snake.left_direction)
    screen.onkeypress(key="Right", fun=snake.right_direction)

    # Game will only stop when the user clicks the close [X] button
    while True:
        time.sleep(REFRESH_SPEED)

        # Once the game starts, the snake will indefinitely move forward to the direction of the snake's head
        # Until it crashes on to itself or the wall
        snake.move_forward()
        if snake.snake_head.distance(food) < COLLISION_DIST_THRESHOLD:
            snake.eat_food(food, scoreboard)

        if abs(snake.snake_head.xcor()) > ((SCREEN_WIDTH / 2) - COLLISION_DIST_THRESHOLD) or \
                abs(snake.snake_head.ycor()) > ((SCREEN_HEIGHT / 2) - COLLISION_DIST_THRESHOLD):
            reset_game(snake, scoreboard)

        for segment in snake.snake_body[1:]:
            if snake.snake_head.distance(segment) < COLLISION_DIST_THRESHOLD:
                reset_game(snake, scoreboard)

        screen.update()


main()
