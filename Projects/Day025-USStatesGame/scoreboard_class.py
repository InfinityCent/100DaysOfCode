from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=200)
        self.color("black")
        self.width(5)
        self.scoreboard()

    def scoreboard(self, score=0):
        self.write(f"{score}/50", align="center", font=("Arial", 30, "bold"))

    def refresh_scoreboard(self, score):
        self.clear()
        self.scoreboard(score=score)