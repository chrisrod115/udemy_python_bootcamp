"""
This program is a BlackJack gambling game. 
"""
import random
from art import logo
from replit import clear
clear()
cards = {
    "user_cards": [],
    "dealer_cards": [],
    "deck": [1,2,3,4,5,6,7,8,9,10,11]
}        

def shuffle_init_cards():
    clear()
    cards["user_cards"] = []
    cards["dealer_cards"] = []
    num_cards = 2
    for i in range(num_cards):
        cards["user_cards"].append(random.choice(cards["deck"]))
    for i in range(num_cards):
        cards["dealer_cards"].append(random.choice(cards["deck"]))
    print(logo)
    print("Your cards are: ", cards["user_cards"])
    print(f"Dealer is showing: ",cards["dealer_cards"][1])
    
def hit_or_stay():
    user_input_hit_or_stay = input("\nType 'hit' or 'stay': ")
    if user_input_hit_or_stay == "hit":
        add_one_card = random.choice(cards["deck"])
        cards["user_cards"].append(add_one_card)
        print(cards["user_cards"])
        hit_or_stay()
    elif user_input_hit_or_stay == "stay":
        return
        
def winner_or_looser():
    if sum(cards["user_cards"]) > 21: 
        print(f"\nYou went over 21 {cards['user_cards']} you loose!")
        print("Dealers cards: ", cards["dealer_cards"])
    elif sum(cards["dealer_cards"]) > 21: 
        print(f"Dealer busts {cards['dealer_cards']} you are the winner!")
    else:
        if sum(cards["user_cards"]) > sum(cards["dealer_cards"]):
            print("\nYou are the winner your cards are: ",cards["user_cards"])
            print("Dealers cards: ", cards["dealer_cards"])
        elif sum(cards["dealer_cards"]) > sum(cards["user_cards"],):
            print("\nyour cards are:  ", cards["user_cards"])
            print("sorry you lost! dealer cards are: ", cards["dealer_cards"])
        else:
            print("You pushed, the game is a tie!") 
            
def dealer_hits_16():
    add_a_card = random.choice(cards["deck"])
    cards["dealer_cards"].append(add_a_card)
    winner_or_looser()      

playing = True
while playing != False:
    wanna_play = input("\nDo you want to play a blackjack game 'y' or 'n': ")
    if wanna_play == 'y':
        shuffle_init_cards()
        hit_or_stay()
        #while sum(cards["dealer_cards"]) < 16:
         #   dealer_hits_16()
        winner_or_looser()
    elif wanna_play == 'n':
        clear()
        print("Goodbye!")
        playing = False
    else:
        print("Not an option try again")
        continue
        

