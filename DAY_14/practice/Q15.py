# Employee Constructor

class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department


employee1 = Employee("Amir", 50000, "IT")

print("Employee Name:", employee1.name)
print("Salary:", employee1.salary)
print("Department:", employee1.department)