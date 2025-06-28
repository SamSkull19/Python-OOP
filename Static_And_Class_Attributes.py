# 🛒 Class representing a shopping system
class Shopping:
    # 🧺 Class variable shared across all instances
    cart = []
    origin = "Bangladesh"

    def __init__(self):
        # 🧍 Instance variables (unique for each object)
        self.name = "Rahim"
        self.location = "Sylhet Bangladesh"

    # 🛍️ Instance method (needs 'self' and tied to a specific object)
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'Buying {item} For price : {price} and Remaining : {remaining}')

    # ✖️ Static method: no access to class or instance (no self/cls)
    @staticmethod
    def multiply(a, b):
        print(a * b)

    # 👀 Class method: takes 'cls' (conventionally), works with class variables
    @classmethod
    def see(self, item):  # NOTE: 'self' here actually refers to the class (better to name it 'cls')
        print(f'Item Name : {item}')


# 🧪 Creating object 'coke'
coke = Shopping()

# 🛍️ Calling instance method (uses self, tied to the 'coke' object)
coke.purchase('Coke', 2, 3)  # Output: Buying Coke For price : 2 and Remaining : 1

# 👀 Calling class method with object (allowed)
coke.see('Mojo Jojo')        # Output: Item Name : Mojo Jojo

# 👀 Calling class method with class name (preferred)
Shopping.see('Mojo Jojo')    # Output: Item Name : Mojo Jojo

# ✖️ Calling static method with class name (preferred)
Shopping.multiply(5, 6)      # Output: 30

# ✖️ Calling static method with object (allowed but not preferred)
coke.multiply(5, 6)          # Output: 30
