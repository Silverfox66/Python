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
    elif(choice == 3):
        name = "Scissors"
    elif(choice == 4):
        name = "Lizard"
    else:
        name = "Spock"
    return name

def get_winner(user_choice, computer_choice):
    winner = ""

    if(user_choice == 1 and computer_choice == 3):
        winner = "user"
    elif(user_choice == 2 and computer_choice == 1):
        winner = "user"
    elif(user_choice == 3 and computer_choice == 2):
        winner = "user"
    elif(user_choice == computer_choice):
        winner = None
    elif(user_choice == 1 and computer_choice == 4):
        winner = "user"
    elif(user_choice == 4 and computer_choice == 5):
        winner = "user"
    elif(user_choice == 5 and computer_choice == 3):
        winner = "user"
    elif(user_choice == 3 and computer_choice == 4):
        winner = "user"
    elif(user_choice == 4 and computer_choice == 2):
        winner = "user"
    elif(user_choice == 2 and computer_choice == 5):
        winner = "user"
    elif(user_choice == 5 and computer_choice == 1):
        winner = "user"
    else:
        winner = "computer"

    return winner

Wins = 0
Losses = 0

while(True):
    print("Choose rock, paper or scissors by entering the apropriate number.")
    print("Rock = 1")
    print("Paper = 2")
    print("Scissors = 3")
    print("Lizard = 4")
    print("Spock = 5")
    user_choice = int(input("Enter your choice: "))

    if(user_choice < 1 or user_choice > 5):
        print("You entered an invalid input! Please re-enter.")
        print()
        print()
        continue

    computer_choice = random.randint(1, 5)

    print()
    print()

    user_name = get_choice_name(user_choice)
    computer_name = get_choice_name(computer_choice)

    print("You chose", user_name)
    print("The computer chose", computer_name)

    print()



    winner = get_winner(user_choice, computer_choice)
    if(winner == "user"):
        print("You win!")
        Wins += 1
        print(f"You: {Wins}, Losses: {Losses}")
    elif(winner == "computer"):
        print("You lose!")
        Losses += 1
        print(f"You: {Wins}, Losses: {Losses}")
    else:
        print("The game was a draw! Choose again!")
        continue
    
    print()
    print()

    print("Do you want to play again?")
    choice = input("Enter Y for yes or N for no: ")    
    print()
    print()
    if(choice == 'Y'):
        continue
    else:
        print("Thanks for playing!")
        break