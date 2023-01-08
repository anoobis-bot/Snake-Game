import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Initializing screen
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

REFRESH_SPEED = 0.1

COLLISION_DIST_THRESHOLD = 15


def main():

    snake = Snake()
    food = Food(screen_size_width=SCREEN_WIDTH, screen_size_height=SCREEN_HEIGHT)
    scoreboard = ScoreBoard(screen_height=SCREEN_HEIGHT)
    screen.update()

    screen.listen()
    screen.onkeypress(key="Up", fun=snake.up_direction)
    screen.onkeypress(key="Down", fun=snake.down_direction)
    screen.onkeypress(key="Left", fun=snake.left_direction)
    screen.onkeypress(key="Right", fun=snake.right_direction)

    game_over = False
    while not game_over:
        time.sleep(REFRESH_SPEED)

        snake.move_forward()
        if snake.snake_head.distance(food) < COLLISION_DIST_THRESHOLD:
            snake.eat_food(food, scoreboard)

        if abs(snake.snake_head.xcor()) > (SCREEN_WIDTH / 2) - COLLISION_DIST_THRESHOLD or \
                abs(snake.snake_head.ycor()) > (SCREEN_WIDTH / 2) - COLLISION_DIST_THRESHOLD:
            game_over = True
            scoreboard.display_game_over()

        for segment in snake.snake_body:
            if segment == snake.snake_head:
                pass
            elif snake.snake_head.distance(segment) < COLLISION_DIST_THRESHOLD:
                game_over = True
                scoreboard.display_game_over()

        screen.update()

    screen.mainloop()


main()
