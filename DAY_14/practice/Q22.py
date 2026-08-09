# Three Students

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


student1 = Student("Amir", 85)
student2 = Student("Rahul", 90)
student3 = Student("Priya", 92)

student1.display()
print()

student2.display()
print()

student3.display()