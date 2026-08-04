# Question: Create a function that accepts multiple positional arguments using *args.

def numbers(*num):
    for i in num:
        print(i)

numbers(10, 20, 30, 40, 50)