# Question: Create a function to check whether a number is Prime or Not.

def is_prime(num):

    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

number = 17

if is_prime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is Not a Prime Number")