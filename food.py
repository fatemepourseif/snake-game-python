from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5 , stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_position = random.randint(-280 , 280)
        y_position = random.randint(-280 , 280)
        self.goto(x_position,y_position)
