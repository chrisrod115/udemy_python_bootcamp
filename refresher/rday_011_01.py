"""
Welcome to my fucking blackjack game
brought to you by: chris
date: gtfo
"""

import random as rand

black_playing = True
deck_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
rand.shuffle(deck_cards)


def calculate_total(hand):
    total = 0
    for card in hand:
        total += card
    for card in hand:
        if card == 11 and total > 21:
            total -= 10
            break
    return total


def print_winner(player_total, dealer_total):
    if player_total <= 21:
        if player_total > dealer_total or dealer_total > 21:
            print("You win!")
        elif dealer_total > player_total:
            print("Dealer Wins")
        else:
            print("Bust")
    else:
        print(f"Dealer wins! You bust with a total of {player_total}")

