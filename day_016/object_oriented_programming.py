# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


from prettytable import PrettyTable
from replit import clear
clear()
table = PrettyTable()
table.add_column("Pokemon Name:", ["Pikachu", "Charizard"])
table.add_column("Type:", ["Electric", "Fire"])
table.align = 'l'

print(table)