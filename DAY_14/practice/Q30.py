# Update Employee Salary

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee1 = Employee("Amir", 40000)

print("Old Salary:", employee1.salary)

employee1.salary = 50000

print("Updated Salary:", employee1.salary)