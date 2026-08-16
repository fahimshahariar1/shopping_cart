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
        