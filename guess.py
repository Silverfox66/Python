import random

number = random.randint(1, 10)

guess = int(input("I'm thinking of a number between 1 and 10. What is it? "))

if(guess == number):
    print("Correct :)")
else:
    print("Incorrect :( The correct number is", number)