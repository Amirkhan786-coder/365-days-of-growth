# ============================================================
# Q14. MULTIPLE EXCEPTIONS
# Handle ValueError and ZeroDivisionError.
# ============================================================

try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    result = first / second

    print("Result:", result)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")