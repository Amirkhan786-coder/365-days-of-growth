# Add New Attribute
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Amir", 20)

# Adding a new attribute
student1.course = "CSE"

print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)