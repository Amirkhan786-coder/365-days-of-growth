# Q10. Function Factory
# Create a function that returns different functions
# for addition and multiplication.


def calculator(operation):

    if operation == "add":

        def add(a, b):
            return a + b

        return add

    elif operation == "multiply":

        def multiply(a, b):
            return a * b

        return multiply


addition = calculator("add")
multiplication = calculator("multiply")

print("Addition:", addition(10, 5))
print("Multiplication:", multiplication(10, 5))