symbol_list = ["!","@","#","$","&"]
print(str_number_list)
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
    n_string += str_number_list[num_rand-1]


result = l_string+s_string+n_string
print(f"your generated password is: {result}")