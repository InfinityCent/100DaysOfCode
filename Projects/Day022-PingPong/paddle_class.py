from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position

        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(self.position)
        self.setheading(90)

    def up(self):
        self.setheading(90)
        if self.ycor() < 250:
            self.forward(20)

    def down(self):
        self.setheading(270)
        if self.ycor() > -230:
            self.forward(20)

