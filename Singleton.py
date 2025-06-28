# 🧱 Singleton class to ensure only one instance is created
class Singleton:
    # 🔐 Private class variable to hold the single instance
    __instance = None

    def __init__(self):
        # 🔁 Check if an instance already exists
        if Singleton.__instance is None:
            Singleton.__instance = self   # ✅ Assign current object as the single instance
        else:
            # ❌ Raise exception if trying to create a second instance
            raise Exception('Singleton already has an instance')

    # 🔧 Static method to get the single instance of the class
    @staticmethod
    def get_Instance():
        # 🔍 If no instance exists, create one
        if Singleton.__instance is None:
            Singleton()
        # ✅ Return the already created instance
        return Singleton.__instance


# 🔁 First call: Creates the instance
a = Singleton.get_Instance()
print(a)   # Prints the memory address of the instance

# 🔁 Second call: Returns the same instance (not a new one)
b = Singleton.get_Instance()
print(b)   # Same address as 'a'
