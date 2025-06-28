# 🧍 Base class for any person
class Person:
    def __init__(self, name, age, height, weight):
        # Initialize basic attributes
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    # Common method for all persons
    def eat(self):
        print("Eat Sleep Play and Repeat")

    # This method must be implemented by subclasses
    def exercise(self):
        raise NotImplementedError


# 🏏 Derived class: Cricketer inherits from Person
class Cricketer(Person):
    def __init__(self, name, age, height, weight, bat, ball, field):
        # Initialize Cricketer-specific attributes
        self.bat = bat
        self.ball = ball
        self.field = field
        # Call the constructor of the base class (Person)
        super().__init__(name, age, height, weight)
    
    # Overriding eat method with additional details
    def eat(self):
        print(f"{self.name} Eat Sleep Play and Repeat | Height: {self.height}, Weight: {self.weight}")

    # Providing implementation for abstract method
    def exercise(self):
        print(f"{self.name} is going to the gym and doing some workout.")


# 👤 Creating first object: sakib
sakib = Cricketer('Sakib', 35, 6.2 , '60 Kg', 120, 5, 2)
sakib.eat()         # Custom eat method for Sakib
sakib.exercise()    # Exercise method for Sakib

print('---')

# 👤 Creating second object: tamim
tamim = Cricketer('Tamim', 33, 5.9, '68 Kg', 100, 4, 3)
tamim.eat()         # Custom eat method for Tamim
tamim.exercise()    # Exercise method for Tamim
