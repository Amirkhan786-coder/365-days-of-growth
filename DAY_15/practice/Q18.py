# Q18. Create a getter method to access private-style data.

class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


student1 = Student(85)

print("Marks:", student1.get_marks())