from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    if choice == "off":
        is_on = False
        print("off")
    elif choice == "report":
        coffee_maker.report()
    else:
        drink = menu[choice]
        if coffee_maker.is_resource_sufficient(drink["ingredients"]):
            payment = money_machine.process_coins()
            if money_machine(payment, drink["cost"]):
                coffee_maker(choice, drink["ingredients"])