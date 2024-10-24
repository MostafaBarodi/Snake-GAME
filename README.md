# Snake Game

a classic Snake Game made using the Python Turtle library. This repository contains a simple Snake Game built using Python's turtle module, following an Object-Oriented Programming (OOP) structure. The game allows the player to control the snake's movement using the arrow keys.

## Features
- **Snake Movement**: The player controls the snake using the arrow keys.
- **Object-Oriented Design**: The game is structured using OOP principles, making the code more organized and scalable.
- **Graphical Interface**: The turtle module provides a simple graphical interface to visualize the game.
- **Collision Detection**: Detects collisions with food, the snake's own body, and the walls.
- **Score Tracking**: A scoreboard keeps track of the player's score and displays a game-over message.

## Modifications
- **Screen Update Time**: The game speed is controlled by adjusting the screen update time with `time.sleep(0.1)`, allowing for smooth snake movement.
- **Turtle Class Customization**: The turtle module was manipulated to create snake segments, display food, and handle score display.

## File Structure
- **`main.py`**: Initializes the game screen and manages the game loop. It binds the arrow keys to control the snake's movement.
- **`snake.py`**: Defines the Snake class, which is responsible for creating the snake, managing its movement, and handling direction changes.
- **`food.py`**: Defines the Food class, responsible for generating food at random positions on the screen.
- **`scoreboard.py`**: Manages the scoreboard display and game-over message.

## Task Breakdown
The project was broken down into the following tasks:
1. **Create a snake body**: Initialize the snake with three segments and grow the body after eating food.
2. **Detect collision with food**: Detect when the snake eats food and grow its body.
3. **Move the snake**: Continuously move the snake, updating the position of each segment.
4. **Create a scoreboard**: Display the player's score and a game-over message when the game ends.
5. **Control the snake**: Allow the player to control the snake using the arrow keys.
6. **Detect collision with walls**: End the game if the snake collides with the screen edges.
7. **Detect collision with tail**: End the game if the snake runs into its own body.

## How to Play
- Use the arrow keys to control the direction of the snake.
- The goal is to eat food and grow the snake without hitting the walls or its own body.
- The game ends when the snake collides with a wall or its tail.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/snake-game.git
