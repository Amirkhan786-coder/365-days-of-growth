# Change Student Age

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Amir", 20)

print("Old Age:", student1.age)

student1.age = 21

print("Updated Age:", student1.age)