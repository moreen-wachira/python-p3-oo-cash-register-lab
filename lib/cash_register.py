# lib/cash_register.py

class CashRegister:
    def __init__(self, discount=0):
        self.items = []
        self.total = 0
        self.discount = discount
        self.last_transaction_amount = 0

    def add_item(self, item_name, quantity, price):
        # Add item to the list of items
        self.items.append({"item": item_name, "quantity": quantity, "price": price * quantity})

        # Update the total and last_transaction_amount
        self.total += price * quantity
        self.last_transaction_amount = price * quantity

    def calculate_discount(self):
        # Calculate discount based on the total and discount percentage
        return self.total * (self.discount / 100)

    def apply_discount(self):
        # Apply discount to the total
        self.total -= self.calculate_discount()
        return f"After applying a {self.discount}% discount, the total is: {self.total}"

    def void_last_transaction(self):
        # Remove the last transaction from the total
        self.total -= self.last_transaction_amount
        self.items.pop()  # Remove the last item from the list

    def show_items(self):
        # Display the list of items
        return self.items

    def get_total(self):
        # Return the current total
        return self.total
