MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

drinks = ['Espresso', 'Latte', 'Cappuccino']


def resources_sufficient(user_order: str, menu: dict,
                         machine_resources: dict) -> bool:
    ingredients = menu[user_order]['ingredients']
    for ingredient in ingredients:
        if ingredient == 'water':
            if machine_resources['water'] - ingredients[ingredient] < 0:
                return False
        elif ingredient == 'milk':
            if machine_resources['milk'] - ingredients[ingredient] < 0:
                return False
        elif ingredient == 'coffee':
            if machine_resources['coffee'] - ingredients[ingredient] < 0:
                return False

    return True


def add_money(quarters: int, dimes: int, nickles: int, pennies: int) -> float:
    return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + \
           (pennies * 0.01)


all_done = 'Y'
while not all_done == 'N':
    command = input("To make an order, press 1. "
                    "\nTo see a report for this machine's resources, press 2. "
                    "\nTo refill ingredient(s) in this machine, press 3. ")

    if command == '1':
        drinks_copy = drinks.copy()
        order = input("What would you like? "
                      "Espresso/Latte/Cappuccino: ").lower()
        have_resources = resources_sufficient(order, MENU, resources)

        while not have_resources:
            drinks_copy.remove(order.title())
            order = input(f"The machine does not have the required ingredients "
                          f"to make your order. Please choose another drink: "
                          f"{'/'.join(drinks_copy)} ")

        if have_resources:
            for ingredient in MENU[order]['ingredients']:
                resources[ingredient] -= MENU[order]['ingredients'][ingredient]

            money_needed = MENU[order]['cost']
            input_money = 0
            print(f"Please insert ${money_needed}.")
            while input_money < money_needed:
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickels = int(input("How many nickels? "))
                pennies = int(input("How many pennies? "))

                input_money += add_money(quarters, dimes, nickels, pennies)
                input_money = round(input_money, 2)

                if input_money < money_needed:
                    print(f"Insufficient funds. Please insert "
                          f"${money_needed - input_money} more.")

            resources['money'] += input_money

            if input_money - money_needed > 0:
                resources['money'] -= round(input_money - money_needed, 2)
                print(f"Here is ${round(input_money - money_needed, 2)} "
                      f"in change.")

            print(f"Here is your {order}. Enjoy!")

    elif command == '2':
        print(f"Water: {resources['water']} mL"
              f"\nMilk: {resources['milk']} mL"
              f"\nCoffee: {resources['coffee']} g")

    elif command == '3':
        done = 'Y'
        while not done == 'N':
            change = input("What would you like to refill? Water/Milk/Coffee: "
                           "").lower()
            amount = float(input("How much would you like to add or remove? "
                                 "Values are in mL for Water/Milk and in grams "
                                 "for Coffee. "
                                 "\nNote: if you are removing an ingredient, "
                                 "please enter a negative value. "))

            resources[change] += amount
            if resources[change] < 0:
                resources[change] = 0

            done = input("Resource adjustments have been made. Would you like "
                         "to make anymore adjustments? Y/N: ").upper()

    all_done = input("Do you have any other business with the coffee machine? "
                     "Y/N: ").upper()
