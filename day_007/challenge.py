#Step 1 
from dis import dis
import random
from re import S, T
from turtle import pos
word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
"""
# This was my implementation of challenge 1

def rand_word_gen():
    choose_word = random.choice(word_list)
    print(choose_word)
    print("Welcome to hangman!")
    guess = input("Choose a lowercase letter: ")
    while True:    
        if guess.islower() == True: # Check letter
            for letter in choose_word:
                for guess_letter in guess:
                    if guess == letter:
                        print(f"")
                    else: 
                        print("False")
            return
        else: 
            guess = input("Not lowercase, try again: ").islower()
            continue

    

rand_word_gen()
"""
# Solution and correct implementation of challenge

chosen_word = random.choice(word_list)
print(f"This was the chosen word: {chosen_word}")
end_of_game = False
num_lives = 6

under_scores = []
# create a list of underscores
for idx in range(len(chosen_word)):
    under_scores += "_"

# Check if player won   
while not end_of_game:

    guess = input("Guess a letter: ").lower()
    # check if letter is in word
    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            under_scores[position] = guess
            print(f"You have {num_lives} left.")
            print(f"{stages[num_lives]}")

    if guess not in chosen_word:
        num_lives -= 1
        print(f"Number of lives left: {num_lives}")
        print(f"{stages[num_lives]}")
    print(under_scores)

    # check if player won
    if "_" not in under_scores:
        end_of_game = True
        print ("you win")
    
    # check if number of lives is not zero
    if num_lives == 0:
        end_of_game = True
        print("you lose")








