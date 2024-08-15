from turtle import Turtle
from random import randint


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color((randint(0, 255), randint(0, 255), randint(0, 255)))
        self.setheading(180)
        self.penup()
        self.goto(x=300, y=randint(-210, 210))