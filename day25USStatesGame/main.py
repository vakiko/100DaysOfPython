from os import stat_result
import turtle
import pandas

turt = turtle.Turtle()
turt.hideturtle()
turt.penup()

data = pandas.read_csv("50_states.csv")
states = data.state
screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
guessed_states = []
missed_states = []
turtle.shape(image)
while len(guessed_states) < 50: 
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guessed States", prompt="Guess another state's name:")
    if answer_state in str(states):
        state_row = data[data.state == answer_state]
        turt.goto(int(state_row.x), int(state_row.y))
        turt.write(answer_state)
        guessed_states.append(answer_state)
    if answer_state == 'exit':
        break
print(states)
for state in states:
    if state not in guessed_states:
        print(state)
        missed_states.append(state)
new_data = pandas.DataFrame(missed_states)
new_data.to_csv("missed_states_to_review.csv")
