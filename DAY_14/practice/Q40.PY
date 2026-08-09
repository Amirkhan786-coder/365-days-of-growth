#  Student Gradebook

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())


student1 = Student("Amir", 88)
student2 = Student("Rahul", 76)
student3 = Student("Priya", 95)

student1.display()
print()

student2.display()
print()

student3.display()