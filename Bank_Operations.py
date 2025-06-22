# Define a class named Bank to manage a user's bank account
class Bank:
    def __init__(self, balance):
        # Initialize the account with a starting balance
        self.balance = balance
        # Set the maximum amount allowed to withdraw at once
        self.max_Withdraw = 1000000
        # Set the minimum amount allowed to withdraw
        self.min_Withdraw = 100

    # Method to return the current balance
    def getBalance(self):
        return self.balance

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:  # Only deposit if amount is positive
            self.balance += amount

    # Method to withdraw money from the account
    def withdraw(self, amount):
        # Check if the amount is below the minimum withdrawal limit
        if amount < self.min_Withdraw:
            return f'You can not withdraw below {self.min_Withdraw}'
        
        # Check if the amount exceeds the maximum withdrawal limit
        elif amount > self.max_Withdraw:
            return f'You can not withdraw more than {self.max_Withdraw}'
        
        else:
            # Subtract the amount from balance and return success message
            self.balance -= amount
            return f'Money withdrawn : {amount} \nCurrent Balance : {self.balance}'

# Create a Bank object with an initial balance of 500,000
JBL = Bank(500000)

# Get and print the current balance
currentBalance = JBL.getBalance()
print(currentBalance)

# Deposit 20,000 into the account
JBL.deposit(20000)

# Get and print the new balance
currentBalance = JBL.getBalance()
print(currentBalance)

# Attempt to withdraw 400,000 and print the result
withdraw = JBL.withdraw(400000)
print(withdraw)

# Get and print the final balance
currentBalance = JBL.getBalance()
print(currentBalance)
