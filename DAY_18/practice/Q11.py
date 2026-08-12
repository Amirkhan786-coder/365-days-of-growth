# ============================================================
# Q11. POSITIVE NUMBER VALIDATOR
# Raise ValueError if the number is negative.
# ============================================================

try:
    number = float(input("Enter a positive number: "))

    if number < 0:
        raise ValueError("Number cannot be negative.")

    print("Valid number:", number)

except ValueError as e:
    print("Error:", e)