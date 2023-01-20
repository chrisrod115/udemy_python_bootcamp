import random
"""
Instructions:

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.


There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g. 1 means Heads 0 means Tails
"""
playing = True

while playing != False:
    
    action = (input("Type \"roll\" to flip a coin, or type \"stop\" to quit: "))
    
    if action == "roll":
        heads_or_tails = random.randint(0,1)
        if heads_or_tails == 0:
            print("Heads")
            continue
        elif heads_or_tails == 1: 
            print("Tails")
            continue
        else:
            print("invalid option try again\n") 
            exit
    elif action =="stop":
        print("game over have a nice day! \n")
        playing = False
        exit
