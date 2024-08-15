from turtle import Turtle
from random import randint, choice

FIRST_QUADRANT = list(range(0, 91))
SECOND_QUADRANT = list(range(91, 181))
THIRD_QUADRANT = list(range(181, 271))
FOURTH_QUADRANT = list(range(271, 361))
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(360)
        self.speed("fastest")

    def detect_paddle_collision(self, paddle):
        ball_x = self.xcor()
        paddle_x = paddle.xcor()

        if abs(paddle_x - ball_x) < 15:
            return True
        return False

    def paddle_ricochet(self, point_of_collision):
        current_heading = self.heading()

        direction = "L"
        if current_heading in FIRST_QUADRANT + FOURTH_QUADRANT:
            direction = "R"

        if -11 <= point_of_collision <= 11:
            self.right(180)

        elif 11 < point_of_collision < 39:
            if direction == "R":
                self.setheading(0)
                self.left(randint(110, 130))
            else:
                self.setheading(180)
                self.right(randint(110, 130))

        elif -39 < point_of_collision < -11:
            if direction == "R":
                self.setheading(0)
                self.right(randint(110, 130))
            else:
                self.setheading(180)
                self.left(randint(110, 130))

        elif 39 <= point_of_collision < 51:
            if direction == "R":
                self.setheading(0)
                self.left(140)
            else:
                self.setheading(180)
                self.right(140)

        elif -51 < point_of_collision <= -39:
            if direction == "R":
                self.setheading(0)
                self.right(140)
            else:
                self.setheading(180)
                self.left(140)

    def detect_wall_collision(self, screen):
        ball_y = abs(self.ycor())
        screen_height = (screen.screensize()[1])

        if abs(screen_height - ball_y) < 15:
            return True
        return False

    def wall_ricochet(self):
        current_heading = self.heading()
        self.setheading(-current_heading)

    def reset_ball(self):
        self.goto(0, 0)
        headings = list(range(0, 46)) + list(range(315, 361)) + list(range(135, 226))
        self.setheading(choice(headings))


