# Question: Create a function that checks whether a number is positive, negative, or zero.

def check(num):

    if num > 0:
        return "Positive"

    elif num < 0:
        return "Negative"

    else:
        return "Zero"

print(check(-15))