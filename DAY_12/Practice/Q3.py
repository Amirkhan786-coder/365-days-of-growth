# Q3. Handle TypeError
# Question:
# Create an example that produces TypeError
# and handle it using try-except.

try:
    result = "10" + 5
    print(result)

except TypeError:
    print("Cannot add a string and an integer.")