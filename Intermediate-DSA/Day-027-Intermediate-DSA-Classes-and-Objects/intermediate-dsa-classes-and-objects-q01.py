# Basics of Classes

class Student:
    name = "student_name"
    id = "student_id"
    
    def print_fn(self):
        print(f"name = {self.name}")
        print(f"id = {self.id}")
        
s1 = Student()
print(s1.name)
print(s1.id)
s1.print_fn()