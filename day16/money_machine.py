class MoneyMachine:

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self) -> None:
        self.profits = 0
        self.money_received = 0

    def report(self):
        print(f"Money: ${self.profits}")
    
    def process_coins(self):
        print("Please insert Coins")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received
    
    def make_payment(self, cost):
        if self.money_received > cost:
            print(f"Here is your change back: ${round(self.money_received - cost,2)}")
            self.profits += round(self.money_received - cost,2)
            return True
        elif self.money_received == cost:
            self.profits += self.money_received
            return True
        else:
            print(f"Insufficient Funds, Balance ${round(cost - self.money_received, 2)} left")
            return False
    