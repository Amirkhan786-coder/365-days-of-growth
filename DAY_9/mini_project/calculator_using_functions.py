# ==========================================
# Mini Project: Calculator Using Functions
# ==========================================

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Division by zero is not allowed!"
    return a / b


def modulus(a, b):
    return a % b


def power(a, b):
    return a ** b


while True:

    print("\n========== CALCULATOR USING FUNCTIONS ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    choice = input("\nEnter Your Choice (1-7): ")

    if choice == "7":
        print("\nThank You for Using the Calculator!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid Choice! Please Try Again.")
        continue

    num1 = float(input("Enter First Number : "))
    num2 = float(input("Enter Second Number: "))

    if choice == "1":
        print("Result =", addition(num1, num2))

    elif choice == "2":
        print("Result =", subtraction(num1, num2))

    elif choice == "3":
        print("Result =", multiplication(num1, num2))

    elif choice == "4":
        print("Result =", division(num1, num2))

    elif choice == "5":
        print("Result =", modulus(num1, num2))

    elif choice == "6":
        print("Result =", power(num1, num2))