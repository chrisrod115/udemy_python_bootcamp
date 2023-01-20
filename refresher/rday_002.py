#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

from replit import clear
clear()

def tip(price ,tip,split):
    """Returns total cost on the reciept

    Args:
        price (int): Food cost in US dollars
        tip (float): Percentage/decimal

    Returns:
        float: The total price of the meal with tip included
    """
    return (price + (price*(tip/100)))/split
    
    
run_calc = True
while run_calc != False:
    clear()
    print("Hello welcome to the split calculator!\n")
    meal_cost = int(input("What is the total price of the meal with tax? \n"))
    tip_cost = int(input("What percentage tip are you going to leave? 10%,15%, and 20%\n"))
    num_split = int(input("How many people are you split? \n"))
    price_per = tip(price=meal_cost,tip= tip_cost,split= num_split)
    
    print(f"\nThe total cost of the meal per person is ${price_per}\n")
    check_another = input("Would you like to check another split; type 'yes' or 'no'? ")
    if check_another != 'yes':
        run_calc = False

    
    
    
    
    
    
