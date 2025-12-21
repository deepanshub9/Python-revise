"""
WORKFLOW IN PROJECT Rock_Paper_Scissor

1- Input from user(Rock, Paper, Scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result Print

Cases:
A- Rock
Rock - Rock = Tie
Rock - Paper = Paper Win
Rock - Scissor = Rock Win

B- Paper
Paper - Paper = Tie
Paper - Rock = Paper Win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = Tie
Scissor - Rock = Rock Win
Scissor - Paper = Scissor Win
"""

import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor= ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("It's a tie!")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper cover Rock. Computer wins!")
    else:
        print("Rock crushes Scissor. You win!")
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cut paper. Computer wins!")
    else:
        print("Paper cover Rock. You win!")
elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock crushes Scissor. Computer wins!")
    else:
        print("Scissor cut paper. You win!")
        