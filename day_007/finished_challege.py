#Step 1 
from replit import clear
import random
word_list = ["lorena", "maria", "sam smith","sylvia"]
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
# Solution and correct implementation of challenge
chosen_word = random.choice(word_list)
print("Do you wanna play a game?")
end_of_game = False
num_lives = 6
under_scores = []

# create a list of underscores
for idx in range(len(chosen_word)):
    under_scores += "_"

# Check if player won   
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
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