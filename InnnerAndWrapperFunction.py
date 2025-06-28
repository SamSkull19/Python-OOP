# 🧪 A function that returns another function
def doubleFunc():
    print("Function Started Here")  # Executed when doubleFunc is called

    # 🔁 Inner function
    def insideFunc():
        print("Inside Function")    # This prints when insideFunc is called
        return 3000                 # Returns 3000

    print("Function Ended Here")    # End of outer function
    return insideFunc               # Returns the inner function itself


# 🔍 Calling doubleFunc returns a function, not its result yet
print(doubleFunc())                 # Output: prints start/end messages, returns function <insideFunc>
print(" ")

# 🔁 Now actually calling the returned function
print(doubleFunc()())               # Output: prints everything and finally prints 3000


# 🧪 Higher-order function: takes a function as a parameter
def doSomething(work):
    print("Function Started Here")
    work()                          # 👈 Calling the function passed in
    print("Function Ended Here")

# 🔧 Function to pass
def coding():
    print("Python")

# 🔁 Calling doSomething with coding as a function argument
doSomething(coding)

# 🔧 Another function to pass
def playingGames():
    print("Valorant")

# 🔁 Calling again with a different function
doSomething(playingGames)
