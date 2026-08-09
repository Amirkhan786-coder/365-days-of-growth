# Constructor with Two Values

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Amir", 20)

print("Name:", student1.name)
print("Age:", student1.age)