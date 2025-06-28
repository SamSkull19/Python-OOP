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

    # Abstract method - must be overridden
    def exercise(self):
        raise NotImplementedError


# 🏏 Derived class: Cricketer inherits from Person
class Cricketer(Person):
    def __init__(self, name, age, height, weight, bat, ball, field):
        # Initialize Cricketer-specific attributes
        self.bat = bat
        self.ball = ball
        self.field = field
        # Initialize common attributes from Person
        super().__init__(name, age, height, weight)
    
    # Method overriding: eat method customized for Cricketer
    def eat(self):
        print(f"{self.name} Eat Sleep Play and Repeat | Height: {self.height}, Weight: {self.weight}")

    # Method overriding: concrete implementation of exercise
    def exercise(self):
        print(f"{self.name} is going to the gym and doing some workout.")

    # 🧮 Operator Overloading: add two cricketers' ages
    def __add__(self, other):
        return self.age + other.age
    
    # 🧮 Operator Overloading: multiply two cricketers' ages
    def __mul__(self, other):
        return self.age * other.age
    
    # ➕ Operator Overloading: compare who is older (greater than)
    def __gt__(self, other):
        return self.age > other.age
    
    # ➖ Operator Overloading: compare who is shorter (less than)
    def __lt__(self, other):
        return self.height < other.height    
    
    # ✅ Operator Overloading: check if two cricketers have the same weight
    def __eq__(self, other):
        return self.weight == other.weight
    
    # 🧮 len() Overloading: return length of cricketer’s name
    def __len__(self):
        return len(self.name)


# 👤 Creating first object: sakib
sakib = Cricketer('Sakib', 35, 6.2 , '60 Kg', 120, 5, 2)
sakib.eat()         # Custom eat method for Sakib
sakib.exercise()    # Exercise method for Sakib

print('---')

# 👤 Creating second object: tamim
tamim = Cricketer('Tamim', 33, 5.9, '60 Kg', 100, 4, 3)
tamim.eat()         # Custom eat method for Tamim
tamim.exercise()    # Exercise method for Tamim

# ➕ Add ages: 35 + 33 = 68
print(sakib + tamim)

# ✖️ Multiply ages: 35 * 33 = 1155
print(sakib * tamim)

# ➕ Who is older? sakib > tamim → True
print(sakib > tamim)

# ➖ Who is shorter? sakib < tamim → False (6.2 > 5.9)
print(sakib < tamim)

# ✅ Do they have the same weight? True
print(sakib == tamim)

# 🧮 Length of names
print(len(sakib))   # 5
print(len(tamim))   # 5
