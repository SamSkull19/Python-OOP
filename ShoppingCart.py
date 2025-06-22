# Define a class for Shopping
class Shopping:
    def __init__(self, name):
        # Initialize the shopper's name and an empty shopping cart
        self.name = name
        self.cart = []

    # Method to add a product to the cart
    def add_to_cart(self, item, price, quantity):
        # Create a dictionary with product details
        product = { "item" : item, "price" : price, "quantity" : quantity }
        # Add the product to the cart list
        self.cart.append(product)

    # Method to remove a product from the cart by its item name
    def remove_from_cart(self, product):
        # Filter out the product whose 'item' matches the given product name
        self.cart = [i for i in self.cart if i['item'] != product]
        print(f"{product} is removed from the Cart")

    # Method to handle checkout and show payment summary
    def checkout(self, amount):
        total = 0
        # Calculate total cost of items in the cart
        for item in self.cart:
            total += item['price'] * item['quantity']

        print(f'Total Price : {total}')

        # Compare paid amount with total and print appropriate message
        if amount < total:
            print(f"Please pay more {total - amount}")
        
        elif amount > total:
            print(f"You have paid extra {amount - total}")
        
        else:
            print(f"Your payment is successful")
            print(f"You will get your product in few days")


# Create an instance of the Shopping class for a user named 'Samin'
shop = Shopping('Samin')

# Add items to the cart
shop.add_to_cart('Watch', 4000, 2)
print(shop.cart)  # View current cart

shop.add_to_cart('Pen', 10, 12)
print(shop.cart)  # View updated cart

shop.add_to_cart('Laptop', 50000, 1)
print(shop.cart)  # View final cart before checkout

# Try different checkout amounts
shop.checkout(40000)   # Not enough
shop.checkout(80000)   # Extra paid
shop.checkout(58120)   # Exact amount

# Remove an item from the cart
shop.remove_from_cart('Laptop')
print(shop.cart)  # View cart after removal
