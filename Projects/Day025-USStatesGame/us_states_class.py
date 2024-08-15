from turtle import Turtle
import pandas


class USStates(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.states = pandas.read_csv("50_states.csv")
        self.user_inputs = []
        self.score = len(set(self.user_inputs))

    def move_to_state(self, state):
        state_row = self.states[self.states["state"] == state.title()]
        x = int(state_row.iloc[0]['x'])
        y = int(state_row.iloc[0]['y'])
        self.goto(x, y)
        self.write(f"{state.title()}", align="center",
                   font=("Arial", 10, "bold"))

    def missed_states(self):
        missed_states = list(set(self.states["state"].to_list()) - set(self.user_inputs))
        self.color("red")
        for state in missed_states:
            self.move_to_state(state)

    def evaluate_answer(self, user_attempt):
        return user_attempt.title() in self.states["state"].to_list()

    def store_user_inputs(self, user_input):
        self.user_inputs.append(user_input.title())

    def increase_score(self):
        self.score = len(set(self.user_inputs))

    def game_is_on(self):
        return self.score < 50
