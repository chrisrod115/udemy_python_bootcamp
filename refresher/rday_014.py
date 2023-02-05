import higher_lower_data
import random as rand
from replit import clear


def rand_dict_generator():
    return rand.choice(higher_lower_data.data)


def account_formatter(account):
    name = account['name']
    desc = account['description']
    country = account['country']
    return f"{name}, {desc}, from {country}"


def game_checker(account1, account2, user_choice):
    if user_choice == 'higher':
        if account2['follower_count'] > account1['follower_count']:
            return True
        else:
            return False
    elif user_choice == 'lower':
        if account2['follower_count'] < account1['follower_count']:
            return True
        else:
            return False


def game():
    print("Welcome to the higher lower game!")
    score = 0
    playing = True
    while playing:
        clear()
        account_2 = rand_dict_generator()
        choosing = True
        while choosing:
            clear()
            account_1 = account_2
            account_2 = rand_dict_generator()
            if account_2 == account_1:
                account_1 = rand_dict_generator()
            print(f"A: {account_formatter(account=account_1)}\n")
            choice = str(input(f"B: Does \'{account_formatter(account=account_2)}\' have higher or lower followers? "
                               f"\nType higher or"
                               f" lower: ")).lower()
            check = game_checker(account_1, account_2, choice)
            if check:
                clear()
                score += 1
                print(score)
                continue
            else:
                clear()
                print(f"You lost, final score: {score}")
                exit()


play = True
while play:
    wanna_play = str(input("do you want to play? \nyes or no: ")).lower()
    if wanna_play == 'yes':
        game()
    else:
        exit()
