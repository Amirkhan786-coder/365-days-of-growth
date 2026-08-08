# Q26. Create a reusable module.

# File: greeting.py

def greet(name):
    print("Hello,", name)


if __name__ == "__main__":
    greet("Amir")


# File: main.py

import greeting

greeting.greet("Rahul")