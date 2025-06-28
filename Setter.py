# 👤 Define the Person class
class Person:
    def __init__(self, name, age, salary):
        self.name = name          # Public attribute
        self._age = age           # 🔐 Protected attribute (conventionally private)
        self.__salary = salary    # 🔒 Private attribute (name mangled)

    # 📤 Normal method to return age
    def age(self):
        return self._age
    
    # 📤 Property: read age as if it's a variable
    @property
    def ageAt(self):
        return self._age

    # ✍️ Setter for ageAt property: update _age
    @ageAt.setter
    def setAge(self, newAge):
        self._age = newAge
        return self._age
    
    # 📤 Normal method to return salary
    def salary(self):
        return self.__salary    
    
    # 📤 Property: read salary as if it's a variable
    @property
    def salaryAt(self):
        return self.__salary

    # ✍️ Setter for salaryAt: safely increase salary
    @salaryAt.setter
    def setSalary(self, amount):
        if amount < 0:
            return f'Salary can not be Negative'  # Validation check
        else:
            self.__salary += amount              # Add to salary


# 👤 Create instance of Person
sam = Person('Samin', 24, 20000)

# ✅ Access age using method
print(sam.age())           # Output: 24

# ✅ Set new age using setter
sam.setAge = 27

# ✅ Read updated age using property
print(sam.ageAt)           # Output: 27

# ✅ Access salary using method
print(sam.salary())        # Output: 20000

# ✅ Increase salary using setter
sam.setSalary = 4500

# ✅ Access updated salary using property
print(sam.salaryAt)        # Output: 24500
