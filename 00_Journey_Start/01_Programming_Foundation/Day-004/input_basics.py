# Day 004 - Python Input Basics


# ==========================================
# 1. Taking a Name
# ==========================================

name = input("Enter your name: ")

print("Hello", name)


# ==========================================
# 2. Taking Multiple Inputs
# ==========================================

college = input("Enter your college name: ")
branch = input("Enter your branch: ")
semester = input("Enter your semester: ")

print("\n----- STUDENT INFORMATION -----")

print("Name:", name)
print("College:", college)
print("Branch:", branch)
print("Semester:", semester)


# ==========================================
# 3. Taking City
# ==========================================

city = input("\nEnter your city: ")

print("City:", city)


# ==========================================
# 4. Checking Input Data Type
# ==========================================

user_input = input("\nEnter anything: ")

print("You entered:", user_input)
print("Data type:", type(user_input))


# ==========================================
# 5. Taking Career Goal
# ==========================================

goal = input("\nEnter your career goal: ")

print("Your career goal is:", goal)


# ==========================================
# 6. Simple Personal Introduction
# ==========================================

print("\n========== PERSONAL INTRODUCTION ==========")

name = input("Enter your name: ")
college = input("Enter your college: ")
branch = input("Enter your branch: ")
goal = input("Enter your career goal: ")

print("\nHello! My name is", name)
print("I am studying at", college)
print("My branch is", branch)
print("My career goal is", goal)

print("===========================================")