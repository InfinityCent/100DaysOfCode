from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("CadetBlue4")

#tommy = Turtle()
#tommy.shape("turtle")
#tommy.color("coral")
#tommy.penup()
#tommy.setpos(0, 100)
#tommy.pendown()

# Draw dashed line
#for _ in range(10):
#    tommy.forward(10)
#    tommy.penup()
#    tommy.forward(10)
#    tommy.pendown()

# Draw a bunch of shapes in sequence
#for sides in range(3, 11):
#    angle = 360/sides
#    timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#    timmy.width(3)
#    for _ in range(sides):
#        timmy.forward(100)
#        timmy.right(angle)

# Random walk
#tommy.width(5)
#tommy.speed("fastest")
#for _ in range(1000):
#    tommy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#    tommy.setheading(choice([0, 90, 180, 270, 360]))
#    tommy.forward(15)


# Spirograph
timmy.speed("fastest")
timmy.hideturtle()
for degree in range(0, 361, 5):
    timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    timmy.setheading(degree)
    timmy.circle(radius=100)


screen.exitonclick()