# College Name

class Student:

    college = "Shobhit University"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("College:", self.college)


student1 = Student("Amir")
student2 = Student("Rahul")
student3 = Student("Priya")

student1.display()
print()

student2.display()
print()

student3.display()