from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.head.color("orange")

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def move(self):
        for pixel_num in range(len(self.snake_body) - 1, 0, -1):
            start_pixel = self.snake_body[pixel_num]
            target_pixel = self.snake_body[pixel_num - 1]

            start_pixel.goto(target_pixel.position())
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_pixel = Turtle(shape="square")
        new_pixel.penup()
        new_pixel.color("white")
        new_pixel.goto(position)
        self.snake_body.append(new_pixel)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def ouroboros(self):
        for snake_segment in self.snake_body[1:]:
            if self.head.distance(snake_segment) < 15:
                return True
        return False

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
