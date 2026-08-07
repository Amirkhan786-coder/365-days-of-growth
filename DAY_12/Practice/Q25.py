# Q25. Exception Chaining
# Question:
# Create a program where one exception causes another exception.
# Use: raise ... from e

try:

    number = int("Hello")

except ValueError as e:

    raise RuntimeError(
        "Unable to process the input."
    ) from e