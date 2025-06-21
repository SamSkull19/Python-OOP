# A standalone function named 'call' (not inside any class)
def call():
    print("This From Call Function")

# Define a class named 'Phone'
class Phone:
    # Class attributes (shared across all instances unless overridden)
    price = 10000
    brand = 'Samsung'
    color = 'Black'

    # Instance method named 'call'
    # 'self' refers to the current object (instance) that is calling this method
    def call(self):
        print("This is From Class A")

    # Another instance method 'sms' that takes 2 extra arguments: number and msg
    def sms(self, number, msg):
        print(f"Mobile Number : {number} Message : {msg}")

# Create an instance (object) of the Phone class
myPhone = Phone()

# Call the 'call' method from the Phone class using the object
myPhone.call()  # Output: This is From Class A

# Access and print the 'color' attribute of the object
print(myPhone.color)  # Output: Black

# Call the global (outside class) function named 'call'
call()  # Output: This From Call Function

# Print the 'brand' attribute of the object
print(myPhone.brand)  # Output: Samsung

# Call the 'sms' method from the Phone class using the object and pass arguments
myPhone.sms(124512, "GGWP")  # Output: Mobile Number : 124512 Message : GGWP
