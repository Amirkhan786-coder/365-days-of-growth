#  Employee Salary

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12


employee1 = Employee("Amir", 50000)

print("Name:", employee1.name)
print("Monthly Salary:", employee1.salary)
print("Annual Salary:", employee1.annual_salary())