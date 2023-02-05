from replit import clear
import random as rand
from hangman_art import stages, logo
from hangman_words import word_list

clear()


def underscore_word(str_word):
    underscores = []
    for i in range(len(str_word)):
        underscores += "_"
    return underscores


hangman = True
while hangman:
    clear()
    print(logo)
    word = rand.choice(word_list)
    underscore_list = underscore_word(str_word=word)
    lives = len(stages) - 1
    while lives != 0:
        print(word)
        print(underscore_list)
        print(f"You have {lives} lives left!")
        guess = input("Guess a letter now!")
        if guess in underscore_list:
            print("Guess again")
        for index in range(len(word)):
            letter = word[index]
            if guess == letter:
                underscore_list[index] = guess
        print(f"{' '.join(underscore_list)}")
        if guess not in word:
            print("wrong, minus 1 life")
            lives -= 1
            if lives == 0:
                hangman = False

        if "_" not in underscore_list:
            print("winner")
            exit()
