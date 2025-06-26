class Bank:
    def __init__(self, name, branch_id, balance):
        self.name = name              # Public attribute: account holder's name
        self._branch_id = branch_id   # Protected attribute: branch ID (can be accessed within subclasses)
        self.__balance = balance      # Private attribute: account balance (accessible only inside the class)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            return '⚠️ Enter a valid amount'

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            return '❌ Not enough money in balance'


karim = Bank('Karim', 'UCB-12', 40000)

karim.deposit(20000)
print('Current Balance : ', karim.get_balance())

karim.withdraw(50000)
print('Current Balance : ', karim.get_balance())

# 🔍 Shows all available attributes and methods of the object, including mangled private ones
print(dir(karim))

# 🔓 Accessing the private variable __balance using name mangling (not recommended in practice)
print(karim._Bank__balance)

"""
    The dir() function is a built-in Python function that:
    Returns a list of all the attributes and methods (including inherited ones) available for an object.

    Syntax:
        dir(object)
"""