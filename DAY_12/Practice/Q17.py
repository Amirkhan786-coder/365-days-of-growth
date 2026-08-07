# Q17. try-except-else-finally
# Question:
# Create a program using:
# try
# except
# else
# finally

try:

    number = int(input("Enter number: "))

    result = 100 / number

except ValueError:

    print("Invalid input.")

except ZeroDivisionError:

    print("Cannot divide by zero.")

else:

    print("Result:", result)

finally:

    print("Program completed.")