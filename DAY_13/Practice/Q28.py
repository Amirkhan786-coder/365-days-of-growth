# Q28. Import a function from a package module.

# Folder:
# student/
#     __init__.py
#     details.py

# details.py

def show_name():
    print("Name: Amir")


# main.py

from student.details import show_name

show_name()