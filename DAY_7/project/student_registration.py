# ==========================================
# Day 7 Mini Project
# Student Registration System Using Sets
# Author : Md Amir Khan
# ==========================================

students = set()

while True:

    print("\n" + "=" * 45)
    print("   STUDENT REGISTRATION SYSTEM")
    print("=" * 45)

    print("1. Register Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Total Students")
    print("6. Clear All Students")
    print("7. Exit")

    choice = input("\nEnter Your Choice (1-7): ")

    # Register Student
    if choice == "1":

        name = input("Enter Student Name: ").strip().title()

        if name == "":
            print("❌ Name cannot be empty!")

        elif name in students:
            print("⚠ Student Already Registered!")

        else:
            students.add(name)
            print("✅ Student Registered Successfully!")

    # Show Students
    elif choice == "2":

        if len(students) == 0:
            print("📂 No Students Registered.")

        else:
            print("\n📋 Registered Students:")

            count = 1
            for student in sorted(students):
                print(f"{count}. {student}")
                count += 1

    # Search Student
    elif choice == "3":

        name = input("Enter Student Name to Search: ").strip().title()

        if name in students:
            print("✅ Student Found.")
        else:
            print("❌ Student Not Found.")

    # Remove Student
    elif choice == "4":

        name = input("Enter Student Name to Remove: ").strip().title()

        if name in students:
            students.remove(name)
            print("🗑 Student Removed Successfully.")
        else:
            print("❌ Student Not Found.")

    # Count Students
    elif choice == "5":

        print("👨‍🎓 Total Registered Students :", len(students))

    # Clear All
    elif choice == "6":

        confirm = input("Are you sure? (yes/no): ").lower()

        if confirm == "yes":
            students.clear()
            print("🧹 All Students Removed Successfully.")
        else:
            print("Operation Cancelled.")

    # Exit
    elif choice == "7":

        print("\n🎉 Thank You for Using Student Registration System!")
        print("🚀 Happy Coding!")
        break

    else:
        print("❌ Invalid Choice! Please Enter 1 to 7.")