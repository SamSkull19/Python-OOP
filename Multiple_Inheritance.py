# 👨‍👩‍👧‍👦 Base Class 1: Family
class Family:
    def __init__(self, father_name, mother_name, address):
        self.father_name = father_name
        self.mother_name = mother_name
        self.address = address

    def family_info(self):
        return f'Father: {self.father_name} | Mother: {self.mother_name} | Address: {self.address}'


# 🏫 Base Class 2: School
class School:
    def __init__(self, school_name, grade, roll_number):
        self.school_name = school_name
        self.grade = grade
        self.roll_number = roll_number

    def school_info(self):
        return f'School: {self.school_name} | Grade: {self.grade} | Roll No: {self.roll_number}'


# 🏀 Base Class 3: Sports
class Sports:
    def __init__(self, favorite_sport, achievements):
        self.favorite_sport = favorite_sport
        self.achievements = achievements  # list of awards or titles

    def sports_info(self):
        titles = ', '.join(self.achievements) if self.achievements else "None"
        return f'Favorite Sport: {self.favorite_sport}, Achievements: {titles}'


# 👦 Derived Class: Student (Multiple Inheritance)
class Student(Family, School, Sports):
    def __init__(self, name, age, father_name, mother_name, address, school_name, grade, roll_number, favorite_sport, achievements):
        self.name = name
        self.age = age

        # Initialize all parent classes
        Family.__init__(self, father_name, mother_name, address)
        School.__init__(self, school_name, grade, roll_number)
        Sports.__init__(self, favorite_sport, achievements)

    def __repr__(self):
        return (f'👤 Student: {self.name} | Age: {self.age}\n' +
                self.family_info() + '\n' +
                self.school_info() + '\n' +
                self.sports_info())

student1 = Student(
    name = 'Sifat Samin',
    age = 20,
    father_name = 'Abdus Sabus',
    mother_name = 'Sharmin Akter',
    address = 'Sylhet, Bangladesh',
    school_name = 'Sylhet Engineering College',
    grade = '4th Year',
    roll_number = 12345,
    favorite_sport = 'Football',
    achievements = ['Best Player 2022', 'Captain 2023']
)

print(student1)