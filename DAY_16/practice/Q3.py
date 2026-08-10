# Q3. Function Returning Function
# Create a function outer() that returns an inner() function.


def outer():

    def inner():
        print("Hello from inner function!")

    return inner


result = outer()

result()