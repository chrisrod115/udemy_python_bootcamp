import random as rand
from replit import clear

clear()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_processor(letter_int, number_int, symbols_int):
    store_shuffle = []
    for i in range(letter_int):
        store_shuffle += rand.choice(letters)
    for i in range(number_int):
        store_shuffle += rand.choice(numbers)
    for i in range(symbols_int):
        store_shuffle += rand.choice(symbols)
    rand.shuffle(store_shuffle)
    return print(''.join(map(str, store_shuffle)))


operating = True
while operating:
    clear()
    print("\n\nPassword generator")
    let: int = int(input("How many letters you want!\n"))
    nums: int = int(input("How many numbers you want!\n"))
    syms: int = int(input("How many symbols you want!\n"))
    password_processor(letter_int=let, number_int=nums, symbols_int=syms)
    cont = input("Do you need another password? \"yes\" or \"no\"?").lower()
    if cont == "no":
        operating = False

