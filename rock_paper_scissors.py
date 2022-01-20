import numpy as np
from numpy import random

user = 0
bot = 0

options = np.array(["rock", "paper", "scissors"])

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    
    computer_pick = random.choice(["rock", "paper", "scissors"])
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user += 1
    
    elif ((user_input == "rock" and computer_pick == "rock") or (user_input == "paper" and computer_pick == "paper" or (user_input == "scissors" and computer_pick == "scissors"))):
        print("Draw")
        

    else:
        print("You lost!")
        bot += 1

print("Game Over!")
print("Your score is", user)
