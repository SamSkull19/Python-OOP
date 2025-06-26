# 🏦 Bank Class
class Bank:
    def __init__(self, name, branch_id, balance):
        self.name = name              # Public attribute: account holder's name
        self._branch_id = branch_id   # Protected attribute: branch ID (can be accessed within subclasses)
        self.__balance = balance      # Private attribute: account balance (accessible only inside the class)

    # ➕ Deposit Method
    def deposit(self, amount):
        if amount > 0:                # Only allow positive amounts
            self.__balance += amount  # Add deposit amount to balance
        else:
            return '⚠️ Enter a valid amount'

    # 💰 Getter Method for Balance
    def get_balance(self):
        return self.__balance         # Return current balance (private variable accessed via method)

    # ➖ Withdraw Method
    def withdraw(self, amount):
        if amount <= self.__balance:  # Check if balance is sufficient
            self.__balance -= amount  # Subtract amount
        else:
            return '❌ Not enough money in balance'

# ------------------------------
# ▶️ Example Usage
# ------------------------------

# Create a Bank account for Karim with initial balance 40,000
karim = Bank('Karim', 'UCB-12', 40000)

# Deposit 20,000
karim.deposit(20000)

# Print current balance after deposit
print('Current Balance : ', karim.get_balance())  # Expected: 60000

# Try to withdraw 50,000
karim.withdraw(50000)

# Print current balance after withdrawal
print('Current Balance : ', karim.get_balance())  # Expected: 10000
