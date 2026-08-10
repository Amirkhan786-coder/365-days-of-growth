# Q9. List of Functions
# Create a list containing three functions and execute
# all functions using a loop.


def hello():
    print("Hello")


def welcome():
    print("Welcome")


def goodbye():
    print("Goodbye")


functions = [hello, welcome, goodbye]


for function in functions:
    function()