# Define a class named 'Cart'
class Cart:
    # Constructor method to initialize buyer name and individual cart
    def __init__(self, buyer):
        self.buyer = buyer        # Instance variable for buyer name
        self.cart = []            # Instance variable: each buyer gets their own cart

    # Method to add an item to the buyer's cart
    def add_to_cart(self, item):
        self.cart.append(item)    # Add item to this buyer's personal cart

# Create an object 'a' for buyer "SamSkull"
a = Cart("SamSkull")
a.add_to_cart('Shoes')
a.add_to_cart('Mobile')
a.add_to_cart('Pen')
a.add_to_cart('Ball')

# Print the cart for buyer 'a'
print(a.cart)  # Output: ['Shoes', 'Mobile', 'Pen', 'Ball']

# Create another object 'b' for buyer "SamSkull"
b = Cart("SamSkull")
b.add_to_cart('Candy')
b.add_to_cart('Watch')
b.add_to_cart('Bottle')
b.add_to_cart('Bat')

# Print the cart for buyer 'b'
print(b.cart)  # Output: ['Candy', 'Watch', 'Bottle', 'Bat']
