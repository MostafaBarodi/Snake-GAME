from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        xcoordinate = random.randint(-180,180)
        ycoordinate = random.randint(-180, 180)
        coo = (xcoordinate, ycoordinate)
        self.goto(coo)
        self.refresh()  # Spawn the food at the start

    def refresh(self):
        """Move the food to a new random location."""
        xcoordinate = random.randint(-180, 180)
        ycoordinate = random.randint(-180, 180)
        self.goto(xcoordinate, ycoordinate)