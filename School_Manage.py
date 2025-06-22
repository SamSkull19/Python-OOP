from random import choice  # For random section assignment

# ------------------- Student Class -------------------
class Student:
    def __init__(self, name, section, id):
        self.name = name
        self.section = section
        self.id = id

    # String representation for printing student details
    def __repr__(self) -> str:
        return f"Student Name : {self.name} | Section : {self.section} | ID : {self.id}"


# ------------------- Teacher Class -------------------
class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    # String representation for printing teacher details
    def __repr__(self) -> str:
        return f"Teacher Name : {self.name} | Subject : {self.subject} | ID : {self.id}"


# ------------------- School Class -------------------
class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []   # List to store Teacher objects
        self.students = []   # List to store Student objects

    # Add a new teacher to the school
    def add_teachers(self, name, subject):
        id = len(self.teachers) + 101  # Unique teacher ID starting from 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    # Enroll a student if the fee is >= 5000
    def enroll(self, name, fee):
        if fee < 5000:
            return f"Not Enough Fee"
        else:
            id = len(self.students) + 1  # Unique student ID starting from 1
            section = choice(['A', 'B', 'C', 'D', 'E'])  # Random section assignment
            student = Student(name, section, id)
            self.students.append(student)
            return f"Student {name} enrolled with ID : {id}"

    # Display the full school report
    def __repr__(self) -> str:
        print(f"----------- Welcome to Our School {self.name} -----------") 
        print(f"----------- Our Teachers -----------") 
        for teacher in self.teachers:
            print(teacher)

        print(f"----------- Our Students -----------") 
        for student in self.students:
            print(student)

        return f"----------- All Done -----------" 


# ------------------- Test/Demo -------------------

# Create some sample standalone students
samin = Student('Samin', 'A', 10)
print(samin)

sifat = Student('Sifat', 'B', 101)
print(sifat)

# Create a School instance
a = School('NeffRoxx')

# Add some teachers
a.add_teachers('Mr. Rahman', 'Mathematics')
a.add_teachers('Ms. Farzana', 'English')
a.add_teachers('Dr. Hossain', 'Physics')

# Enroll some students
print(a.enroll('Kombul', 5000))   # Success
print(a.enroll('Toma', 4500))     # Should fail (fee too low)
print(a.enroll('Jamal', 6000))    # Success

# Print the full school summary
print(a)
