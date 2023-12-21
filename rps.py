'''
Rock beats scissors
Paper beats rock
Scissors beats paper

Rock = 1
Paper = 2
Scissors = 3
'''
import random

def get_choice_name(choice):
    name = ""
    if(choice == 1):
        name = "Rock"
    elif(choice == 2):
        name = "Paper"
    else:
        name = "Scissors"
    return name

def get_winner(user_choice, computer_choice):
    winner = ""
    if(user_choice == 1 and computer_choice == 3):
        winner = "user"
    elif(user_choice == 2 and computer_choice == 1):
        winner = "user"



while(True):
    print("Choose rock, paper or scissors by entering the apropriate number.")
    print("Rock = 1")
    print("Paper = 2")
    print("Scissors = 3")
    user_choice = int(input("Enter your choice: "))

    if(user_choice < 1 or user_choice > 3):
        print("You entered an invalid input! Please re-enter.")
        print()
        print()
        continue

    computer_choice = random.random(1, 3)

    print()
    print()

    user_name = get_choice_name(user_choice)
    computer_name = get_choice_name(computer_choice)

    print("You chose", user_name)
    print("The computer chose", computer_name)

    print()
