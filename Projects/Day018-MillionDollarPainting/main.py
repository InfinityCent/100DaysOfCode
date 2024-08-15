import colorgram
from turtle import Turtle, Screen
from random import choice

# Get colours
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
# get rid of the first two because they're likely to be background colours
rgb_colors = rgb_colors[2:]

print(rgb_colors)


# Create Hirst dot painting
screen = Screen()
screen.colormode(255)
screen.canvheight = 300
screen.canvwidth = 400

timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.setposition(-400, -300)
timmy.pendown()


def draw_circles(turtle_obj, num_circles, num_lines, rad_circle, fwd_steps, colours):
    """Draw num_lines with num_circles circles of size rad_circle."""

    for _ in range(num_lines):
        original_pos_x = turtle_obj.pos()[0]
        original_pos_y = turtle_obj.pos()[1]

        for _ in range(num_circles):
            col = choice(colours)
            turtle_obj.color(col)
            turtle_obj.fillcolor(col)
            turtle_obj.begin_fill()
            turtle_obj.circle(rad_circle)
            turtle_obj.end_fill()
            turtle_obj.penup()
            turtle_obj.forward(fwd_steps)
            turtle_obj.pendown()

        turtle_obj.penup()
        turtle_obj.setpos(original_pos_x, original_pos_y + fwd_steps)


draw_circles(timmy, num_circles=10, num_lines=10, rad_circle=10, fwd_steps=50, colours=rgb_colors)
timmy.hideturtle()

screen.exitonclick()