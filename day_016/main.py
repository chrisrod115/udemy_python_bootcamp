from importlib.resources import is_resource
from pprint import isreadable
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



report_1 = MoneyMachine()
report_2 = CoffeeMaker()
menu = Menu()
order = menu.get_items()
coffee_machine_on = True



while coffee_machine_on != False:
    user_input = input(f"​What would you like? ({order}): ")
    if user_input == "report":
        report_1.report()
        report_2.report()
    elif user_input == "end":
        coffee_machine_on = False
    else: 
        drink = menu.find_drink(order_name=user_input)
        if report_2.is_resource_sufficient(drink)and report_1.make_payment(drink.cost):
            report_2.make_coffee(order = drink)
        else:
            coffee_machine_on = False