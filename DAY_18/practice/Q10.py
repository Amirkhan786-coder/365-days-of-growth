# ============================================================
# Q10. FINALLY BLOCK
# Use try, except and finally.
# ============================================================

try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Invalid input.")

finally:
    print("Program completed.")