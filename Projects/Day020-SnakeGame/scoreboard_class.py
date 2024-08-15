from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=270)

        self.write(f"Score: {self.score}", align="center",
                   font=("Arial", 15, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.create_scoreboard()

    def extend_score_history(self):
        with open("scores.txt", "a") as score_file:
            score_file.write(f"{self.score}\n")

    def game_over(self):
        highscores = list(open("scores.txt", "r"))
        for i in range(len(highscores)):
            highscores[i] = int(highscores[i].strip())
        self.goto(0, 0)
        self.write(f"Game Over!\nScore: {self.score}\nHighscore: {max(highscores)}",
                   align="center", font=("Arial", 15, "bold"))
