from turtle import Turtle


class Snake:
    def __init__(self):
        """Initialize the snake with default positions."""
        self.my_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.direction = "Right"  # Initial direction is right

    def create_snake(self):
        """Create the initial snake with 3 segments."""
        for position in self.my_positions:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a segment to the snake at the specified position."""
        snake = Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake.goto(position)
        self.segments.append(snake)

    def move(self):
        """Move the snake forward based on the current direction."""
        # Move each segment to the position of the one ahead of it
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)

        # Move the head based on the current direction
        if self.direction == "Up":
            self.segments[0].setheading(90)  # Set direction to up
        elif self.direction == "Down":
            self.segments[0].setheading(270)  # Set direction to down
        elif self.direction == "Left":
            self.segments[0].setheading(180)  # Set direction to left
        elif self.direction == "Right":
            self.segments[0].setheading(0)  # Set direction to right

        self.segments[0].forward(20)

    # Methods for changing direction
    def up(self):
        """Change direction to up (only if not going down)."""
        if self.direction != "Down":
            self.direction = "Up"

    def down(self):
        """Change direction to down (only if not going up)."""
        if self.direction != "Up":
            self.direction = "Down"

    def left(self):
        """Change direction to left (only if not going right)."""
        if self.direction != "Right":
            self.direction = "Left"

    def right(self):
        """Change direction to right (only if not going left)."""
        if self.direction != "Left":
            self.direction = "Right"
