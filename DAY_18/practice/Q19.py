# ============================================================
# Q19. MULTIPLE EXCEPTION BLOCKS
# Demonstrate ValueError, TypeError and ZeroDivisionError.
# ============================================================

try:
    number = int(input("Enter a number: "))

    result = 100 / number

    print("Result:", result)

except ValueError:
    print("ValueError: Invalid number.")

except TypeError:
    print("TypeError: Invalid data type.")

except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")