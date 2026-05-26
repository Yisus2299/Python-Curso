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
        title=f"{len(guessed_states)}/50 estados correctos",
        prompt="Cual es el nombre de otro estado?"
    )
# If answe_state es uno de los estados dentro de todos los 50_stados.csv
 #if ellos tienen razon, crea una turtle para escribir el nombre de los estados en las coordenasdas X y ponerlo

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
                    

# estados para aprender en un csv

missing_states = [state for state in all_states if state not in guessed_states]
#es decir:     estados para los estados en todos los estados si el estado no esta en los estados adivinados
missing_path = os.path.join(base_dir, "states_to_learn.csv")
new_data = pd.DataFrame(missing_states, columns=["state"])
new_data.to_csv(missing_path, index=False)









screen.exitonclick()