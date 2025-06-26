from math import pi

# 🎯 Base Class
class Shape:
    def __init__(self, name):
        self.name = name

# 🟩 Rectangle Class
class Rectangle(Shape):
    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width

# ⚪ Circle Class
class Circle(Shape):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)

    def area(self):
        return pi * self.radius * self.radius

# ⬛ Square Class
class Square(Shape):
    def __init__(self, name, side):
        self.side = side
        super().__init__(name)

    def area(self):
        return self.side * self.side


# -------------------------
# ▶️ Create Shape Objects
# -------------------------

shapes = [
    Rectangle("MyRectangle", 10, 5),
    Circle("MyCircle", 7),
    Square("MySquare", 4)
]

# -------------------------
# ▶️ Use Polymorphism
# -------------------------

print("Shape Areas:")
for shape in shapes:
    print(f"{shape.name} Area: {shape.area():.2f}")
