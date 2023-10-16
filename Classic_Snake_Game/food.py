from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randon_x = random.randint(-270, 270)
        randon_y = random.randint(-270, 270)
        self.goto(randon_x, randon_y)
