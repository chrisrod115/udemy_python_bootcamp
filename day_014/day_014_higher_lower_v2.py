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
from unicodedata import name 
from art import logo,vs
from game_data import data
from replit import clear


def data_format(compare):
    """The following function imports a dicitonary 
    and separates the data for use of either choice a
    or choice b of the data

    Args:
        compare (dict): dictionary from the game_data file

    Returns:
        string: The string that is returned is a name, description, and a country.
    """
    name = compare['name']
    description = compare ['description']
    country = compare['country']
    return f"{name}, a {description}, from {country}"


def checker(comp_a,comp_b,guess):
    """The following function will compare two follower counts from the 
    game_data python file. 

    Args:
        comp_a (int): Follower count for the first user
        comp_b (int): Follower count for the first user
        guess (string): Either an upper 'A' or 'B'

    Returns:
        bool: Returns either True or False
    """
    if comp_a>comp_b:
        return guess == "A"
    else:
        return guess == "B"
    
    
count = 0
playing = True
while playing != False:
    
    compare_a = random.choice(data)
    compare_b = random.choice(data)
    follower_a = compare_a['follower_count']
    follower_b = compare_b['follower_count']
    if compare_a == compare_b:
        compare_b = random.choice(data)
    print(logo)
    print(f"Compare A: {data_format(compare=compare_a)}")
    print(vs)
    print(f"Compare B: {data_format(compare=compare_b)}")
    user_choice = input("Who has more followers: Type 'A' or 'B'? ").upper()
    if checker(comp_a=follower_a,comp_b=follower_b,guess=user_choice) == True:
        count += 1
        clear()
        print(f"Correct! Your score is: {count}")
        
    else: 
        print("You lost sorry!")
        playing = False

