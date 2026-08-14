# ============================================================
# DAY 19 — PART 4
# 30 PRACTICE QUESTIONS
# REGEX + COLLECTIONS
# ============================================================

# IMPORTANT:
# Solve these questions yourself first.
# Do NOT look for the code immediately.
# The separate code solutions will be provided in the
# next part.


# ============================================================
# SECTION A — REGULAR EXPRESSIONS
# QUESTIONS 1–15
# ============================================================


# Q1. Extract all numbers from a string.
#
# Input:
# "I have 10 apples, 20 bananas and 30 oranges."
#
# Expected:
# ['10', '20', '30']


# ============================================================

# Q2. Extract all words beginning with a capital letter.
#
# Input:
# "Python is Developed by Guido Rossum."
#
# Expected words should include:
# Python
# Developed
# Guido
# Rossum


# ============================================================

# Q3. Find all email addresses from a paragraph.
#
# Input:
# "Contact us at hello@gmail.com or support@example.com."
#
# Expected:
# ['hello@gmail.com', 'support@example.com']


# ============================================================

# Q4. Extract all Indian-style 10-digit mobile numbers.
#
# Requirement:
# The number should begin with 6, 7, 8, or 9.
#
# Input:
# "Call 9876543210 or 8123456789."
#
# Expected:
# ['9876543210', '8123456789']


# ============================================================

# Q5. Extract all hashtags from a sentence.
#
# Input:
# "Learning #Python #AI #MachineLearning today."
#
# Expected:
# ['#Python', '#AI', '#MachineLearning']


# ============================================================

# Q6. Extract all @mentions from a sentence.
#
# Input:
# "Hello @amir, ask @rahul and @developer."
#
# Expected:
# ['@amir', '@rahul', '@developer']


# ============================================================

# Q7. Find all URLs beginning with http:// or https://.
#
# Input:
# "Visit https://github.com and http://example.com"
#
# Expected:
# ['https://github.com', 'http://example.com']


# ============================================================

# Q8. Replace every digit in a string with '#'.
#
# Input:
# "My OTP is 123456"
#
# Expected:
# "My OTP is ######"


# ============================================================

# Q9. Remove all special characters from a string.
#
# Input:
# "Python@2026! Advanced#$"
#
# Expected:
# "Python2026 Advanced"


# ============================================================

# Q10. Check whether a string contains only digits.
#
# Test:
# "123456"
#
# Expected:
# Valid
#
# Test:
# "123abc"
#
# Expected:
# Invalid


# ============================================================

# Q11. Check whether a string contains only alphabets.
#
# Test:
# "Python"
#
# Expected:
# Valid
#
# Test:
# "Python123"
#
# Expected:
# Invalid


# ============================================================

# Q12. Check whether a username is valid.
#
# Requirements:
# - 3 to 15 characters
# - Only letters, numbers and underscore
# - No spaces
#
# Examples:
#
# "amir_123"  -> Valid
# "am"        -> Invalid
# "amir khan" -> Invalid


# ============================================================

# Q13. Extract dates in DD-MM-YYYY format.
#
# Input:
# "Important dates: 15-08-2026 and 26-01-2027."
#
# Expected:
# ['15-08-2026', '26-01-2027']


# ============================================================

# Q14. Find all words containing the letter 'a'.
#
# Input:
# "Python Java C++ Data Science"
#
# Expected:
# Words containing 'a' should be extracted.


# ============================================================

# Q15. Count how many times the word "Python" appears
# as a complete word.
#
# Input:
# "Python is easy. Python is powerful.
#  Pythonic programming is different."
#
# Expected:
# 2
#
# Important:
# "Pythonic" should NOT be counted.


# ============================================================
# SECTION B — COLLECTIONS
# QUESTIONS 16–25
# ============================================================


# Q16. Use Counter to count the frequency of each character.
#
# Input:
# "programming"
#
# Expected:
# Character frequencies.


# ============================================================

# Q17. Find the three most common characters in a string.
#
# Input:
# "bananaappleorange"
#
# Use:
# Counter.most_common()


# ============================================================

# Q18. Count the frequency of each word in a sentence.
#
# Input:
# "python java python c++ java python"
#
# Expected:
#
# python -> 3
# java   -> 2
# c++    -> 1


# ============================================================

# Q19. Find duplicate elements in a list using Counter.
#
# Input:
# [1, 2, 3, 2, 4, 5, 1, 3, 3]
#
# Expected:
# Duplicate elements should be identified.


# ============================================================

# Q20. Find the most frequent number in a list.
#
# Input:
# [10, 20, 10, 30, 20, 10, 40]
#
# Expected:
# 10


# ============================================================

# Q21. Use defaultdict(list) to group students by course.
#
# Input:
#
# [
#     ("Amir", "CSE"),
#     ("Rahul", "ECE"),
#     ("Aman", "CSE"),
#     ("Ravi", "ME"),
#     ("Ankit", "ECE")
# ]
#
# Expected:
#
# CSE -> Amir, Aman
# ECE -> Rahul, Ankit
# ME  -> Ravi


# ============================================================

# Q22. Use defaultdict(int) to count word frequency.
#
# Input:
#
# ["python", "java", "python", "sql", "java", "python"]
#
# Expected:
#
# python -> 3
# java   -> 2
# sql    -> 1


# ============================================================

# Q23. Use defaultdict(set) to group unique skills by person.
#
# Input:
#
# [
#     ("Amir", "Python"),
#     ("Amir", "SQL"),
#     ("Amir", "Python"),
#     ("Rahul", "Java"),
#     ("Rahul", "SQL")
# ]
#
# Expected:
#
# Amir  -> {'Python', 'SQL'}
# Rahul -> {'Java', 'SQL'}


# ============================================================

# Q24. Implement a queue using deque.
#
# Tasks:
#
# 1. Add:
#    Task 1
#    Task 2
#    Task 3
#
# 2. Remove tasks from the left.
#
# Expected order:
#
# Task 1
# Task 2
# Task 3


# ============================================================

# Q25. Implement a deque where elements can be added
# from both ends.
#
# Start:
#
# ["B", "C"]
#
# Add "A" to the left.
#
# Add "D" to the right.
#
# Expected:
#
# ["A", "B", "C", "D"]


# ============================================================
# SECTION C — COMBINED ADVANCED PRACTICE
# QUESTIONS 26–30
# ============================================================


# Q26. Build a Word Frequency Analyzer.
#
# Input:
#
# text = """
# Python is powerful.
# Python is easy.
# Python is popular.
# Java is powerful.
# """
#
# Requirements:
#
# 1. Convert text to lowercase.
# 2. Extract words using Regex.
# 3. Count words using Counter.
# 4. Display the top 5 words.


# ============================================================

# Q27. Build an Email Extractor.
#
# Input:
#
# text = """
# Contact:
# amir@gmail.com
# hello@example.com
# test123@company.org
# """
#
# Requirements:
#
# 1. Use Regex.
# 2. Extract all email addresses.
# 3. Store them in a list.
# 4. Print the total number of emails.


# ============================================================

# Q28. Build a Log Analyzer.
#
# Input:
#
# logs = """
# ERROR: Database connection failed
# INFO: User logged in
# ERROR: File not found
# WARNING: Low memory
# ERROR: Timeout occurred
# """
#
# Requirements:
#
# 1. Extract ERROR, INFO and WARNING.
# 2. Count each type using Counter.
# 3. Display the frequency.
#
# Expected:
#
# ERROR   -> 3
# INFO    -> 1
# WARNING -> 1


# ============================================================

# Q29. Build a Text Data Cleaner.
#
# Input:
#
# text = """
# Hello!!! This is Python @2026.
# Visit: https://github.com
# Email: amir@gmail.com
# """
#
# Requirements:
#
# 1. Extract email.
# 2. Extract URL.
# 3. Extract numbers.
# 4. Extract words.
# 5. Count word frequency.
#
# Use:
#
# Regex
# Counter


# ============================================================

# Q30. MINI CHALLENGE — SMART TEXT ANALYZER
#
# Create a program that accepts a paragraph from the user
# and performs the following operations:
#
# 1. Count total words.
# 2. Count unique words.
# 3. Find the most common 5 words.
# 4. Extract all numbers.
# 5. Extract all email addresses.
# 6. Extract all URLs.
# 7. Extract all hashtags.
# 8. Extract all @mentions.
# 9. Display character frequency.
# 10. Display word frequency.
#
# Required modules:
#
# import re
# from collections import Counter
#
#
# Example Input:
#
# """
# Python is amazing.
# I am learning Python in 2026.
# Contact: amir@gmail.com
# Visit https://github.com
# #Python #Coding
# Follow @developer
# """
#
#
# Expected output should contain:
#
# Total Words
# Unique Words
# Top 5 Words
# Numbers
# Emails
# URLs
# Hashtags
# Mentions
# Character Frequency
# Word Frequency


# ============================================================
# DAY 19 PRACTICE CHECKLIST
# ============================================================

REGEX PRACTICE:

[ ] Numbers
[ ] Capitalized words
[ ] Emails
[ ] Phone numbers
[ ] Hashtags
[ ] Mentions
[ ] URLs
[ ] Text replacement
[ ] Special character removal
[ ] Digit validation
[ ] Alphabet validation
[ ] Username validation
[ ] Date extraction
[ ] Word filtering
[ ] Word counting


COLLECTIONS PRACTICE:

[ ] Counter
[ ] most_common()
[ ] defaultdict(list)
[ ] defaultdict(int)
[ ] defaultdict(set)
[ ] deque
[ ] appendleft()
[ ] popleft()


ADVANCED PRACTICE:

[ ] Word Frequency Analyzer
[ ] Email Extractor
[ ] Log Analyzer
[ ] Text Data Cleaner
[ ] Smart Text Analyzer


# ============================================================
# DAY 19 TARGET
# ============================================================

Complete all 30 questions.

Recommended order:

Q1–Q15
    ↓
Regex Practice

Q16–Q25
    ↓
Collections Practice

Q26–Q30
    ↓
Advanced Real-World Practice