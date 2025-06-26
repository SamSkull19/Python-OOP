# 🧬 Importing abstract base class tools
from abc import ABC, abstractmethod

# 🐾 Base Abstract Class
class Animal(ABC):
    def __init__(self, name):
        self.name = name  # Common attribute for all animals

    @abstractmethod
    def make_sound(self):
        # Abstract method that must be implemented by subclasses
        # No body is needed here (print is removed)
        pass


# 🐶 Dog Class inherits from Animal
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)  # Call Animal's constructor

    def make_sound(self):
        print(f"{self.name} is making Barking sound")


# 🐱 Cat Class inherits from Animal
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print(f"{self.name} is making Meow sound")


# 🐐 Goat Class inherits from Animal
class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print(f"{self.name} is making Meh sound")


# 🐄 Cow Class inherits from Animal
class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print(f"{self.name} is making Hamba sound")


# 🐘 Elephant Class inherits from Animal
class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print(f"{self.name} is making Horn sound")


# -------------------------
# ▶️ Individual Calls
# -------------------------

# Creating instances of animals
dog = Dog('Bruno')
dog.make_sound()

cat = Cat('Flusha')
cat.make_sound()

goat = Goat('Messi')
goat.make_sound()

cow = Cow('Forest Cow')
cow.make_sound()

elephant = Elephant('Brrr')
elephant.make_sound()


# -------------------------
# ▶️ Polymorphism in Action
# -------------------------
print("\nUsing loop with polymorphism:\n")

# Store all animal objects in a list
animals = [dog, cat, goat, cow, elephant]

# Call make_sound() for each animal in the list
# This demonstrates polymorphism: same method name, different behavior
for animal in animals:
    animal.make_sound()
