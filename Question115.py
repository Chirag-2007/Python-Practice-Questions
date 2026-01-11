# Q36. Show First N Characters of a File (File Positioning)

n = int(input())

with open("info.txt","r") as f:
    final = f.read(n)
    print(final)

# Q37. Safe Division (Basic Exception Handling)

a,b = map(int,input().split())

try:
    final =  a / b
    print(final)
except ZeroDivisionError:
    print("Division by zero error")

# Q38. Integer Input with finally

try:
    n = int(input())
    print("You entered",n)
except ValueError:
    print("Invalid integer")
finally:
    print("Program End")

# Q39. Age Validation with User-Defined Exception

class UnderAgeError(Exception):
    pass
age = int(input())

try:
    if age < 18:
        raise UnderAgeError("Under age for voting")
    else:
        print("Eligible to vote")
except UnderAgeError as e:
    print(e)

# Q40. Student Inheritance Demo (OOP, Inheritance, Overriding, isinstance)

class Person:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print("Person:", self.name)

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def describe(self):
        print("Student:", self.name + ",", "Grade:", self.grade)

name = input().strip()
grade = input().strip()

s = Student(name, grade)
s.describe()
print("Is Person?", isinstance(s, Person))