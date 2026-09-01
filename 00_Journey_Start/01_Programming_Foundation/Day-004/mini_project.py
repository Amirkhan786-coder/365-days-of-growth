# ==========================================
# 🚀 DAY 004 MINI PROJECT
# STUDENT INFORMATION & RESULT SYSTEM
# ==========================================


print("=" * 55)
print("          STUDENT INFORMATION & RESULT SYSTEM")
print("=" * 55)


# ==========================================
# 1. STUDENT INFORMATION
# ==========================================

name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
college = input("Enter College Name: ")
branch = input("Enter Branch: ")


# ==========================================
# 2. SUBJECT MARKS
# ==========================================

print("\nEnter Marks of Five Subjects")

subject1 = float(input("Subject 1: "))
subject2 = float(input("Subject 2: "))
subject3 = float(input("Subject 3: "))
subject4 = float(input("Subject 4: "))
subject5 = float(input("Subject 5: "))


# ==========================================
# 3. CALCULATIONS
# ==========================================

total_marks = (
    subject1
    + subject2
    + subject3
    + subject4
    + subject5
)

average_marks = total_marks / 5

percentage = (total_marks / 500) * 100


# ==========================================
# 4. DISPLAY STUDENT INFORMATION
# ==========================================

print("\n" + "=" * 55)
print("                 STUDENT DETAILS")
print("=" * 55)

print("Name       :", name)
print("Age        :", age)
print("College    :", college)
print("Branch     :", branch)


# ==========================================
# 5. DISPLAY SUBJECT MARKS
# ==========================================

print("\n" + "-" * 55)
print("                 SUBJECT MARKS")
print("-" * 55)

print("Subject 1  :", subject1)
print("Subject 2  :", subject2)
print("Subject 3  :", subject3)
print("Subject 4  :", subject4)
print("Subject 5  :", subject5)


# ==========================================
# 6. DISPLAY RESULT
# ==========================================

print("\n" + "-" * 55)
print("                    RESULT")
print("-" * 55)

print("Total Marks :", total_marks)
print("Average     :", average_marks)
print("Percentage  :", percentage, "%")


# ==========================================
# 7. FINAL MESSAGE
# ==========================================

print("\n" + "=" * 55)
print("       🎉 RESULT GENERATED SUCCESSFULLY!")
print("=" * 55)

print("\nKeep Learning.")
print("Keep Practicing.")
print("Keep Building. 🚀")

