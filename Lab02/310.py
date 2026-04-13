class Person:
    def __init__(self, name):
       
        self.name = name

class Student(Person):
    def __init__(self, name, gpa):
     
        super().__init__(name)
        
        self.gpa = gpa

    def display(self):
       
        print(f"Student: {self.name}, GPA: {self.gpa}")

try:
    line = input().split()
    if len(line) >= 2:
        
        name = line[0]
        gpa = line[1]
        
        student_obj = Student(name, gpa)
       
        student_obj.display()
except EOFError:
    pass