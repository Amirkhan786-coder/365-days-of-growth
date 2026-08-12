# ============================================================
# Q27. MENU-DRIVEN PROGRAM
# Create a basic calculator menu.
# ============================================================

try:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        print("Program exited.")

    elif choice in [1, 2, 3, 4]:

        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", first + second)

        elif choice == 2:
            print("Result:", first - second)

        elif choice == 3:
            print("Result:", first * second)

        elif choice == 4:
            print("Result:", first / second)

    else:
        raise ValueError("Invalid menu choice.")

except ValueError as e:
    print("Error:", e)

except ZeroDivisionError:
    print("Cannot divide by zero.")