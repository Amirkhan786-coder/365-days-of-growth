# ============================================
# Project : Number Guessing Game
# Day     : 03
# Author  : Amir Khan
# ============================================

import random

print("=" * 60)
print("        🎮 NUMBER GUESSING GAME 🎮")
print("=" * 60)

print("\nChoose Difficulty Level")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-500)")

level = int(input("\nEnter your choice (1-3): "))

if level == 1:
    start = 1
    end = 50
elif level == 2:
    start = 1
    end = 100
elif level == 3:
    start = 1
    end = 500
else:
    print("\nInvalid Choice!")
    exit()

secret_number = random.randint(start, end)

attempts = 0

print(f"\nI have selected a number between {start} and {end}.")
print("Can you guess it?\n")

while True:

    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("📉 Too Low! Try Again.\n")

    elif guess > secret_number:
        print("📈 Too High! Try Again.\n")

    else:
        print("\n🎉 Congratulations!")
        print("You guessed the correct number.")
        print(f"Total Attempts : {attempts}")

        if attempts == 1:
            print("🏆 Incredible! First attempt!")
        elif attempts <= 5:
            print("🌟 Excellent Guessing Skills!")
        elif attempts <= 10:
            print("👍 Good Job!")
        else:
            print("💪 Keep Practicing!")

        break

print("\nThank you for playing!")
print("=" * 60)

choice = input("\nDo you want to play again? (yes/no): ")

if choice.lower() == "yes":
    print("\nRestart the program to play again.")
else:
    print("\n👋 Goodbye! Keep Coding.")