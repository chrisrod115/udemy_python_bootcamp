#Password Generator Project
import random as rand
from replit import clear
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:

def rand_gen(let,sym,nums):
    """Takes three inputs; letters, symbols, and numbers and generates a random password

    Args:
        let (int): Number of letters 
        sym (int): Number of symbols 
        nums (int): Number of numbers 

    Returns:
        string: random password with given amount of letters, symbols, and numbers.
    """
    password = ""
    for i in range(let):
        random_choice_let = rand.randrange(len(letters))
        password += letters[random_choice_let]
    for i in range(sym):
        random_choice_sym = rand.randrange(len(symbols))
        password += symbols[random_choice_sym]
    for i in range(nums):
        random_choice_num = rand.randrange(len(symbols))
        password += numbers[random_choice_num]

    pass_rand = ''.join(rand.sample(password,len(password)))
    return pass_rand
    

generator = True 
while generator != False: 
    clear()
    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))    
    letters_return = rand_gen(let=nr_letters,sym=nr_symbols,nums=nr_numbers)
    print(f"This is your password: {letters_return}\n")
    another = input(f"Would you like another password? yes or no: ").lower()
    if another != "yes":
        generator = False