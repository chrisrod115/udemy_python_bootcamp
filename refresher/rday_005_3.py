import random as rand
from replit import clear

clear()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def rand_selector(str_char):
    return rand.randint(0, len(str_char))


store_letters:str = []
store_nums:str = []
store_syms:str = []
store_shuffle:str = []


operating = True
while operating:
    print("Welcome to the password Generator")
    len_letter: int = int(input(f"How many letters do you want?\n"))
    len_nums: int = int(input(f"How many numbers do you want?\n"))
    len_syms: int = int(input(f"How many symbols do you want?\n"))
    for i in range(len_letter):
        rand_letter = rand_selector(str_char=letters)
        store_letters += letters[rand_letter]
    for i in range(len_nums):
        rand_nums = rand_selector(str_char=numbers)
        store_letters += numbers[rand_nums]
    for i in range(len_letter):
        rand_syms = rand_selector(str_char=symbols)
        store_letters += symbols[rand_syms]
    store_shuffle = store_letters+store_nums+store_syms
    rand.shuffle(store_shuffle)
    print(''.join(map(str, store_shuffle)))
    operating = False
