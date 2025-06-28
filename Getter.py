# 👤 Define the Person class
class Person:
    def __init__(self, name, age, salary):
        self.name = name          # Public attribute
        self._age = age           # 🔐 Protected attribute (conventionally)
        self.__salary = salary    # 🔒 Private attribute (name mangled)

    # 📤 Normal getter method for protected attribute
    def age(self):
        return self._age
    
    # 📤 Read-only property (acts like a variable)
    @property
    def ageAt(self):
        return self._age
    
    # 📤 Normal getter method for private attribute
    def salary(self):
        return self.__salary    
    
    # 📤 Read-only property for private salary
    @property
    def salaryAt(self):
        return self.__salary


# 👤 Create an instance of Person
sam = Person('Samin', 24, 20000)

# ✅ Calling normal method to get age
print(sam.age())         # Output: 24

# ✅ Calling property (read-only)
print(sam.ageAt)         # Output: 24

# ✅ Calling normal method to get private salary
print(sam.salary())      # Output: 20000

# ✅ Calling property for private salary
print(sam.salaryAt)      # Output: 20000

# ❌ The following would cause error:
# print(sam.__salary)     # AttributeError: 'Person' object has no attribute '__salary'
