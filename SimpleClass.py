# Define a class named 'Phone'
class Phone:
    # Class attributes (shared by all instances of Phone)
    price = 10000           
    color = 'Black'         
    brand = 'Samsung'       
    manufactured = 'Korea'  
    rating = 4.5            

# Create an instance (object) of the Phone class
myPhone = Phone()

# Print the object itself (will show memory address, not useful unless __str__ is defined)
print(myPhone)

# Access and print individual attributes of the object
price = myPhone.price      # Get the price of the phone
print(price)               # Print the price

color = myPhone.color      # Get the color of the phone
print(color)               # Print the color

# Directly access and print other attributes
print(myPhone.brand)       # Print the brand
print(myPhone.manufactured)  # Print the manufacturing country
print(myPhone.rating)      # Print the rating
