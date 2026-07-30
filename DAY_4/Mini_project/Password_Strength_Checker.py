# ===============================================
# Project : Password Strength Checker
# Day     : 04
# Author  : Amir Khan
# ===============================================

print("=" * 60)
print("        🔐 PASSWORD STRENGTH CHECKER")
print("=" * 60)

password = input("\nEnter your password: ")

uppercase = False
lowercase = False
digit = False
special = False

special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

# Check every character
for ch in password:

    if ch.isupper():
        uppercase = True

    elif ch.islower():
        lowercase = True

    elif ch.isdigit():
        digit = True

    elif ch in special_characters:
        special = True

# Calculate Score
score = 0

if len(password) >= 8:
    score += 1

if uppercase:
    score += 1

if lowercase:
    score += 1

if digit:
    score += 1

if special:
    score += 1

print("\n" + "=" * 60)
print("Password Analysis")
print("=" * 60)

print(f"Length             : {len(password)}")
print(f"Uppercase Present  : {uppercase}")
print(f"Lowercase Present  : {lowercase}")
print(f"Digit Present      : {digit}")
print(f"Special Character  : {special}")

print("\nPassword Score :", score, "/5")

# Password Strength
if score == 5:
    print("\n✅ Strength : STRONG")
elif score >= 3:
    print("\n⚠ Strength : MEDIUM")
else:
    print("\n❌ Strength : WEAK")

print("\nSuggestions to Improve:")

if len(password) < 8:
    print("• Use at least 8 characters.")

if not uppercase:
    print("• Add one uppercase letter.")

if not lowercase:
    print("• Add one lowercase letter.")

if not digit:
    print("• Add at least one number.")

if not special:
    print("• Add at least one special character.")

if score == 5:
    print("🎉 Excellent! Your password is secure.")

print("\nThank you for using Password Strength Checker!")
print("=" * 60)