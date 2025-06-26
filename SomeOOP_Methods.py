# 📚 Base Class: Book
class Book:
    def __init__(self, name):
        self.name = name  # Book name

    def read(self):
        # Abstract-like method (meant to be overridden in subclasses)
        raise NotImplementedError  # Raises error if not overridden


# 📘 Derived Class: English
class English(Book):
    def __init__(self, name, grammar):
        self.grammar = grammar  # Specific grammar topic
        super().__init__(name)  # Initialize base class Book

    def read(self):
        # Overridden method from Book class
        print(f'Complete : {self.grammar}')


# 📘 Create an object of English book
english = English('English', 'Tense')

# ✅ Check if English is a subclass of Book
print(issubclass(English, Book))     # True

# ✅ Check if english is an instance of English class
print(isinstance(english, English))  # True

# ✅ Check if english is also an instance of Book class
print(isinstance(english, Book))     # True

# ▶️ Call the read method
english.read()  # Output: Complete : Tense
