# 🧭 Decorator function
def timer(func):
    # 🧩 Inner wrapper function
    def inner():
        print("Function Started Here")  # Executed before the original function
        func()                          # Call the original function
        print("Function Ended Here")    # Executed after the original function
    return inner                        # Return the wrapper

# 🔁 Apply the decorator using @timer
@timer
def work():
    print("Solving Math Problems")

# 🚀 Call the decorated function
work()

# 🔁 Equivalent to: work = timer(work)
# work()


# 🧭 Define a decorator that logs function calls
def logFunction(func):  # 'func' is the function being decorated
    # 🧩 Define the wrapper function (the new behavior)
    def wrapper():
        # 📋 Log before calling the original function
        print(f"Calling function: {func.__name__}")  # Shows the name of the function
        func()  # 🛠️ Call the actual function
        # ✅ Log after function execution
        print(f"Function {func.__name__} finished.\n")
    return wrapper  # Return the wrapper function

# 🎮 Apply the logFunction decorator to playGame
@logFunction
def playGame():
    print("Playing Valorant")  # Core logic of playGame

# 📝 Apply the logFunction decorator to doHomework
@logFunction
def doHomework():
    print("Solving Data Structures")  # Core logic of doHomework

# 🚀 Call the decorated functions
playGame()     # Will show logging before and after
doHomework()   # Will also show logging

