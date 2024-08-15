from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()
timmy.speed("fastest")


def go_forward():
    timmy.forward(10)


def go_backward():
    timmy.backward(10)


def head_cw():
    timmy.setheading(timmy.heading() + 10)


def head_ccw():
    timmy.setheading(timmy.heading() - 10)


def draw_or_not():
    if timmy.isdown():
        timmy.penup()
    else:
        timmy.pendown()


screen.onkeypress(go_forward, "w")
screen.onkeypress(go_backward, "s")
screen.onkeypress(head_cw, "d")
screen.onkeypress(head_ccw, "a")
screen.onkeypress(screen.reset, "c")
screen.onkeypress(draw_or_not, "space")

screen.listen()
screen.exitonclick()

