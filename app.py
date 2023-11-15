#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# initialize the score variable
score = 0
# initialize the number of turns variable
turns = 0

# create an array with 3 options : rock, paper and scissors
options = ["rock", "paper", "scissors"]

# write 'Welcome to the game' to the console
print("Welcome to the game !")

# initialize the user input variable
user_input = "y"

# start the game loop
while (user_input == "y"):

    # increment the number of turns variable
    turns += 1

    # initialize the user input variable
    user_input = ""
    # ask for the user input until it's a valid option from the array
    while (user_input not in options):
        # get the user input in a variable
        user_input = input("Choose rock, paper or scissors: ")
        # transform the user input to lowercase
        user_input = user_input.lower()
        # if the user input is not valid, print an error message
        if (user_input not in options):
            print("Invalid option. Please try again.")

    # write the user input to the console
    print("You typed: " + user_input)

    # create a computer_input variable with a random option from the array
    computer_input = random.choice(options)

    # write the computer input to the console
    print("Computer typed: " + computer_input)

    # if the user input is the same as the computer input, write 'Tie' to the console
    if (user_input == computer_input):
        print("Tie")
    # if the user input is rock and the computer input is scissors, write 'You won' to the console
    elif (user_input == "rock" and computer_input == "scissors"):
        print("You won")
        # increment the score variable
        score += 1
    # if the user input is paper and the computer input is rock, write 'You won' to the console
    elif (user_input == "paper" and computer_input == "rock"):
        print("You won")
        # increment the score variable
        score += 1
    # if the user input is scissors and the computer input is paper, write 'You won' to the console
    elif (user_input == "scissors" and computer_input == "paper"):
        print("You won")
        # increment the score variable
        score += 1
    # if the user input is rock and the computer input is paper, write 'You lost' to the console
    elif (user_input == "rock" and computer_input == "paper"):
        print("You lost")
        # decrement the score variable
        score -= 1
    # if the user input is paper and the computer input is scissors, write 'You lost' to the console
    elif (user_input == "paper" and computer_input == "scissors"):
        print("You lost")
        # decrement the score variable
        score -= 1
    # if the user input is scissors and the computer input is rock, write 'You lost' to the console
    elif (user_input == "scissors" and computer_input == "rock"):
        print("You lost")
        # decrement the score variable
        score -= 1

    # write the score to the console
    print(f"Score: {score}")

    # Ask the user if he wants to play again
    user_input = input("Do you want to play again? (y/n) ")

# Print final score and good bye message
print(f"Final score: {score}")
print("Good bye !")
