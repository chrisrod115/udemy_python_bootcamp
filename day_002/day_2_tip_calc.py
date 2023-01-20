#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

print("\nWelcome to the tip calculator!")
bill = float(input("What was the total bill: "))
split = float(input("How many people to split the bill? ")) 
percentage = float(input("What percentage tip would you like to give? 10,12, or 15? "))

def tip_calc():
    val = 100
    result = (bill/split) * (val+percentage)/100
    return result

# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048
print("\nEach person should pay",tip_calc())


# Redo 1/20/23

"""print("Split generator")
bill = float(input("Enter total bill now! \n"))
peop = float(input("Enter how many people:\n"))
tip = float(input("Enter tip percent now! 10, 12, or 15%\n"))

def tip_calculator():
    return (bill*(1+(tip/100)))/peop

print(f"Bill per people is now! ${tip_calculator():.2f}")"""

