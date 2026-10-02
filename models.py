"""ByteBites core models.

Classes (see bytebites_design.mmd):
- Customer: a user; tracks name and purchase history.
- MenuItem: one food item; tracks name, price, category, popularity.
- Menu: the full collection of MenuItems; filters and sorts them.
- Order: one transaction; stores selected MenuItems and computes the total.
"""


class MenuItem:
    def __init__(self, name, price, category, popularity):
        self.name = name
        self.price = price
        self.category = category
        self.popularity = popularity


class Menu:
    def __init__(self):
        self.items = []


class Order:
    def __init__(self):
        self.items = []


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []
