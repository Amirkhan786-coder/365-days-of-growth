# ============================================
# DAY 12 - MINI PROJECT
# SAFE CALCULATOR
# Python Exception Handling
# ============================================


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


while True:

    print("\n================================")
    print("       SAFE CALCULATOR")
    print("================================")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:

        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("\nCalculator closed.")
            print("Thank you for using Safe Calculator!")
            break

        if choice not in [1, 2, 3, 4]:
            raise ValueError(
                "Invalid choice. Please select 1 to 5."
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

    except ValueError as e:

        print("\nInput Error:", e)

    except ZeroDivisionError as e:

        print("\nCalculation Error:", e)

    except Exception as e:

        print("\nUnexpected Error:", e)

    else:

        print("\n--------------------------------")
        print("Result:", result)
        print("--------------------------------")

    finally:

        print("Operation completed.")