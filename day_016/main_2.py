
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_report = CoffeeMaker()


using_machine = True
while using_machine != False:
    user_input = input("What would you like: (Latte/Cappuccino/Espresso)? ").lower()

    if user_input == "end":
        using_machine == False
    elif user_input == "report":
        print(machine_report.report())

            