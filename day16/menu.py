
class MenuItem:
    def __init__(self, name, cost, ingredients) -> None:
        self.name = name
        self.cost = cost
        self.ingredients = ingredients

class Menu:
    def __init__(self, items) -> None:
        self.items = items

    def get_items(self):
        '''
        Returns all the names of the available menu items as a concatenated string
        '''
        return '/'.join(item.name for item in self.items)

    def find_drink(self, order_name):
        for item in self.items:
            if item.name == order_name:
                return item

        return None