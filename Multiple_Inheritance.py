# 🚗 Base Class: Vehicle
class Vehicle:
    def __init__(self, type, company, wheel, doors):
        self.type = type            # Type of vehicle
        self.company = company      # Vehicle manufacturer
        self.wheel = wheel          # Number of wheels
        self.doors = doors          # Number of doors

    def run(self):
        # Common method for all vehicles
        return f'🚘 Running Vehicle: {self.type}'


# 🚌 Level 1: Bus inherits from Vehicle
class Bus(Vehicle):
    def __init__(self, type, company, wheel, doors, owner, seats):
        self.owner = owner          # Owner of the bus
        self.seats = seats          # Number of seats
        super().__init__(type, company, wheel, doors)

    def __repr__(self):
        return (f'Bus Type : {self.type} | Company : {self.company} | '
                f'Wheels : {self.wheel} | Doors : {self.doors} | '
                f'Owner : {self.owner} | Seats : {self.seats}')


# 🚐 Level 2: MiniBus inherits from Bus → Multilevel Inheritance
class MiniBus(Bus):
    def __init__(self, type, company, wheel, doors, owner, seats, route):
        self.route = route          # Assigned route
        super().__init__(type, company, wheel, doors, owner, seats)

    def __repr__(self):
        return (f'MiniBus Type : {self.type} | Company : {self.company} | '
                f'Wheels : {self.wheel} | Doors : {self.doors} | '
                f'Owner : {self.owner} | Seats : {self.seats} | Route : {self.route}')


# 🚛 Level 1: Truck inherits from Vehicle
class Truck(Vehicle):
    def __init__(self, type, company, wheel, doors, capacity):
        self.capacity = capacity    # Load capacity in tons
        super().__init__(type, company, wheel, doors)

    def __repr__(self):
        return (f'Truck Type : {self.type} | Company : {self.company} | '
                f'Wheels : {self.wheel} | Doors : {self.doors} | '
                f'Capacity : {self.capacity} Tons')


# 🚙 Level 2: Jeep inherits from Truck → Multilevel Inheritance
class Jeep(Truck):
    def __init__(self, type, company, wheel, doors, capacity, model):
        self.model = model          # Jeep model or name
        super().__init__(type, company, wheel, doors, capacity)

    def __repr__(self):
        return (f'Jeep Type : {self.type} | Company : {self.company} | '
                f'Wheels : {self.wheel} | Doors : {self.doors} | '
                f'Capacity : {self.capacity} Tons | Model : {self.model}')


# -------------------------------
# ▶️ Object Creation & Testing
# -------------------------------

# ✅ MiniBus object
greenline_mini = MiniBus(
    type='MiniBus',
    company='GreenLine',
    wheel=4,
    doors=2,
    owner='Mr. Rahman',
    seats=18,
    route='Route-7'
)
print(greenline_mini)
print(greenline_mini.run())

# ✅ Truck object
cargo_truck = Truck(
    type='Truck',
    company='Tata',
    wheel=10,
    doors=2,
    capacity=20
)
print(cargo_truck)
print(cargo_truck.run())

# ✅ Jeep object
army_jeep = Jeep(
    type='Jeep',
    company='Mahindra',
    wheel=4,
    doors=4,
    capacity=2,
    model='XUV700'
)
print(army_jeep)
print(army_jeep.run())
