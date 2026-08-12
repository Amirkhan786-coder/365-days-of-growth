# ============================================================
# 🚀 DAY 18 / 365 — MINI PROJECT
# 🛡️ SMART ERROR HANDLER & FILE VALIDATOR
# ============================================================
#
# Concepts Used:
# - try
# - except
# - else
# - finally
# - raise
# - Custom Exceptions
# - ValueError
# - ZeroDivisionError
# - FileNotFoundError
# - PermissionError
# - OSError
# - File Handling
# - Input Validation
#
# ============================================================


# ============================================================
# CUSTOM EXCEPTION
# ============================================================

class InvalidNumberError(Exception):
    """Custom exception for invalid numbers."""
    pass


# ============================================================
# 1. SAFE DIVISION
# ============================================================

def safe_division():

    print("\n========== SAFE DIVISION ==========")

    try:

        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        result = first / second

    except ValueError:

        print("❌ Error: Please enter valid numbers.")

    except ZeroDivisionError:

        print("❌ Error: Cannot divide by zero.")

    else:

        print("✅ Division successful.")
        print("Result:", result)

    finally:

        print("Division operation completed.")


# ============================================================
# 2. NUMBER VALIDATION
# ============================================================

def validate_number():

    print("\n========== NUMBER VALIDATION ==========")

    try:

        value = input("Enter a number: ")

        number = float(value)

        if number < 0:

            raise InvalidNumberError(
                "Number cannot be negative."
            )

    except ValueError:

        print("❌ Error: Invalid number.")

    except InvalidNumberError as e:

        print("❌ Validation Error:", e)

    else:

        print("✅ Valid number:", number)

    finally:

        print("Number validation completed.")


# ============================================================
# 3. FILE VALIDATION AND READING
# ============================================================

def read_file():

    print("\n========== FILE VALIDATOR ==========")

    filename = input("Enter filename: ")

    try:

        with open(filename, "r") as file:

            content = file.read()

    except FileNotFoundError:

        print("❌ Error: File not found.")

    except PermissionError:

        print("❌ Error: Permission denied.")

    except OSError as e:

        print("❌ File System Error:", e)

    else:

        print("\n✅ File found successfully.")
        print("\n========== FILE CONTENT ==========")

        if content.strip():

            print(content)

        else:

            print("File is empty.")

    finally:

        print("\nFile operation completed.")


# ============================================================
# 4. MAIN MENU
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 55)
        print("       🛡️ SMART ERROR HANDLER & FILE VALIDATOR")
        print("=" * 55)

        print("\n1. Safe Division")
        print("2. Validate Number")
        print("3. Read File")
        print("4. Exit")

        print("=" * 55)

        try:

            choice = int(input("\nEnter your choice: "))

        except ValueError:

            print("\n❌ Error: Please enter a number from 1 to 4.")
            continue

        if choice == 1:

            safe_division()

        elif choice == 2:

            validate_number()

        elif choice == 3:

            read_file()

        elif choice == 4:

            print("\n" + "=" * 55)
            print("Thank you for using Smart Error Handler!")
            print("🚀 Day 18 Mini Project Completed!")
            print("=" * 55)

            break

        else:

            print("\n❌ Invalid choice.")
            print("Please select a number between 1 and 4.")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print("\n\nProgram interrupted by user.")

    finally:

        print("\nProgram execution finished.")