from secrets import choice
import logo as logo_art
from replit import clear
bidders = {}
def store_bidders(bid,name):
    bidders[name] = bid
    
still_bidding = True
while still_bidding != False:
    clear()
    print(logo_art.logo)
    user_name = input("what is your name: ")
    user_bid = input("what is your bid: ")
    other_bid = input("Any other bids? Type 'yes' or 'no': ")
    if other_bid == "yes":
        store_bidders(bid=user_bid,name=user_name)
        clear()
        continue
    elif other_bid == "no":
        store_bidders(bid=user_bid,name=user_name)
        max_bid = max(bidders, key = bidders.get)
        winner_amount = bidders[max_bid]
        print(f"\nThe highest bidder was: {max_bid} with a bid of {winner_amount}")
        still_bidding =False
    else: 
        print("Try again, this is not an option.")
        continue
    
            
            

        