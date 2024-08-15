from turtle import Turtle


class Timmy(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(x=0, y=-280)

    def create_timmy(self):
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(x=0, y=-280)

    def up(self):
        self.forward(20)

    def back_to_start(self):
        self.clear()
        self.create_timmy()

    def collision(self, cars):
        for car in cars:
            if self.distance(car) < 20:
                return False
        return True