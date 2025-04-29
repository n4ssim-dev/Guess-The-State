import turtle
import pandas

score = 0

# Importe le fichier des états
file = pandas.read_csv('50_states.csv')
file_us_state = list(file.state)

# Créer un dictionnary avec un état associé à une coordonnée
us_states = {}

for index, row in file.iterrows():
    us_states[row["state"]] = (row["x"], row["y"])

# Création de l'écran
screen = turtle.Screen()
screen.title("Guess The States")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
turtle.penup()

guessed_states = []
non_guessed_states = us_states.copy()  # Create a copy to modify


def give_question():
    global score, non_guessed_states

    while score < 50:
        guessed_state = screen.textinput(
            title=f"Score : {score} / {len(file_us_state)}\nGuess a state",
            prompt="Guess the name of a U.S. State :"
        )

        if not guessed_state:
            break

        guessed_state = guessed_state.title()

        # coupe le jeu
        if guessed_state == "Exit":
            print("You stopped ...")
            non_guessed_states = [state for state in file_us_state if state not in guessed_states]
            print("States you missed:", non_guessed_states)

            # Save to CSV
            pandas.DataFrame(non_guessed_states, columns=["state"]).to_csv("states_to_learn.csv")
            break

        # Ajoute un état deviné à la carte
        if guessed_state in us_states and guessed_state not in guessed_states:
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()

            x_location = us_states[guessed_state][0]
            y_location = us_states[guessed_state][1]
            location = (x_location, y_location)

            t.goto(location)
            t.write(guessed_state)

            score += 1
            guessed_states.append(guessed_state)

        if score == 50:
            print("You won!")
            break


give_question()
turtle.mainloop()