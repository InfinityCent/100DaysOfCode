from turtle import Screen
from timmy_class import Timmy
from car_class import Car
from level_class import Level
from random import choice
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.colormode(255)
screen.tracer(0)

timmy = Timmy()
level = Level(screen)

screen.listen()
screen.onkeypress(timmy.up, "Up")

game_is_on = True
spawn_car = True
cars = []
while game_is_on:
    screen.update()
    time.sleep(0.1)

    spawn_car = choice([True, False, False])
    if spawn_car:
        cars.append(Car())
    for car in cars:
        car.forward(level.level * 5)

    if timmy.ycor() > screen.screensize()[1]:
        level.increase_level(screen)
        timmy.back_to_start()

    game_is_on = timmy.collision(cars)

level.game_over()
screen.exitonclick()