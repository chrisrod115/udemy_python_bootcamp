""" 
Initial Program: 
#1. Create a greeting for your program.
print("Hello, Welcome to the Band Name Generator. ")
#2. Ask the user for the city that they grew up in.
name_city = input(f"What's the name of the city you grew up in? ")
#3. Ask the user for the name of a pet.
name_pet = input(f"What's the name of your pet? ")
#4. Combine the name of their city and pet and show them their band name.
print(f"Congrats your brand name is: {name_city + ' ' + name_pet}")
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end
"""


# My improvements: 

from replit import clear
clear()

generating = True

while generating != False:
    clear()
    #1. Create a greeting for your program.
    print("Hello, Welcome to the Band Name Generator. ")
    #2. Ask the user for the city that they grew up in.
    name_city = input(f"What's the name of the city you grew up in? ")
    #3. Ask the user for the name of a pet.
    name_pet = input(f"What's the name of your pet? ")
    #4. Combine the name of their city and pet and show them their band name.
    print(f"\nCongrats your brand name is: {name_city + ' ' + name_pet}\n")
    
    #Are you still generating band names?
    still_gen = input("Are you still generating band names; yes or no? ").lower   
    if still_gen != "yes":
        generating = False
    print("Thanks for generating band names\nrun program again to restart")