import turtle
from us_states_class import USStates
from scoreboard_class import Scoreboard

screen = turtle.Screen()
screen.title("US States Quiz")
screen.setup(width=750, height=510)
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

us_states = USStates()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    user_input = screen.textinput(title="US States Quiz",
                                  prompt="Enter a US State.\nType 'QUIT' to exit.")
    if us_states.evaluate_answer(user_input):
        us_states.store_user_inputs(user_input)
        us_states.increase_score()
        us_states.move_to_state(user_input)
        scoreboard.refresh_scoreboard(score=us_states.score)

    elif user_input.upper() == "QUIT":
        game_is_on = False

    else:
        game_is_on = us_states.game_is_on()


us_states.missed_states()
screen.exitonclick()
