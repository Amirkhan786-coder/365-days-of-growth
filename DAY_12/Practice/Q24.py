# Q24. Re-raise Exception
# Question:
# Catch a ValueError.
# Print a message.
# Then re-raise the same exception using raise.

try:

    number = int("Hello")

except ValueError:

    print("ValueError occurred.")
    print("Re-raising the exception...")

    raise