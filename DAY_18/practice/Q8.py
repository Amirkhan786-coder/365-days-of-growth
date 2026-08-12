# ============================================================
# Q8. TYPE ERROR
# Try adding an integer and a string.
# Handle TypeError.
# ============================================================

try:
    result = 10 + "Python"
    print("Result:", result)

except TypeError:
    print("Cannot add an integer and a string.")