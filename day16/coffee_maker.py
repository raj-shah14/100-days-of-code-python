class CoffeeMaker:
    def __init__(self) -> None:
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml \nMilk: {self.resources['milk']}ml \nCoffee: {self.resources['coffee']}g")
    
    def is_resources_sufficient(self, drink):
        if self.resources["water"] < drink.ingredients['water']:
            return False
    
        # Check Coffee
        if self.resources["coffee"] < drink.ingredients['coffee']:
            return False
        
        # Check milk
        if drink.name != 'espresso':
            if self.resources["milk"] < drink.ingredients['milk']:
                return False      
        return True
    
    def make_coffee(self, order):
        # update reosurces
        self.resources["water"] -= order.ingredients['water']
        if order.name != 'espresso':
            self.resources["milk"] -= order.ingredients['milk']
        self.resources["coffee"] -= order.ingredients['coffee']
        print(f"Enjoy your {order.name}!")
