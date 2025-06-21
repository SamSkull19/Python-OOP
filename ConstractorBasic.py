# Define a class named 'Phone'
class Phone:
    # Class attribute (shared by all Phone objects)
    manufactured = 'Korea'

    # Constructor method (__init__) is automatically called when a new object is created
    # 'self' refers to the current object being created
    def __init__(self, price, brand, color):
        # These are instance attributes, specific to each object
        self.price = price
        self.brand = brand
        self.color = color

    # An instance method named 'call'
    def call(self):
        print("This is From Class A")


# Create an object named 'myPhone' with specific attributes
myPhone = Phone(10000, 'Samsung', 'Black')

# Print the attributes of the first phone
print(f"Price : {myPhone.price} | Brand : {myPhone.brand} | Color : {myPhone.color}")

# Call the 'call' method for this object
myPhone.call()

# Create a new Phone object (this replaces the previous one in 'myPhone')
myPhone = Phone(12000, 'Xiaomi', 'Orange')

# Print the attributes of the second phone
print(f"Price : {myPhone.price} | Brand : {myPhone.brand} | Color : {myPhone.color}")

# Create a third Phone object, again replacing the previous one
myPhone = Phone(17000, 'Iphone', 'Blue')

# Print the attributes of the third phone
print(f"Price : {myPhone.price} | Brand : {myPhone.brand} | Color : {myPhone.color}")
