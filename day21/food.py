from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('red')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x = random.randint(-280,280)
        y = random.randint(-250,250)
        self.goto(x,y)
