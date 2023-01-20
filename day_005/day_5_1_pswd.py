import random as rnd
import string
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number_list = ['0','1','2','3','4','5','6','7','8','9']
symbol_list = ["!","@","#","$","&"]

alp_letters = input("How many letters would you like?")
num_vals = input("how many numbers would you like? ")
symbs = input("how many symbols would you like? ")

l_string = ""
for i in range(int(alp_letters)):
    l_range = rnd.randint(0,26)
    l_string += alpha_list[l_range-1]

n_string = ""
for i in range(int(num_vals)):
    n_rand = rnd.randint(0,9)
    n_string += number_list[n_rand-1]

s_string = ""
for i in range(int(symbs)):
    s_rand = rnd.randint(0,4)
    s_string += symbol_list[s_rand-1]

result = l_string+n_string+s_string
str_result = list(result)
rnd.shuffle(str_result)
print(''.join(str_result))
