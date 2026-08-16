
class ShoppingCart:

  def __init__(self, customer_name, item_prices = None):
    self.customer_name =  customer_name
    self.item_prices = item_prices or []

  def add_item(self, price):
    if price > 0:
      self.item_prices.append(price)
      print(f"Item of {price} BDT added to {self.customer_name}'s cart")
    else:
      print("Invalid price. Price must be a Positive number")

  def remove_item(self, price):
    if price in self.item_prices:
      self.item_prices.remove(price)
      print(f"Item of {price} BDT removed from {self.customer_name}'s cart")
    else:
      print(f"Item of {price} BDT not found in {self.customer_name}'s cart")


  def calculate_total(self):
    total = 0
    for price in self.item_prices:
      total += price
    return total

  def apply_discount(self):
    total = self.calculate_total()
    if total >= 3000:
      discount = total * 0.10
      final = total - discount
      print(f"Discount applied: 10% (-{discount} BDT)")

    else:
      final = total
      print("No Discount applied")

    return final

  def display_cart(self):
    total = self.calculate_total()
    final = self.apply_discount()
    print("=" * 40)
    print(f"  Customer  : {self.customer_name}")
    print(f"  Items     : {self.item_prices}")
    print(f"  Total     : {total} BDT")
    print(f"  Payable   : {final} BDT")
    print(f"  No. Items : {len(self.item_prices)}")
    print("=" * 40)

  def clear_cart(self):
    self.item_prices = []
    print(f"{self.customer_name}'s cart is cleared")

  def __add__(self, other):
    combined_name = f"{self.customer_name} + {other.customer_name}"
    combined_item_prices = self.item_prices + other.item_prices
    return ShoppingCart(combined_name, combined_item_prices)


cart1 = ShoppingCart("Fahim")
cart2 = ShoppingCart("Shahariar")


print("Cart1")
cart1.add_item(500)
cart1.add_item(1000)
cart1.add_item(1500)
print("\nCart2")
cart2.add_item(600)
cart2.add_item(5000)
cart2.add_item(1000)

cart1.remove_item(500)
cart2.remove_item(1000)


print("Cart1")
cart1.display_cart()
print("\nCart2")
cart2.display_cart()


print("Combined Cart")
combined = cart1 + cart2
combined.display_cart()