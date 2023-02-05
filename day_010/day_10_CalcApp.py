from ast import operator
from replit import clear
from art import logo

""" Initial attempt at creating a calculator application.
def adding(num1,num2):
    adding_result = num1+num2
    return print(adding_result)
def subtracting(num1,num2):
    sub_result = num1-num2
    return sub_result
def multiplying(num1,num2):
    mult_result = num1*num2
    return mult_result
def dividing(num1,num2):
    div_result = num1/num2
    return div_result
calculating = True
while calculating != False: 
    clear()
    print(logo)
    user_first_num = input("First number: ")
    user_second_num = input("Second number: ")
    operating_symbol = input("Operator type:\n'+'\n'-'\n'*'\n'/'\nto quit 'end'")
    if operating_symbol == "+":
        adding(num1=user_first_num,num2=user_second_num)
        continue
    elif operating_symbol == "-":
        subtracting(num1=user_first_num,num2=user_second_num)
        continue
    elif operating_symbol == "*":
        multiplying(num1=user_first_num,num2=user_second_num)
        continue
    elif operating_symbol == "/":
        dividing(num1=user_first_num,num2=user_second_num)
        continue
    elif operating_symbol == "end":
        print("goodbye!")
        calculating = False
    else:
        print("This is not an option try again!")
        stop_calc = input("Type 'end' to quit or 'start' to continue: ")
        if stop_calc == "end":
            calculating = False
        else:
            continue
            """


def add(a, b):
    return f"Result is {a + b}"


def subtract(a, b):
    return f"Result is {a - b}"


def multiply(a, b):
    return f"Result is {a * b}"


def divide(a, b):
    return f"Result is {a / b}"


calculating = True
while calculating:
    clear()
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    print("Choose and operator:")

    operations = {
        "+": add(a=num1, b=num2),
        "-": subtract(a=num1, b=num2),
        "*": multiply(a=num1, b=num2),
        "/": divide(a=num1, b=num2),
    }
    for i in operations:
        print(i)
    user_operator = input("\nChoice: ")
    print(operations[user_operator])
    calc_again = input("Calculate again? 'yes' or 'no': ")
    if calc_again == "yes":
        continue
    elif calc_again == "no":
        calculating = False
    else:
        print("try again")
