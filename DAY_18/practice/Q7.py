# ============================================================
# Q7. INVALID INTEGER
# Try converting 'Python' into an integer.
# Handle ValueError.
# ============================================================

value = "Python"

try:
    number = int(value)
    print("Number:", number)

except ValueError:
    print("Python cannot be converted into an integer.")