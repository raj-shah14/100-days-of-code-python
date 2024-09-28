from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

espresso = MenuItem('espresso', 1.5, {"water":50, "coffee":18 } )
latte = MenuItem('latte', 2.5, {"water":200, "milk":150, "coffee":24 }  )
cappuccino = MenuItem('cappuccino', 3.0, {"water":250, "milk":100, "coffee":24 } )

MENU = {espresso , latte, cappuccino}

menu = Menu(MENU)
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

def coffee_machine():
    order_name = input(f"What would you like? \n{menu.get_items()}: ")
    if order_name == "off":
        print("Turning off the Coffee Machine, See you!")
        return
    
    if order_name == "report":
        coffee_maker.report()
        money_machine.report()
        return 
    
    drink = menu.find_drink(order_name)
    if not coffee_maker.is_resources_sufficient(drink):
        print(f"Insufficient Resources, Sorry, {order_name} can't be made")

    money_machine.process_coins()
    if not money_machine.make_payment(drink.cost):
        return 
    
    coffee_maker.make_coffee(drink)
    coffee_maker.report()
    money_machine.report()

coffee_machine()
    
    