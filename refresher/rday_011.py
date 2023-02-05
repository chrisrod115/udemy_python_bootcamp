"""
Welcome to my fucking blackjack game
brought to you by: chris
date: gtfo
"""
import random as rand

black_playing = True
black_dict = {
    "A": 11,
    "K": 10,
    "Q": 10,
    "J": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def card_generator():
    empty_container = []
    dict_key = list(black_dict.keys())
    rand_index = rand.randint(0, 12)
    for i in range(1):
        empty_container.append(dict_key[rand_index])
    return empty_container


def correct_checker(sum_d, sum_p):
    if sum_d == sum_p:
        print("push")
    elif sum_d < sum_p:
        print("winner")
    elif sum_d > sum_p:
        print("loser")


def hit_stay(direction):
    if direction == "hit":
        return card_generator()


def str_int_converter_dealer(deck1):
    converted_list = []
    for key in deck1:
        converted_list.append(black_dict[key])
    return converted_list


def str_int_converter_player(deck2):
    converted_list = []
    for key in deck2:
        converted_list.append(black_dict[key])
    return converted_list


# def comp_play(total_d):
#     """
#     dealer hits soft 17
#     """
#     dealer_empty_cont = []
#     while total_d < 17:
#         dealer_empty_cont.append(card_generator())
#     return dealer_empty_cont


def blackjack(playing):
    cards_computer = []
    cards_player = []
    if playing == "yes":
        for i in range(2):
            cards_computer += card_generator()
            cards_player += card_generator()
    else:
        exit()
    tot_d = sum(str_int_converter_dealer(deck1=cards_computer))
    tot_p = sum(str_int_converter_player(deck2=cards_player))
    print(f"{cards_computer}, {cards_player} {tot_d} {tot_p}")
    hitting = True
    while hitting:
        if tot_p > 21:
            print("lost")
            hitting = False
            continue
        hit_or_stay = str(input("Would you like to \"hit\" or \"stay\"?"))
        if hit_or_stay == "hit":
            cards_player += hit_stay(direction=hit_or_stay)
            tot_d = sum(str_int_converter_dealer(deck1=cards_computer))
            tot_p = sum(str_int_converter_player(deck2=cards_player))
            print(f"{cards_computer}, {cards_player} {tot_d} {tot_p}")
            continue
        else:
            tot_d = sum(str_int_converter_dealer(deck1=cards_computer))
            tot_p = sum(str_int_converter_player(deck2=cards_player))
            correct_checker(sum_d=tot_d, sum_p=tot_p)
            print(f"{cards_computer}, {cards_player} {tot_d} {tot_p}")
            hitting = False


while black_playing:
    wanna_play = str(input("Do you want to play blackjack? \"yes\" or \"no\"")).lower()
    if wanna_play == "yes":
        blackjack(playing=wanna_play)
    else:
        black_playing = False
