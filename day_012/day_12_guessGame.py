from replit import clear
from what_are_the_odds import logo
import random
clear()
lives = 10 
num_list = list(range(1,101))
hidden_num = []
game_mode = {
    "easy": 10,
    "hard": 5,
}
def store_num():
    hidden_num.append(random.choice(num_list))
store_num()

user_input_mode = str(input("Pick a mode to play: 'easy' or 'hard': "))
if user_input_mode == "hard":
    lives = game_mode["hard"]
else:
    lives == game_mode["easy"]

    
playing = True
while playing != False:
        print(logo)
        guess = int(input("Guess a number: "))
        if lives ==0:
            print(f"Lives left: {lives}")
            playing = False
        elif guess == hidden_num[0]: 
            print("OMG you found the hidden number!!!")
            playing = False        
        elif guess != hidden_num:
            clear()
            print(f"Lives left: {lives}")
            lives -= 1
    
    
    
    
        
        
        
    