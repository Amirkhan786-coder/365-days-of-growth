# Q4. Nested Function
# Create a function containing another function
# and call the inner function from the outer function.


def outer():

    print("This is the outer function.")

    def inner():
        print("This is the inner function.")

    inner()


outer()