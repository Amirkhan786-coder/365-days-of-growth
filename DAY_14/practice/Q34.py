# Check Pass or Fail

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"


student1 = Student("Amir", 75)

print("Name:", student1.name)
print("Marks:", student1.marks)
print("Result:", student1.check_result())