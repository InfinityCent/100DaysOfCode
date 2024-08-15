from turtle import Screen
from paddle_class import Paddle
from ball_class import Ball
from scoreboard_class import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard(screen)

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "e")
screen.onkeypress(l_paddle.down, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

    ball.forward(20)

    # Check for paddle collision
    if ball.detect_paddle_collision(r_paddle):
        point_of_collision = ball.ycor() - r_paddle.ycor()
        ball.paddle_ricochet(point_of_collision)

    elif ball.detect_paddle_collision(l_paddle):
        point_of_collision = ball.ycor() - l_paddle.ycor()
        ball.paddle_ricochet(point_of_collision)

    # Check for wall collision
    if ball.detect_wall_collision(screen):
        ball.wall_ricochet()

    # Check if ball is out of bounds and assign score
    if ball.xcor() > screen.screensize()[0]:
        scoreboard.increase_score("L")
        ball.reset_ball()

    if ball.xcor() < -screen.screensize()[0]:
        scoreboard.increase_score("R")
        ball.reset_ball()

    game_is_on = scoreboard.is_game_on()

scoreboard.game_over()





screen.exitonclick()