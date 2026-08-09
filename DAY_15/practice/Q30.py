# Q30. Create a complete OOP program using inheritance, polymorphism and encapsulation.

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def work(self):
        print(self.name, "is working")


class Developer(Employee):

    def work(self):
        print(self.name, "is developing software")


class Designer(Employee):

    def work(self):
        print(self.name, "is designing UI")


developer = Developer("Amir", 50000)
designer = Designer("Rahul", 45000)

developer.work()
designer.work()

print("Developer Salary:", developer.get_salary())
print("Designer Salary:", designer.get_salary())