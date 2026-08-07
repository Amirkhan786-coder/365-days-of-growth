# Q9. Exception Object
# Question:
# Catch an exception using 'as e'
# and print the error message.

try:
    result = 10 / 0
    print(result)

except ZeroDivisionError as e:
    print("Error:", e)