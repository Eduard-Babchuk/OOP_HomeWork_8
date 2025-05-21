class CafeOrder:
    def __init__(self):
        self.menu = {
            "Pasta": 10.0,
            "Pizza": 12.0,
            "Salad": 5.0,
            "Soup": 7.0
        }
        self.order_items = []
        self.total = 0.0

    def add_item(self, dish, quantity):
        if dish in self.menu:
            self.order_items.append((dish, quantity))
            self.total += self.menu[dish] * quantity
        else:
            print(f"Dish {dish} is not on the menu.")

    def apply_discount(self):
        if self.total > 50:
            self.total *= 0.9
        elif self.total > 30:
            self.total *= 0.95

    def generate_receipt(self):
        print("Receipt:")
        for dish, quantity in self.order_items:
            print(f"{dish} x{quantity} = {self.menu[dish] * quantity} USD")
        self.apply_discount()
        print(f"Total: {self.total} USD")
