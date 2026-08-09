# School Name (Class Variable)

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("School:", self.school)


student1 = Student("Amir")
student2 = Student("Rahul")

student1.display()
print()

student2.display()