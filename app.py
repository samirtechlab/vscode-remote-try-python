#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write "hello world" in the console
print("hello world")

from random import randint

score = {"player": 0, "computer": 0}

while True:
    user_choice = input("Enter rock, paper, or scissors: ")
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid entry. Please try again.")
        continue

    computer_choice = randint(0, 2)
    if computer_choice == 0:
        computer_choice = "rock"
    elif computer_choice == 1:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"
    print("Computer chose " + computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
            score["player"] += 1
        else:
            print("Computer wins!")
            score["computer"] += 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
            score["player"] += 1
        else:
            print("Computer wins!")
            score["computer"] += 1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
            score["player"] += 1
        else:
            print("Computer wins!")
            score["computer"] += 1

    print("Score: Player {} - {} Computer".format(score["player"], score["computer"]))

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thanks for playing!")
        break
    user_choice = input("Enter rock, paper, or scissors: ")
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid entry. Please try again.")
        continue

    computer_choice = randint(0, 2)
    if computer_choice == 0:
        computer_choice = "rock"
    elif computer_choice == 1:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"
    print("Computer chose " + computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("Computer wins!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thanks for playing!")
        break














