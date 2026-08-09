# Company Name (Class Variable)

class Employee:

    company = "Tech Company"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("Company:", self.company)


employee1 = Employee("Amir")
employee2 = Employee("Rahul")

employee1.display()
print()

employee2.display()