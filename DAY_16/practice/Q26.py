# Q26. Even Number Decorator
# Create a decorator that allows a function to execute
# only when the given number is even.


def even_only(function):

    def wrapper(number):

        if number % 2 == 0:
            return function(number)

        print("Only even numbers are allowed.")

    return wrapper


@even_only
def display(number):

    print("Number:", number)


display(20)
display(15)