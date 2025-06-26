# Vehicle Management System

class Vehicle_management:
    def __init__(self, name):
        self.name = name
        self.bus = []           # List of all buses
        self.counter = []       # List of all ticket counters
        self.routes = []        # List of available routes
        self.driver = []        # List of all drivers
        self.manager = []       # List of all managers
        self.supervisor = []    # List of all supervisors

    def add_Bus(self, bus):
        self.bus.append(bus)
        print(f'🚍 Bus : {bus.bus_number} added.')

    def add_Counter(self, counter):
        self.counter.append(counter)
        print(f'🏢 Counter : {counter.name} added.')

    def add_Routes(self, route):
        self.routes.append(route)
        print(f"🛣️ Route from {route['start']} to {route['end']} added.")

    def add_Driver(self, driver):
        self.driver.append(driver)
        print(f'🧑‍✈️ Driver : {driver.name} added.')

    def add_Manager(self, manager):
        self.manager.append(manager)
        print(f'👨‍💼 Manager : {manager.name} added.')

    def add_Supervisor(self, supervisor):
        self.supervisor.append(supervisor)
        print(f'🧑‍🔧 Supervisor : {supervisor.name} added.')

# -------------------------
# Related Classes
# -------------------------

class Driver:
    def __init__(self, name, license, age):
        self.name = name
        self.license = license
        self.age = age

class Manager:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Supervisor:
    def __init__(self, name, area):
        self.name = name
        self.area = area

class Counter:
    def __init__(self, name, location, vehicle_manager):
        self.name = name
        self.location = location
        self.vehicle_manager = vehicle_manager

    def purchaseTicket(self, start, destination):
        # Check if route is available
        available_routes = [
            route for route in self.vehicle_manager.routes
            if route['start'] == start and route['end'] == destination
        ]

        if available_routes:
            print(f"✅ Ticket purchased from {start} to {destination}")
        else:
            print(f"❌ No route available from {start} to {destination}")

class Bus:
    def __init__(self, bus_number, capacity, driver):
        self.bus_number = bus_number
        self.capacity = capacity
        self.driver = driver


# -------------------------
# ▶️ Example Usage
# -------------------------

# Create main vehicle management system
transport = Vehicle_management("GreenLine Transport")

# Add Driver
karim = Driver('Karim', '12456', 32)
transport.add_Driver(karim)

# Add Manager
rahim = Manager('Rahim', 'MGR-1001')
transport.add_Manager(rahim)

# Add Supervisor
salam = Supervisor('Salam', 'Sylhet Area')
transport.add_Supervisor(salam)

# Add Bus
bus1 = Bus('GL-101', 40, karim)
transport.add_Bus(bus1)

# Add Route
transport.add_Routes({'start': 'Dhaka', 'end': 'Sylhet'})

# Add Counter
counter1 = Counter('Main Counter', 'Dhaka', transport)
transport.add_Counter(counter1)

# Purchase Ticket
counter1.purchaseTicket('Dhaka', 'Sylhet')      # ✅ Should succeed
counter1.purchaseTicket('Dhaka', 'Chittagong')  # ❌ Should fail (no route)
