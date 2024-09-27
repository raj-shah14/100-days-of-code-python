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
}

money = {
    "value": 0,
}

def get_report():
    print(f" Water:{resources["water"]}ml \n Milk: {resources['milk']}ml \n Coffee: {resources['coffee']}g \n Money: ${money['value']}")

def calculate_total(q, p, n, d):
    q *= 0.25
    p *= .10
    n *= .05
    d *= .01 
    return q + p + n + d

def validate_cost(coffee, amt):
    if amt < coffee['cost']:
        print(f"Insufficient Funds. Please add ${round(coffee["cost"] - amt, 2)} and retry. Returning your change")
    return 
    
def check_resources(user_input, coffee, resources):
    # Check water
    if resources["water"] < coffee['ingredients']['water']:
        print("Sorry not Enough Water. Money Refunded")
    
    # Check Coffee
    if resources["coffee"] < coffee['ingredients']['coffee']:
        print("Sorry not Enough Coffee. Money Refunded")
        
    # Check milk
    if user_input != 'espresso':
        if resources["milk"] < coffee['ingredients']['milk']:
            print("Sorry not Enough Milk. Money Refunded")

def request_money():
    print("Please insert Coins")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    amt_paid = calculate_total(quarters, pennies, nickles, dimes)
    print(f"Total amount Paid: ${round(amt_paid, 2)}")
    return amt_paid

def dispense_coffee(user_input, coffee, resources):
    # update reosurces
    resources["water"] -= coffee['ingredients']['water']
    if user_input != 'espresso':
        resources["milk"] -= coffee['ingredients']['milk']
    resources["coffee"] -= coffee['ingredients']['coffee']
    print("Enjoy your Coffee! ☕")

def update_profit(coffee):
    money['value'] += coffee['cost']

def check_for_remaining_change(amt_paid, coffee):
    if amt_paid > coffee['cost']:
        print(f"Here is your remaining balance: ${round(amt_paid - coffee['cost'],2)}")


def coffee_machine():
    while True:
        user_input = input("What would you like to drink? \n Type 'espresso' -> $1.5 \n 'latte' -> $2.5 \n 'cappuccino' -> $3.0\n")

        if user_input == 'off':
            print("Turning off the Coffee Machine")
            break

        elif user_input == 'report':
            get_report()

        elif user_input in MENU:
            coffee = MENU[user_input]
            check_resources(user_input, coffee, resources)
            amt_paid = request_money()
            validate_cost(coffee, amt_paid)
            dispense_coffee(user_input, coffee, resources)
            update_profit(coffee)
            check_for_remaining_change(amt_paid, coffee)
            get_report()

coffee_machine()
    

    
