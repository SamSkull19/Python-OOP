# 🔧 Parent class: Devices
class Devices:
    def __init__(self, device_type, brand, price, color):
        self.device_type = device_type  # e.g., Mobile, Laptop, etc.
        self.brand = brand              # e.g., Samsung, HP
        self.price = price              # e.g., 40000
        self.color = color              # e.g., Black

    def run(self):
        # Method to simulate device running
        return f'Running Device is {self.device_type}'

# 📱 Subclass: Mobile (inherits from Devices)
class Mobile(Devices):
    def __init__(self, device_type, brand, price, color, memory, screen_size):
        self.memory = memory                  # e.g., 12 GB
        self.screen_size = screen_size        # e.g., 6.5 Inch
        super().__init__(device_type, brand, price, color)  # Initialize parent class

    def __repr__(self):
        # Custom string representation for printing
        return (f'Mobile Brand : {self.brand} | Mobile Price : {self.price} | '
                f'Color : {self.color} | Memory : {self.memory} | Screen Size : {self.screen_size}')

# 💻 Subclass: Laptop (inherits from Devices)
class Laptop(Devices):
    def __init__(self, device_type, brand, price, color, processor, ram):
        self.processor = processor             # e.g., Intel i7
        self.ram = ram                         # e.g., 16 GB
        super().__init__(device_type, brand, price, color)  # Initialize parent class

    def __repr__(self):
        # Custom string representation for printing
        return (f'Laptop Brand : {self.brand} | Laptop Price : {self.price} | '
                f'Color : {self.color} | Processor : {self.processor} | RAM : {self.ram}')


# -------------------------------
# ▶️ Creating Objects and Testing
# -------------------------------

# Create Mobile Object
myPhone = Mobile('Mobile', 'Samsung', 400000, 'Black', '12 GB', '6.67 Inch')
print(myPhone.run())
print(myPhone)

# Create Laptop Object
myLaptop = Laptop('Laptop', 'HP', 120000, 'Silver', 'Intel i7', '16 GB')
print(myLaptop.run())
print(myLaptop)

