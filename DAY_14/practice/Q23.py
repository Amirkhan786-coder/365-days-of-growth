# Multiple Employees

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


employee1 = Employee("Amir", 50000)
employee2 = Employee("Rahul", 45000)
employee3 = Employee("Priya", 60000)

employee1.display()
print()

employee2.display()
print()

employee3.display()