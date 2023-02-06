from coffee_menu import MENU, resources

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']


def coffee_resources_adjustor(name):
    ingredients = MENU[name]['ingredients']
    global water, milk, coffee
    water -= ingredients['water']
    coffee -= ingredients['coffee']
    if name != 'espresso':
        milk -= ingredients['milk']


def coffee_cost(coffee_type):
    for i in range(len(MENU)):
        return MENU[coffee_type]['cost']


def coin_checker():
    quarters = float(input(f"How many quarters?"))
    dimes = float(input(f"How many dimes?"))
    nickles = float(input(f"How many nickles?"))
    pennies = float(input(f"How many pennies?"))
    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)


def resource_checker(name):
    ingredients = list(MENU[name]['ingredients'].values())
    water_required = ingredients[0]
    milk_required = ingredients[1]
    coffee_required = ingredients[2]
    if water < water_required:
        return True
    elif milk < milk_required:
        return True
    elif coffee < coffee_required:
        return True


def coffee_machine():
    making_coffee = True
    while making_coffee:
        user_request = str(input(f"Would you like? (espresso/latte/cappuccino):\n")).lower()
        if user_request == 'report':
            print(f"Coffee: {coffee}\nWater: {water}\nMilk: {milk}")
            continue
        if resource_checker(name=user_request):
            print("Not enough resources! Refill")
            print(f"Coffee: {coffee}\nWater: {water}\nMilk: {milk}")
            exit()
        cost = coffee_cost(user_request)
        print(f"The price for the {user_request} is {cost}")
        print(f"Please insert coins.")
        inserted = coin_checker()
        not_enough = True
        while not_enough:
            if cost == inserted:
                coffee_resources_adjustor(user_request)
                print(f"Here is your {user_request}")
                not_enough = False
            elif cost > inserted:
                print(f"Oops too, there is still {cost - inserted:.2f} left please add more money!")
                inserted += coin_checker()
                continue
            else:
                coffee_resources_adjustor(user_request)
                print(f"Here is your {user_request} and your change is {inserted - cost:.2f}")
                not_enough = False


coffee_machine()
