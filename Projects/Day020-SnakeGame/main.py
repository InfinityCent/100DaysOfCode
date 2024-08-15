from turtle import Screen
from scoreboard_class import Scoreboard
from snake_class import Snake
from food_class import Food
import time

SPEED = 0.07

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SPEED)
    # Detect collision with tail
    if snake.ouroboros():
        game_is_on = False

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) <= 15:
        scoreboard.clear()
        scoreboard.increase_score()
        snake.extend()
        food.move()

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or \
            snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False

scoreboard.extend_score_history()
scoreboard.game_over()

screen.exitonclick()
