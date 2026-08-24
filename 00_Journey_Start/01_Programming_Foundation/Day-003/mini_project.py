# Day 003 Mini Project
# Personal Profile Generator

print("=" * 45)
print("     PERSONAL PROFILE GENERATOR")
print("=" * 45)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
college = input("Enter your college name: ")
branch = input("Enter your branch: ")
semester = int(input("Enter your semester: "))

print("\n" + "=" * 45)
print("          YOUR PROFILE")
print("=" * 45)

print("Name:", name)
print("Age:", age)
print("College:", college)
print("Branch:", branch)
print("Semester:", semester)

print("=" * 45)

print("\nData Types:")

print("Name:", type(name))
print("Age:", type(age))
print("Semester:", type(semester))