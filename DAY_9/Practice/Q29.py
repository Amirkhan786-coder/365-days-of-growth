# Question: Create a function that returns the largest of three numbers.

def largest(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c

print(largest(45, 78, 62))