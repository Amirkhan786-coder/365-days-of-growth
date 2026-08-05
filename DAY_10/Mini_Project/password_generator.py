# ==========================================
# Mini Project: Strong Password Generator
# ==========================================

import random
import string


def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("=" * 45)
print("      🔐 STRONG PASSWORD GENERATOR")
print("=" * 45)

while True:

    length = int(input("\nEnter Password Length: "))

    if length < 4:
        print("Password should be at least 4 characters long.")
        continue

    password = generate_password(length)

    print("\nGenerated Password:")
    print(password)

    choice = input("\nGenerate Another Password? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank You for Using Password Generator ❤️")
        break