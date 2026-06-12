import os
from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")

base_dir = os.path.dirname(__file__)
image = os.path.join(base_dir, "blank_states_img.gif")
csv_path = os.path.join(base_dir, "50_states.csv")

screen.addshape(image)
pen = Turtle()
pen.shape(image)

data = pd.read_csv(csv_path)
all_states = data.state.to_list()



guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 correct",
        prompt="What's the name of another state?"
    )
    # If answer_state is one of the states in 50_states.csv,
    # create a turtle to write the state name at its coordinates

    if answer_state is None:
        screen.bye()
        break
    answer_state = answer_state.title()
    if answer_state == "Exit":
        screen.bye()
        break

    if answer_state in all_states and answer_state not in guessed_states:
        state_data = data[data.state == answer_state]
        guessed_states.append(answer_state)

        t = Turtle()
        t.hideturtle()
        t.penup()
        x = int(state_data.x.iloc[0])
        y = int(state_data.y.iloc[0])
        t.goto(x, y)
        t.write(state_data.state.iloc[0])


# States to learn CSV
missing_states = [state for state in all_states if state not in guessed_states]
# i.e. states in all_states if the state is not in guessed_states
missing_path = os.path.join(base_dir, "states_to_learn.csv")
new_data = pd.DataFrame(missing_states, columns=["state"])
new_data.to_csv(missing_path, index=False)



screen.exitonclick()


screen.exitonclick()