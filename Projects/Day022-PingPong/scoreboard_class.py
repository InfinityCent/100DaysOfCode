from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        screen = self.screen
        self.create_scoreboard(screen)

    def create_scoreboard(self, screen):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.width(5)

        # Division line
        self.goto(x=0, y=screen.screensize()[1])
        self.setheading(270)
        while self.ycor() > -screen.screensize()[1]:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

        # Player scores
        self.goto(x=(-screen.screensize()[0]/2), y=(screen.screensize()[0]/2 - 20))
        self.write(f"{self.left_score}", align="center", font=("Arial", 50, "bold"))

        self.goto(x=(screen.screensize()[0]), y=(screen.screensize()[0] / 2 - 20))
        self.write(f"{self.right_score}", align="center", font=("Arial", 50, "bold"))

    def increase_score(self, side):
        if side == "R":
            self.right_score += 1
        elif side == "L":
            self.left_score += 1

        self.clear()
        self.create_scoreboard(self.screen)

    def is_game_on(self):
        if self.left_score < 10 and self.right_score < 10:
            return True
        return False

    def game_over(self):
        if self.left_score == 10:
            #self.clear()
            self.color("green")
            self.goto(0, 0)
            self.write("Game Over! Player 1 Wins.", align="center", font=("Arial", 30, "bold"))

        elif self.right_score == 10:
            #self.clear()
            self.color("green")
            self.goto(0, 0)
            self.write("Game Over! Player 2 Wins.", align="center", font=("Arial", 30, "bold"))