# Question: Create a function that returns whether a number is even or odd.

def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check(12))