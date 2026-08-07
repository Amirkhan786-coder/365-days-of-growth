# Q30. Safe Calculator
# Question:
# Create a calculator with:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
#
# Handle invalid input and division by zero.
# Use try, except and finally.

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:

        raise ZeroDivisionError(
            "Cannot divide by zero."
        )

    return a / b


while True:

    print("\n===== SAFE CALCULATOR =====")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:

        choice = int(input("Enter your choice: "))

        if choice == 5:

            print("Calculator closed.")
            break

        if choice not in [1, 2, 3, 4]:

            raise ValueError(
                "Invalid choice."
            )

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:

            result = add(num1, num2)

        elif choice == 2:

            result = subtract(num1, num2)

        elif choice == 3:

            result = multiply(num1, num2)

        elif choice == 4:

            result = divide(num1, num2)

        print("Result:", result)

    except ValueError as e:

        print("Input Error:", e)

    except ZeroDivisionError as e:

        print("Calculation Error:", e)

    except Exception as e:

        print("Unexpected Error:", e)

    finally:

        print("Operation completed.")