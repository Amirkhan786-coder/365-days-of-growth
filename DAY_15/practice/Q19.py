# Question:
# Print all key-value pairs using a for loop.

student = {
    "Name": "Amir",
    "Age": 19,
    "City": "Meerut"
}

for key, value in student.items():
    print(key, ":", value)
    # Q19. Create a setter method to update private-style data.

class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks


student1 = Student(80)

print("Old Marks:", student1.get_marks())

student1.set_marks(95)

print("New Marks:", student1.get_marks())