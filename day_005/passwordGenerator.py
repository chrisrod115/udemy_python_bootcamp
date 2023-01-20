import random

alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number_list = ['0','1','2','3','4','5','6','7','8','9']

symbol_list = ["!","@","#","$","&"]

print("welcome to the password generator!")
amount_of_letters = input("how many letters do you want in your password: ")

l_string = ""
for letters in range (int(amount_of_letters)):
    alpha_rand = random.randint(1,26)
    l_string += alpha_list[alpha_rand-1]

amount_of_symbols = input("how many symbols would you like: ")

s_string = ""
for symbols in range (int(amount_of_symbols)):
    symbol_rand = random.randint(1,5)
    s_string += symbol_list[symbol_rand-1]

amount_of_numbers = input("now how many numbers would you like: ")

n_string = ""
for numbers in range (int(amount_of_numbers)):
    num_rand = random.randint(1,10)
    n_string += number_list[num_rand-1]


result = l_string+s_string+n_string

str_var = list(result)
random.shuffle(str_var)
print (''.join(str_var))



