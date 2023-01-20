# this was the first test run
""" 
# generate 2 user and 2 dealer cards
def deal_cards_generator ():

    first_card = random.choice(cards)
    second_card = random.choice(cards)

    dealer_card.append(first_card)
    dealer_card.append(second_card)
    return dealer_card

def player_hand_generator ():

    pfirst_card = random.choice(cards)
    psecond_card = random.choice(cards)

    player_hand.append(pfirst_card)
    player_hand.append(psecond_card)
    return player_hand



generate = deal_cards_generator() #generate the first set of dealers cards
generate_player = player_hand_generator()
playing = True

while playing:
    dealer_showing = dealer_card[0]
    print(f"Your cards are: {player_hand}")
    print(f"Dealer is showing: {dealer_showing}")
    yayornay = (input("Type hit or stay: "))
    if yayornay == "hit":
        add_card = player_hand.append(random.choice(cards))
        continue
    elif yayornay == "stay":
        print(f"Your hand is {player_hand}")




    playing = False
    """