from exercise.without_SOLID import CafeOrder
from exercise.with_SOLID import OrderManager, PercentageDiscount, ReceiptGenerator

def run_monolithic_example():
    order = CafeOrder()
    order.add_item("Pizza", 2)
    order.add_item("Pasta", 1)
    order.generate_receipt()

def run_solid_example():
    menu = {
        "Pasta": 10.0,
        "Pizza": 12.0,
        "Salad": 5.0,
        "Soup": 7.0
    }

    discount_calculator = PercentageDiscount()
    receipt_generator = ReceiptGenerator()
    order_manager = OrderManager(discount_calculator, receipt_generator)

    order_manager.add_item("Pizza", 2, menu)
    order_manager.add_item("Pasta", 1, menu)
    print(order_manager.generate_receipt())

def main():
    print("Choose the example to run:")
    print("1. Monolithic Example (without SOLID)")
    print("2. SOLID Example")

    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        run_monolithic_example()
    elif choice == "2":
        run_solid_example()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()