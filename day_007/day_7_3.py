#Step 3
from replit import clear
import random

from sympy import false
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
playing = True
count = word_length
while playing != False:
    guess = input("Guess a letter: ").lower()
    clear()
    #Check guessed letter
    def word_checker():
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter
    word_checker()
    if "_" in display:
        print(display)
        continue
    else:
        print(display)
        print("you win!")
    
