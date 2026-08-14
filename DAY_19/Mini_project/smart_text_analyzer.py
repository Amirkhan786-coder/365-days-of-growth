
# ============================================================
# DAY 19 MINI PROJECT
# SMART TEXT ANALYZER
# ============================================================

import re
from collections import Counter


# ============================================================
# GET USER INPUT
# ============================================================

text = input("\nEnter your paragraph:\n")


# ============================================================
# EXTRACT WORDS
# ============================================================

words = re.findall(
    r"\b\w+\b",
    text.lower()
)


# ============================================================
# BASIC STATISTICS
# ============================================================

total_words = len(words)

unique_words = len(set(words))


# ============================================================
# WORD FREQUENCY
# ============================================================

word_frequency = Counter(words)


# ============================================================
# TOP 5 WORDS
# ============================================================

top_words = word_frequency.most_common(5)


# ============================================================
# EXTRACT NUMBERS
# ============================================================

numbers = re.findall(
    r"\d+",
    text
)


# ============================================================
# EXTRACT EMAILS
# ============================================================

emails = re.findall(
    r"[\w.-]+@[\w.-]+\.\w+",
    text
)


# ============================================================
# EXTRACT URLs
# ============================================================

urls = re.findall(
    r"https?://[^\s]+",
    text
)


# ============================================================
# EXTRACT HASHTAGS
# ============================================================

hashtags = re.findall(
    r"#\w+",
    text
)


# ============================================================
# EXTRACT MENTIONS
# ============================================================

mentions = re.findall(
    r"@\w+",
    text
)


# ============================================================
# CHARACTER FREQUENCY
# ============================================================

character_frequency = Counter(
    character.lower()
    for character in text
    if not character.isspace()
)


# ============================================================
# DISPLAY HEADER
# ============================================================

print("\n")
print("=" * 55)
print("              SMART TEXT ANALYZER")
print("=" * 55)


# ============================================================
# BASIC STATISTICS
# ============================================================

print("\n--- BASIC STATISTICS ---")

print("Total Words:", total_words)

print("Unique Words:", unique_words)


# ============================================================
# TOP 5 WORDS
# ============================================================

print("\n--- TOP 5 WORDS ---")

if top_words:

    for word, count in top_words:
        print(f"{word} -> {count}")

else:

    print("No words found.")


# ============================================================
# NUMBERS
# ============================================================

print("\n--- NUMBERS ---")

if numbers:

    for number in numbers:
        print(number)

else:

    print("No numbers found.")


# ============================================================
# EMAILS
# ============================================================

print("\n--- EMAILS ---")

if emails:

    for email in emails:
        print(email)

else:

    print("No emails found.")


# ============================================================
# URLs
# ============================================================

print("\n--- URLs ---")

if urls:

    for url in urls:
        print(url)

else:

    print("No URLs found.")


# ============================================================
# HASHTAGS
# ============================================================

print("\n--- HASHTAGS ---")

if hashtags:

    for hashtag in hashtags:
        print(hashtag)

else:

    print("No hashtags found.")


# ============================================================
# MENTIONS
# ============================================================

print("\n--- MENTIONS ---")

if mentions:

    for mention in mentions:
        print(mention)

else:

    print("No mentions found.")


# ============================================================
# CHARACTER FREQUENCY
# ============================================================

print("\n--- CHARACTER FREQUENCY ---")

if character_frequency:

    for character, count in character_frequency.most_common():
        print(f"{character} -> {count}")

else:

    print("No characters found.")


# ============================================================
# WORD FREQUENCY
# ============================================================

print("\n--- WORD FREQUENCY ---")

if word_frequency:

    for word, count in word_frequency.most_common():
        print(f"{word} -> {count}")

else:

    print("No words found.")


# ============================================================
# COMPLETION MESSAGE
# ============================================================

print("\n")
print("=" * 55)
print("       ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 55)
print("Day 19 — Python Advanced 🚀")