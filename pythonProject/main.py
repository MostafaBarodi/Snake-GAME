from turtle import Screen
from snake import Snake
import time

# Set up the game screen
myscreen = Screen()
myscreen.setup(width=400, height=400)
myscreen.bgcolor("black")
myscreen.title("Snake")
myscreen.tracer(0)

# Create the snake
snake = Snake()

# Bind the keys to the snake movement
myscreen.listen()
myscreen.onkey(snake.up, "Up")
myscreen.onkey(snake.down, "Down")
myscreen.onkey(snake.left, "Left")
myscreen.onkey(snake.right, "Right")

# Game loop
game_is_on = True
while game_is_on:
    myscreen.update()
    time.sleep(0.1)

    # Move the snake
    snake.move()

myscreen.exitonclick()
