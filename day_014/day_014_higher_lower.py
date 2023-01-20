"""
_To-Do List_
    1. we need a random generator
    2. a dictionary of items with: --> {"strings": int_value} --> (finished)
    3. prompt user to choose either higher or lower: user a dictionary {"higher": 1, "lower": 2} --> (done)
    4. if the answer is correct yes or no?
    5. answer correct = yes --> .pop the value from the dictionary
        1. continue the game 
    6. answer incorrect - no --> print("ouch you lost lol")
"""
import random
from game_data import data
from replit import clear
from art import logo,vs
clear()
higher_lower = {
    "A": "Higher",
    "B": "Lower",
}
comp_a_gen = random.choice(data)
comp_b_gen = random.choice(data)
def checker(comp):
    if higher_lower["A"] == comp:
        if comp_a_gen == comp_b_gen:
            return "go"
        elif comp_a_gen != comp_b_gen:
            return "stop"
        else:
            return "not an option"
    elif higher_lower["B"] == comp:
        return "stop"
    
playing = True
while playing != False:
    print(logo)
    print(f"Compare A: {comp_a_gen['name']}, a {comp_a_gen['description']},from {comp_a_gen['country']}")
    print(vs)
    print(f"Compare B: {comp_b_gen['name']}, a {comp_b_gen['description']},from {comp_b_gen['country']}")
    user_choice = input(str("Who has more followers: 'A' or 'B'? ")).upper()
    checker(comp= user_choice)
    if checker(comp=user_choice) == 'go':
        continue
    elif checker(comp=user_choice) == 'stop':
        playing = False
    elif checker(comp = user_choice) == 'not an option':
        print('this is not an option')
