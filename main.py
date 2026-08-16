#Shopping Cart Project 
#OSTAD

class ShoppingCart:
    
    def __init__(self, customer_name, items, price):
        self.customer_name = customer_name
        self.items = items
        self.price = price

    def add_item(self, price):
        self.price = price
        
    def remove_item(self, price):
        self.price = price
    
    def calculate_total(self):
        total = sum(self.price)
        return total
    
    def apply_discount(self):
        if self.calculate_total() > 3000:
            discount = self.calculate_total() * 0.1
            return self.calculate_total() - discount
        else:
            return self.calculate_total()
    
    def display_cart(self):
        print(f"Customer Name: {self.customer_name}")
        print("Items in Cart:")
        for item in self.items:
            print(f"- {item}")
        print(f"Total Price: {self.calculate_total()}")
        print(f"Price after Discount: {self.apply_discount()}")
    
    def clear_cart(self):
        self.items = []
        self.price = []
        print("Cart has been cleared.")
    
    def __add__(self, other):
        if isinstance(other, ShoppingCart):
            combined_items = self.items + other.items
            combined_price = self.price + other.price
            return ShoppingCart(self.customer_name, combined_items, combined_price)
        else:
            raise ValueError("Can only add another ShoppingCart instance.")
    

cart1 = ShoppingCart("John Doe")
cart2 = ShoppingCart("Jane Smith")

cart1.add_item("500")
cart1.add_item("1500")
cart2.add_item("2000")
cart2.add_item("1500")



