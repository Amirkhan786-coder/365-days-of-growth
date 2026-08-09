#Student Information

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


student1 = Student("Amir", 20, "CSE")

print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)