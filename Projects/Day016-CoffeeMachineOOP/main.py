from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def run_coffeemaker():

    coffeemaker = CoffeeMaker()
    moneymachine = MoneyMachine()
    drinks_menu = Menu()

    print(f"Please select a drink using the numpad: ")
    print(drinks_menu.get_items())
    user_input = int(input())
    drink = drinks_menu.find_drink(drinks_menu.menu[user_input - 1].name)
    while not coffeemaker.is_resource_sufficient(drink):
        user_input = int(input("Sorry this drink is not available. Please select another drink: "))
        drink = drinks_menu.find_drink(drinks_menu.menu[user_input - 1].name)

    print(f"One {drink.name} will cost ${drink.cost}.")
    sufficient_payment = False
    while not sufficient_payment:
        sufficient_payment = moneymachine.make_payment(drink.cost)

    coffeemaker.make_coffee(drink)


get_coffee = "yes"
while get_coffee == "yes":
    run_coffeemaker()
    get_coffee = input("Would you like to get another coffee? Yes/No.").lower()



