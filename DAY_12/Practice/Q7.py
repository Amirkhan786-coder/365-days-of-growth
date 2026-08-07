# Q7. Use finally
# Question:
# Create a program that demonstrates
# that finally always executes.

try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Invalid input.")

finally:
    print("Finally block executed.")