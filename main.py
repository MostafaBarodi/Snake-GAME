from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
import time
from food import Food

# Set up the game screen
myscreen = Screen()
myscreen.setup(width=400, height=400)
myscreen.bgcolor("black")
myscreen.title("Snake")
myscreen.tracer(0)

# Create the snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    snake.move()
    # Detection collision with food.
    if snake.segments[0].distance(food) < 15:
        print("tattaaa")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

        # Detect collision with wall.
    if snake.head.xcor() > 180 or snake.head.xcor() < -180 or snake.head.ycor() > 180 or snake.head.ycor() < -180:
        game_is_on = False
        scoreboard.game_over()

        # Detect collision with tail.
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



myscreen.exitonclick()
