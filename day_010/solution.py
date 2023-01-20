from replit import clear

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))


    for value in operations:
        print(value)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        f_answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {f_answer}")

        if input(f"Type 'y' to continue calculating with {f_answer} or type 'n' to start new calculation: ") == "y":
            num1 = f_answer
        else: 
            should_continue = False
            clear()
            calculator()
calculator()

