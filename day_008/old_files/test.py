"""


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
  'w', 'x', 'y', 'z']

# Poject setup: 1. alphabet list 2. prompts 3. empty sting setup 
#               4. variable to store an int(input())

# user_string = int(input("Type 1 to encypt or 2 to decrypt: "))
# Decision function: 1. decide from encode/decode. 


# if user_string == 1:
#     encrypt_decision = str(input("Type your message: "))
# elif user_string ==2: 
#     decrypt_decision = str(input("Type your message"))
# else: 
#     print("Error restart program")
    

# Function "encode":1. prompt user to input a string str(input()) 
#                   2. prompt user to enter a shift number int(input()) 
#                   3. shift user message to appropriate letter in alpha_bet list
#                       a. for loop to fing the position of the letter in the list
#                       b. index the list to the shift number of the list. 
#                   4. finally print()

def encode_string():
    
    encrypt_decision = str(input("Type your message: "))
    list_encode = list(encrypt_decision)
    shift_number = int(input("Type your shift number: "))
    match_str = " "

    for i in list_encode:
        for a in alphabet:
            if i == a:
                match_str == a[shift_number]
    print(match_str)

encode_string()



# Function "decode":1. prompt user to input a string str(input()) 
#                   2. prompt user to enter a shift number int(input()) 
#                   3. shift user message to appropriate letter in alpha_bet list
#                       a. for loop to fing the position of the letter in the list
#                       b. index the list to the shift number of the list. 
#                   4. finally print()


"""
import numpy as np

alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
  'a', 'b', 'c', 'd', 'e', 'f',
 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(np.size(alphabet))