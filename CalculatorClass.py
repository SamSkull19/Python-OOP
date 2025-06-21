# Define a class named Calculator
class Calculator:
    # Class attribute (shared by all instances)
    brand = "Casio"

    # Instance method to add two numbers
    def addNum(self, num1, num2):
        return num1 + num2

    # Instance method to subtract second number from the first
    def subNum(self, num1, num2):
        return num1 - num2

    # Instance method to multiply two numbers
    def mulNum(self, num1, num2):
        return num1 * num2

    # Instance method to divide num1 by num2
    def divNum(self, num1, num2):
        # Check if num2 is greater than 0 to avoid division by zero
        if num2 > 0:
            return num1 / num2
        else:
            return "Math Error"  # Return error message if division is not possible

# Create an object (instance) of Calculator class
calculation = Calculator()

# Take two integer inputs from the user using space-separated input
a, b = map(int, input().split())

# Call the addNum method and print the result
sum = calculation.addNum(a, b)
print("Summation : ", sum)

# Call the subNum method and print the result
sub = calculation.subNum(a, b)
print("Subtract : ", sub)

# Call the mulNum method and print the result
mul = calculation.mulNum(a, b)
print("Multiplication : ", mul)

# Call the divNum method and print the result
div = calculation.divNum(a, b)
print("Division : ", div)
