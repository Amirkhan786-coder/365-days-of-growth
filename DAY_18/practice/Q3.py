# ============================================================
# Q3. SAFE DIVISION
# Handle ValueError and ZeroDivisionError.
# ============================================================

try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    result = first / second

    print("Result:", result)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")