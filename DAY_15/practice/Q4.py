# Q4. Create a Person class and a Student child class.

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def display(self):
        print("Student Name:", self.name)


student1 = Student("Amir")
student1.display()