# ============================================================
# Q21. CALCULATOR WITH EXCEPTION HANDLING
# Create a calculator for +, -, * and /.
# ============================================================

try:
    first = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    second = float(input("Enter second number: "))

    if operator == "+":
        result = first + second

    elif operator == "-":
        result = first - second

    elif operator == "*":
        result = first * second

    elif operator == "/":
        result = first / second

    else:
        raise ValueError("Invalid operator.")

    print("Result:", result)

except ValueError as e:
    print("Error:", e)

except ZeroDivisionError:
    print("Cannot divide by zero.")