"""ByteBites core models.

Classes (see bytebites_design.mmd):
- Customer: a user; tracks name and purchase history.
- MenuItem: one food item; tracks name, price, category, popularity.
- Menu: the full collection of MenuItems; filters and sorts them.
- Order: one transaction; stores selected MenuItems and computes the total.
"""

from typing import List


class MenuItem:
    """One food item the app sells."""

    def __init__(self, name: str, price: float, category: str, popularity: float):
        if not name or not name.strip():
            raise ValueError("name must not be empty")
        if price < 0:
            raise ValueError("price must not be negative")
        if popularity < 0:
            raise ValueError("popularity must not be negative")
        self.name = name
        self.price = price
        self.category = category
        self.popularity = popularity

    def __repr__(self) -> str:
        return (f"MenuItem({self.name!r}, {self.price}, "
                f"{self.category!r}, {self.popularity})")


class Menu:
    """The full collection of MenuItems."""

    def __init__(self):
        self.items: List[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def filter_by_category(self, category: str) -> List[MenuItem]:
        """Items whose category matches, ignoring case and outer whitespace."""
        wanted = category.strip().lower()
        return [i for i in self.items if i.category.strip().lower() == wanted]

    def sort_by_popularity(self) -> List[MenuItem]:
        """New list, most popular first. Ties keep their original order."""
        return sorted(self.items, key=lambda i: i.popularity, reverse=True)

    def sort_by_price(self) -> List[MenuItem]:
        """New list, cheapest first. Ties keep their original order."""
        return sorted(self.items, key=lambda i: i.price)


class Order:
    """A single transaction: the items a customer picked."""

    def __init__(self):
        self.items: List[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def calculate_total(self) -> float:
        """Sum of item prices, rounded to cents. 0.0 for an empty order."""
        return round(sum(i.price for i in self.items), 2)


class Customer:
    """A user, with past orders used to verify they are real."""

    def __init__(self, name: str):
        self.name = name
        self.purchase_history: List[Order] = []

    def add_purchase(self, order: Order) -> None:
        self.purchase_history.append(order)

    def is_verified(self) -> bool:
        """Real user = has a name and at least one past order."""
        return bool(self.name and self.name.strip()) and len(self.purchase_history) > 0


if __name__ == "__main__":
    burger = MenuItem("Spicy Burger", 8.50, "Burgers", 4.7)
    soda = MenuItem("Large Soda", 2.25, "Drinks", 4.1)
    cookie = MenuItem("Choc Cookie", 1.75, "Desserts", 4.9)
    tea = MenuItem("Iced Tea", 2.00, "Drinks", 3.8)

    menu = Menu()
    for item in (burger, soda, cookie, tea):
        menu.add_item(item)

    print("Drinks:", menu.filter_by_category("drinks"))
    print("By popularity:", [i.name for i in menu.sort_by_popularity()])
    print("By price:", [i.name for i in menu.sort_by_price()])

    order = Order()
    order.add_item(burger)
    order.add_item(soda)
    print("Order total:", order.calculate_total())

    alice = Customer("Alice")
    print("Verified before order:", alice.is_verified())
    alice.add_purchase(order)
    print("Verified after order:", alice.is_verified())
