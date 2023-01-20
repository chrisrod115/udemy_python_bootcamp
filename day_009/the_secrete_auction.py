from replit import clear
import Day_11_Capstone.art as art 


print(art.logo)
print("Welcome to the secret auction program.")


bidding_finished = False



def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder] 
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} the winning bid is {highest_bid}.")


while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    end_of_bid = input("Are there any other bidders? Type 'yes' or 'no'. ")
    bids = {}   
    bids[name]= bid
    
    if end_of_bid == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
        
        
        
    elif end_of_bid == 'yes':
        clear()







