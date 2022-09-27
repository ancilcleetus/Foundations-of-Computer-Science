# Class with __init__ method as constructor

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def print_fn(self):
        print(f"name = {self.name}")
        print(f"id = {self.id}")
        
s1 = Student("Ancil", 1)
print(s1.name)
print(s1.id)
s1.print_fn()