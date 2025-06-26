from abc import ABC, abstractmethod

# 🧬 Abstract Base Class: Animal
class Animal(ABC):
    # Abstract method: All animals must define their own eat behavior
    @abstractmethod
    def eat(self):
        pass  # Must be overridden; cannot contain a body

    # Abstract method: All animals must define how they move
    @abstractmethod  
    def move(self):
        pass


# 🐒 Concrete Class: Monkey inherits from Animal
class Monkey(Animal):
    def __init__(self, name, food):
        self.name = name      # Monkey's name
        self.food = food      # What the monkey eats

    def eat(self):
        print(f"{self.name} eats {self.food}")

    def move(self):
        print(f"{self.name} moves by jumping and climbing")


# 🐦 Concrete Class: Bird inherits from Animal
class Bird(Animal):
    def __init__(self, name, food):
        self.name = name      # Bird's name
        self.food = food      # What the bird eats

    def eat(self):
        print(f"{self.name} pecks and eats {self.food}")

    def move(self):
        print(f"{self.name} moves by flying")


# ------------------------------
# ▶️ Object Creation & Testing
# ------------------------------

# Create a Monkey object
monkey = Monkey('Krabby', 'Banana')
monkey.eat()   # Output: Krabby eats Banana
monkey.move()  # Output: Krabby moves by jumping and climbing

# Create a Bird object
bird = Bird('Robin', 'Worms')
bird.eat()     # Output: Robin pecks and eats Worms
bird.move()    # Output: Robin moves by flying
