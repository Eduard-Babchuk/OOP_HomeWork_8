from abc import ABC, abstractmethod

class OrderManager:
    def __init__(self, discount_calculator, receipt_generator):
        self.order_items = []
        self.discount_calculator = discount_calculator
        self.receipt_generator = receipt_generator
        self.total = 0.0

    def add_item(self, dish, quantity, menu):
        if dish in menu:
            self.order_items.append((dish, quantity))
            self.total += menu[dish] * quantity
        else:
            print(f"Dish {dish} is not on the menu.")

    def apply_discount(self):
        self.total = self.discount_calculator.calculate_discount(self.total)

    def generate_receipt(self):
        self.apply_discount()
        return self.receipt_generator.generate(self.order_items, self.total)

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, total):
        pass

class PercentageDiscount(DiscountStrategy):
    def calculate_discount(self, total):
        if total > 50:
            return total * 0.9
        return total

class BulkDiscount(DiscountStrategy):
    def calculate_discount(self, total):
        if total > 30:
            return total * 0.95
        return total

class ReceiptGenerator:
    def generate(self, order_items, total):
        receipt = "Receipt:\n"
        for dish, quantity in order_items:
            receipt += f"{dish} x{quantity} = {quantity * 10} USD\n"  # Це просто для прикладу
        receipt += f"Total: {total} USD\n"
        return receipt