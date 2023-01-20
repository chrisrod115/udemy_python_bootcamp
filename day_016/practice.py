"""from turtle import *

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

for i in range(100):
    timmy.speed(10)
    timmy.fd(2)
    timmy.backward(10)
    timmy.circle(50,20,1)
    
    

my_screen = Screen()

exit = my_screen.exitonclick()
"""

from prettyTables import Table

new_table = Table()

fire_type = new_table.add_column('Fire',["Charmander","Dragonite"])
water = new_table.add_column('Water',["Squirtle","Blastois"])
print(new_table)
