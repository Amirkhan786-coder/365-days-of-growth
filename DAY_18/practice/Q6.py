# ============================================================
# Q6. STRING TO INTEGER
# Convert a string into an integer.
# ============================================================

value = "100"

try:
    number = int(value)
    print("Converted number:", number)

except ValueError:
    print("Cannot convert value to integer.")