print("=" * 50)
print("      MARKS PERCENTAGE CALCULATOR")
print("=" * 50)

student_name = input("Enter Student Name: ")

subject1 = float(input("Enter Marks of Subject 1: "))
subject2 = float(input("Enter Marks of Subject 2: "))
subject3 = float(input("Enter Marks of Subject 3: "))
subject4 = float(input("Enter Marks of Subject 4: "))
subject5 = float(input("Enter Marks of Subject 5: "))

total = subject1 + subject2 + subject3 + subject4 + subject5

percentage = total / 5

print("\n" + "=" * 50)
print("           RESULT")
print("=" * 50)

print(f"Student Name : {student_name}")
print(f"Total Marks  : {total}")
print(f"Percentage   : {percentage}%")

print("=" * 50)
print("Calculation Completed Successfully ✅")
print("=" * 50)