# Define a class named 'Cart'
class Cart:
    # Class variable (shared by ALL instances of Cart)
    cart = []

    # Constructor to initialize each object with a buyer name
    def __init__(self, buyer):
        self.buyer = buyer  # Instance variable unique to each object

    # Instance method to add an item to the cart
    def add_to_cart(self, item):
        # Adds item to the shared class-level cart list
        self.cart.append(item)


# Create an object 'a' of Cart for buyer "SamSkull"
a = Cart("SamSkull")
a.add_to_cart('Shoes')
a.add_to_cart('Mobile')
a.add_to_cart('Pen')
a.add_to_cart('Ball')

# Print the cart of 'a'
print(a.cart)  # Output: ['Shoes', 'Mobile', 'Pen', 'Ball']

# Create another object 'b' of Cart with the same buyer name
b = Cart("SamSkull")
b.add_to_cart('Candy')
b.add_to_cart('Watch')
b.add_to_cart('Bottle')
b.add_to_cart('Bat')

# Print the cart of 'b'
print(b.cart)  # Output: ['Shoes', 'Mobile', 'Pen', 'Ball', 'Candy', 'Watch', 'Bottle', 'Bat']
