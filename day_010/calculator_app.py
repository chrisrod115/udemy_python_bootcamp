from replit import clear
import art


finished_calc = False

# Calculator functions
def addition(first_number,second_number):
    return first_number + second_number
def subtraction(first_number,second_number):
    return first_number - second_number
def multiplication(first_number,second_number):
    return first_number * second_number
def division(first_number,second_number):
    return first_number / second_number

def calculator_operation(operator_choice):
    if operator_choice == operation_dict["Addition"]:
        result = addition(first_number,second_number)
        return result
    elif operator_choice == operation_dict["Division"]:
        result = subtraction(first_number,second_number)
        return result
    elif operator_choice == operation_dict["Multiplication"]:
        result = (multiplication(first_number,second_number))
        return result
    elif operator_choice == operation_dict["Subtraction"]:
        result = (division(first_number,second_number))
        return result
    else:
        return "invalid"


# Dictionary of operations
operation_dict = {
    "Addition": "+",
    "Subtraction": "-",
    "Multiplication": "*",
    "Division": "/",
}
cont_dict = {
    "continue": "y",
    "clear": "n",
    "end": "x"
}

while not finished_calc:
    clear()
    print(art.logo)
    first_number = int(input("What is the first number: "))
    operator_choice = input(f"+\n-\n*\n/\nPick and operator: ")
    second_number = int(input("What is the next number: "))
    """
        for choice in operation_dict:
        if operator_choice == operation_dict[choice]:
    """
    print(calculator_operation(operator_choice))
            
    continue_option = input(f"Type 'y' to continue calculating with result , or type 'n' to start a new calculation and 'x' to end the program: ")

    if continue_option == cont_dict["continue"]: 
        calculator_operation(operator_choice)
    elif continue_option == cont_dict["clear"]:
        clear()
        first_number = int(input("What is the first number: "))
        operator_choice = input(f"+\n-\n*\n/\nPick and operator: ")
        second_number = int(input("What is the next number: "))
        calculator_operation(operator_choice)
    else:
        quit()

        
        
        
        