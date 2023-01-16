from turtle import Turtle

# Height / width of turtle in pixels
SECTION_PIXEL_SIZE = 20
# Number of starting sections the snake has
STARTING_NUM_SECTIONS = 3

# See turtle.setheading() documentation
EAST_HEAD = 0
NORTH_HEAD = 90
WEST_HEAD = 180
SOUTH_HEAD = 270


def create_section():
    """Returns a section object"""
    new_section = Turtle(shape="square")
    new_section.color("white")
    new_section.penup()
    return new_section


class Snake:
    def __init__(self):
        # The snake_body list acts as the snake itself. The snake is made up of square "turtles".
        # I will call each turtle as "section". New turtle objects are appended into snake_body if the snake size grows.
        # The section below initializes the first STARTING_NUM_SECTIONS sections of the snake.
        # The snake initially points at east (heading == 0)

        self.snake_body = []
        self.snake_head = None
        self.init_snake()

    def init_snake(self):
        # Initializes the first STARTING_NUM_SECTIONS of the snake and puts them at the middle
        for section_num in range(STARTING_NUM_SECTIONS):
            curr_section = create_section()

            curr_section.penup()

            if section_num == 0:
                curr_section.goto(0, 0)
            else:
                x_offset = SECTION_PIXEL_SIZE * len(self.snake_body)
                curr_section.backward(x_offset)

            self.snake_body.append(curr_section)
        self.snake_head = self.snake_body[0]

    def eat_food(self, food, scoreboard):
        food.new_location()
        scoreboard.add_score()
        self.add_section()

    def add_section(self):
        # appends a section object in the snake_body list
        new_section = create_section()
        tail_end_section = self.snake_body[len(self.snake_body) - 1]
        new_section.goto(x=tail_end_section.xcor(), y=tail_end_section.ycor())

        self.snake_body.append(new_section)

    def move_forward(self):
        # The snake moves starting from its tail. The first to move is the last (tail-end) section of the snake
        # It exactly to the location of the section preceding it (the section before the last section).
        # Then the next section goes to the next, until reaching the head (think of it as a wave, where the
        # movement comes from the tail and reaches the head)
        # In this way, the whole snake's direction is only dependent on where the snake's head is going since
        # every section is just following the section preceding it
        for section_index in range(len(self.snake_body) - 1, 0, -1):
            next_section = self.snake_body[section_index - 1]
            self.snake_body[section_index].goto(x=next_section.xcor(), y=next_section.ycor())

        self.snake_head.forward(SECTION_PIXEL_SIZE)

    def up_direction(self):
        """Makes the snake head turn upward"""
        if self.snake_head.heading() != SOUTH_HEAD:
            self.snake_head.setheading(NORTH_HEAD)

    def down_direction(self):
        """Makes the snake head turn downward"""
        if self.snake_head.heading() != NORTH_HEAD:
            self.snake_head.setheading(SOUTH_HEAD)

    def left_direction(self):
        """Makes the snake head turn left"""
        if self.snake_head.heading() != EAST_HEAD:
            self.snake_head.setheading(WEST_HEAD)

    def right_direction(self):
        """Makes the snake head turn right"""
        if self.snake_head.heading() != WEST_HEAD:
            self.snake_head.setheading(EAST_HEAD)

    def reset_snake(self):
        """Destroys the current snake and creates a new starting snake"""
        for section in self.snake_body:
            section.hideturtle()
        self.snake_body.clear()
        self.init_snake()
