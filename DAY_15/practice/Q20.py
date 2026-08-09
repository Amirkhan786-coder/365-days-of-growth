# Q20. Create a setter with marks validation from 0 to 100.

class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):

        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")


student1 = Student(80)

student1.set_marks(95)

print("Marks:", student1.get_marks())