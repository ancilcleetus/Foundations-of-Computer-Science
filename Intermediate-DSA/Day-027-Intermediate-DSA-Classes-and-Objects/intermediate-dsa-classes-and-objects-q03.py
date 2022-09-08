# Class with __init__ method as constructor

class Student:
    # Class variable
    type = "Student"
    
    # Constructor
    def __init__(self, name, id):
        # Instance variables
        self.name = name
        self.id = id
        
    def addSubject(self, subject):
        self.subject = subject
        
    def getSubject(self):
        return self.subject
    
    def print_fn(self):
        print(f"name = {self.name}")
        print(f"id = {self.id}")
        
s1 = Student("Ancil", 1)
print("Details of s1:")
print(f"s1 is a {s1.type}")
print(f"Name of s1 is {s1.name}")
print(f"ID of s1 is {s1.id}")

s1.addSubject("Maths")
print(f"Subject of s1 is {s1.getSubject()}")

# Class variables can be accessed using class name also
print("\nAccessing class variable using class name")
print(f"Type of Student = {Student.type}")