from math import factorial
import time

# 🧭 Define a decorator function that measures execution time
def timer(func):
    # 🧩 Wrapper function accepts any arguments using *args and **kwargs
    def inner(*args, **kwargs):
        print("Function Started Here")

        # ⏱️ Record the start time
        start = time.time()

        # ▶️ Call the original function with all arguments passed
        func(*args, **kwargs)

        # ⏱️ Record the end time
        end = time.time()

        print("Function Ended Here")

        # 🕒 Print total execution time
        print(f"Total Time Taken : {end - start}")

    # 🏁 Return the wrapped function
    return inner

# 📦 Decorate the getFactorial function with @timer
@timer
def getFactorial(n):
    print("Factorial Started Here")

    # 🔁 Compute factorial using built-in math.factorial
    ans = factorial(n)

    # 🖨️ Print the result
    print(f"Factorial of Number {n} : {ans}")

# 🚀 Call the decorated function using positional argument
getFactorial(5)

# 🚀 Call the decorated function using keyword argument
getFactorial(n = 7)
