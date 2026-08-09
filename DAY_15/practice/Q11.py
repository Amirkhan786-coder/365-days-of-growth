# Q11. Create Person -> Student -> CollegeStudent using multilevel inheritance.

class Person:

    def person_info(self):
        print("This is a person")


class Student(Person):

    def student_info(self):
        print("This is a student")


class CollegeStudent(Student):

    def college_info(self):
        print("This is a college student")


student1 = CollegeStudent()

student1.person_info()
student1.student_info()
student1.college_info()