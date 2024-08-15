from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

# Make the turtles
colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []
y_coord = 150
for colour in colours:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colour)
    new_turtle.goto(-230, y_coord)
    y_coord -= 50
    turtles.append(new_turtle)

red, orange, yellow, green, blue, indigo, violet = [turtles[i] for i in range(7)]

bet = screen.textinput(title="Turtle Race", prompt="Make your bet! Which turtle do you think will win?\n"
                                                   "red/orange/yellow/green/blue/indigo/violet")

# Start race
winner = False
while not winner:
    for turtle in turtles:
        turtle_pos = turtle.xcor()
        steps = randint(10, 20)
        if turtle_pos + steps > 230:
            steps = 230 - turtle_pos
            winner = True
            winning_color = turtle.color()[0]
            turtle.forward(steps)
            break

        turtle.forward(steps)

if bet == winning_color:
    print("Your turtle won!")
else:
    print(f"The winner is the {winning_color} turtle. Your turtle lost...")

screen.exitonclick()
