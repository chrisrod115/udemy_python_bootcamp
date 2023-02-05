"""
Welcome to the guessing game!
"""
import random as rand


def difficulty(diff):
    if diff == "hard":
        return 5
    else:
        return 10


def close_or_not(guess_num, actual_value):
    if guess_num < 100:
        if guess_num > actual_value:
            print("Too high, try again!")
            return 1
        elif guess_num < actual_value:
            print("Too low, try again!")
            return 1
        else:
            print("Correct guess, good job!")
    else:
        print("Not an option try a number from 1 to 100!")
        return 1


def guessing_game():
    print("Welcome to the guessing game!")
    print("I'm thinking of a number from 1 to 100.")
    rand_int = rand.randint(1, 100)
    print(f"psst. the number is {rand_int}")
    how_diff = str(input("Choose a difficulty. Type \'easy\' or \'hard\':\n"))
    lives = 0
    lives += difficulty(diff=how_diff)
    while lives != 0:
        print(f"You have: {lives} lives left!")
        guess = int(input("Type a number:\n"))
        if close_or_not(guess_num=guess, actual_value=rand_int) == 1:
            lives -= 1
        else:
            break


guessing = True
while guessing:
    playing = str(input("\nDo you want to play a guess game?\"yes\" or \"no\"?:\n"))
    if playing == "no":
        guessing = False
    else:
        guessing_game()
