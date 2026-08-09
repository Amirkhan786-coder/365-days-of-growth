# Constructor with Three Values

class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


student1 = Student("Amir", 20, 85)

print("Name:", student1.name)
print("Age:", student1.age)
print("Marks:", student1.marks)