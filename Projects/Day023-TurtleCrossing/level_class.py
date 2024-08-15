from turtle import Turtle


class Level(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.level = 1
        self.screen = screen
        self.show_level(self.screen)

    def show_level(self):
        self.penup()
        self.hideturtle()
        self.color("black")
        self.width(5)

        self.goto(x=(-self.screen.screensize()[0]/2 - 70), y=(self.screen.screensize()[1]/2 + 90))
        self.write(f"Level: {self.level}", align="left", font=("Arial", 15, "bold"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.show_level(self.screen)

    def game_over(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("red")
        self.width(5)
        self.write(f"You didn't dodge the car in time!", align="left",
                   font=("Arial", 15, "bold"))