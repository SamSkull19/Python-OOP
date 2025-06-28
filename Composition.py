# 🚗 Base class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} is moving at {self.speed} km/h.")

# 🚙 Derived class (Car is a Vehicle)
class Car(Vehicle):
    def __init__(self, brand, speed, fuel):
        # 🔁 Call the constructor of Vehicle (parent)
        super().__init__(brand, speed)
        self.fuel = fuel

    def move(self):
        # 🔁 Overriding move method
        print(f"{self.brand} car runs at {self.speed} km/h with {self.fuel} fuel.")

# ✅ Create object of Car (inherits from Vehicle)
my_car = Car("Toyota", 120, "Petrol")
my_car.move()  # Output: Toyota car runs at 120 km/h with Petrol fuel.


# 🔊 A separate class for Music System
class MusicSystem:
    def play_music(self):
        print("Playing your favorite music!")

# 🚗 A Car has a MusicSystem — Composition
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        self.music_system = MusicSystem()  # 🎶 Composing MusicSystem

    def drive(self):
        print(f"{self.brand} is driving at {self.speed} km/h.")

    def enjoy_music(self):
        # 🎶 Using MusicSystem functionality via composition
        self.music_system.play_music()

# ✅ Create object of Car with a music system
my_car = Car("Honda", 100)
my_car.drive()         # Output: Honda is driving at 100 km/h.
my_car.enjoy_music()   # Output: Playing your favorite music!
