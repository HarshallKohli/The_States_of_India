import turtle             # helps bring up the image
import pandas             # helps read through the csv file

screen = turtle.Screen()                            # setting up the screen
screen.title("The Game of Indian States")

image = "indianmap.gif"
screen.screensize(900, 1000)
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("indian_states_coordinates.csv")
all_states = (data.States.to_list())   # a list is made of all the states from column called States
guessed_states = set()                   # initially, guessed states =0 -->empty set at first gradually filled


while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 states correct.",
                                    prompt="What's another states name?").title()
    # guessed_states = set()
    # guessed_states.add(answer_state)

    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]          # on exit, the states you couldn't guess will be filled in missing_states list
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        # guessed_states = set()
        guessed_states.add(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.States == answer_state]
        t.goto(int(state_data.X.iloc[0]), int(state_data.Y.iloc[0]))
        t.write(answer_state)

