# ============================================================
# DAY 19 — PART 5
# 30 PRACTICE CODE SOLUTIONS
# REGEX + COLLECTIONS
# ============================================================


# ============================================================
# Q1. EXTRACT ALL NUMBERS FROM A STRING
# ============================================================

import re

text = "I have 10 apples, 20 bananas and 30 oranges."

numbers = re.findall(r"\d+", text)

print(numbers)


# ============================================================
# Q2. EXTRACT WORDS BEGINNING WITH A CAPITAL LETTER
# ============================================================

import re

text = "Python is Developed by Guido Rossum."

words = re.findall(r"\b[A-Z][a-zA-Z]*\b", text)

print(words)


# ============================================================
# Q3. EXTRACT ALL EMAIL ADDRESSES
# ============================================================

import re

text = """
Contact us at hello@gmail.com
or support@example.com.
"""

emails = re.findall(
    r"[\w.-]+@[\w.-]+\.\w+",
    text
)

print(emails)


# ============================================================
# Q4. EXTRACT INDIAN 10-DIGIT MOBILE NUMBERS
# ============================================================

import re

text = "Call 9876543210 or 8123456789."

numbers = re.findall(
    r"\b[6-9]\d{9}\b",
    text
)

print(numbers)


# ============================================================
# Q5. EXTRACT HASHTAGS
# ============================================================

import re

text = "Learning #Python #AI #MachineLearning today."

hashtags = re.findall(
    r"#\w+",
    text
)

print(hashtags)


# ============================================================
# Q6. EXTRACT @MENTIONS
# ============================================================

import re

text = "Hello @amir, ask @rahul and @developer."

mentions = re.findall(
    r"@\w+",
    text
)

print(mentions)


# ============================================================
# Q7. EXTRACT URLs
# ============================================================

import re

text = "Visit https://github.com and http://example.com"

urls = re.findall(
    r"https?://[^\s]+",
    text
)

print(urls)


# ============================================================
# Q8. REPLACE EVERY DIGIT WITH #
# ============================================================

import re

text = "My OTP is 123456"

result = re.sub(
    r"\d",
    "#",
    text
)

print(result)


# ============================================================
# Q9. REMOVE SPECIAL CHARACTERS
# ============================================================

import re

text = "Python@2026! Advanced#$"

result = re.sub(
    r"[^A-Za-z0-9 ]",
    "",
    text
)

print(result)


# ============================================================
# Q10. CHECK WHETHER STRING CONTAINS ONLY DIGITS
# ============================================================

import re

text = "123456"

if re.fullmatch(r"\d+", text):
    print("Valid")
else:
    print("Invalid")


# ============================================================
# Q11. CHECK WHETHER STRING CONTAINS ONLY ALPHABETS
# ============================================================

import re

text = "Python"

if re.fullmatch(r"[A-Za-z]+", text):
    print("Valid")
else:
    print("Invalid")


# ============================================================
# Q12. USERNAME VALIDATION
# ============================================================

import re

username = "amir_123"

pattern = r"^[A-Za-z0-9_]{3,15}$"

if re.fullmatch(pattern, username):
    print("Valid Username")
else:
    print("Invalid Username")


# ============================================================
# Q13. EXTRACT DATES IN DD-MM-YYYY FORMAT
# ============================================================

import re

text = "Important dates: 15-08-2026 and 26-01-2027."

dates = re.findall(
    r"\b\d{2}-\d{2}-\d{4}\b",
    text
)

print(dates)


# ============================================================
# Q14. FIND ALL WORDS CONTAINING THE LETTER 'A'
# ============================================================

import re

text = "Python Java C++ Data Science"

words = re.findall(
    r"\b[A-Za-z]*a[A-Za-z]*\b",
    text,
    re.IGNORECASE
)

print(words)


# ============================================================
# Q15. COUNT COMPLETE WORD "PYTHON"
# ============================================================

import re

text = """
Python is easy.
Python is powerful.
Pythonic programming is different.
"""

matches = re.findall(
    r"\bPython\b",
    text,
    re.IGNORECASE
)

print("Python count:", len(matches))


# ============================================================
# Q16. COUNT CHARACTER FREQUENCY
# ============================================================

from collections import Counter

text = "programming"

frequency = Counter(text)

print(frequency)


# ============================================================
# Q17. FIND THREE MOST COMMON CHARACTERS
# ============================================================

from collections import Counter

text = "bananaappleorange"

frequency = Counter(text)

top_three = frequency.most_common(3)

print(top_three)


# ============================================================
# Q18. COUNT WORD FREQUENCY
# ============================================================

from collections import Counter

text = "python java python c++ java python"

words = text.split()

frequency = Counter(words)

print(frequency)


# ============================================================
# Q19. FIND DUPLICATE ELEMENTS USING COUNTER
# ============================================================

from collections import Counter

numbers = [
    1, 2, 3, 2, 4, 5, 1, 3, 3
]

frequency = Counter(numbers)

duplicates = [
    number
    for number, count in frequency.items()
    if count > 1
]

print("Duplicates:", duplicates)


# ============================================================
# Q20. FIND MOST FREQUENT NUMBER
# ============================================================

from collections import Counter

numbers = [
    10, 20, 10, 30, 20, 10, 40
]

frequency = Counter(numbers)

most_frequent = frequency.most_common(1)

print("Most frequent:", most_frequent[0][0])


# ============================================================
# Q21. GROUP STUDENTS BY COURSE
# USING defaultdict(list)
# ============================================================

from collections import defaultdict

students = [
    ("Amir", "CSE"),
    ("Rahul", "ECE"),
    ("Aman", "CSE"),
    ("Ravi", "ME"),
    ("Ankit", "ECE")
]

groups = defaultdict(list)

for name, course in students:
    groups[course].append(name)

print(dict(groups))


# ============================================================
# Q22. COUNT WORD FREQUENCY
# USING defaultdict(int)
# ============================================================

from collections import defaultdict

words = [
    "python",
    "java",
    "python",
    "sql",
    "java",
    "python"
]

count = defaultdict(int)

for word in words:
    count[word] += 1

print(dict(count))


# ============================================================
# Q23. GROUP UNIQUE SKILLS BY PERSON
# USING defaultdict(set)
# ============================================================

from collections import defaultdict

skills = [
    ("Amir", "Python"),
    ("Amir", "SQL"),
    ("Amir", "Python"),
    ("Rahul", "Java"),
    ("Rahul", "SQL")
]

groups = defaultdict(set)

for person, skill in skills:
    groups[person].add(skill)

print(dict(groups))


# ============================================================
# Q24. IMPLEMENT QUEUE USING DEQUE
# ============================================================

from collections import deque

queue = deque()

queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")

while queue:

    task = queue.popleft()

    print("Processing:", task)


# ============================================================
# Q25. ADD ELEMENTS FROM BOTH ENDS OF DEQUE
# ============================================================

from collections import deque

queue = deque([
    "B",
    "C"
])

queue.appendleft("A")
queue.append("D")

print(queue)


# ============================================================
# Q26. WORD FREQUENCY ANALYZER
# REGEX + COUNTER
# ============================================================

import re

from collections import Counter


text = """
Python is powerful.
Python is easy.
Python is popular.
Java is powerful.
"""


# Convert text to lowercase

text = text.lower()


# Extract words

words = re.findall(
    r"\b\w+\b",
    text
)


# Count words

frequency = Counter(words)


# Display top 5 words

print(
    "Top 5 Words:"
)

for word, count in frequency.most_common(5):

    print(
        word,
        "->",
        count
    )


# ============================================================
# Q27. EMAIL EXTRACTOR
# ============================================================

import re

text = """
Contact:
amir@gmail.com
hello@example.com
test123@company.org
"""


emails = re.findall(
    r"[\w.-]+@[\w.-]+\.\w+",
    text
)


print("Emails:")

for email in emails:

    print(email)


print(
    "Total Emails:",
    len(emails)
)


# ============================================================
# Q28. LOG ANALYZER
# ============================================================

import re

from collections import Counter


logs = """
ERROR: Database connection failed
INFO: User logged in
ERROR: File not found
WARNING: Low memory
ERROR: Timeout occurred
"""


log_types = re.findall(
    r"\b(ERROR|INFO|WARNING)\b",
    logs
)


frequency = Counter(log_types)


print("Log Frequency:")

for log_type, count in frequency.items():

    print(
        log_type,
        "->",
        count
    )


# ============================================================
# Q29. TEXT DATA CLEANER
# ============================================================

import re

from collections import Counter


text = """
Hello!!! This is Python @2026.
Visit: https://github.com
Email: amir@gmail.com
"""


# ------------------------------------------------------------
# Extract Email
# ------------------------------------------------------------

emails = re.findall(
    r"[\w.-]+@[\w.-]+\.\w+",
    text
)


# ------------------------------------------------------------
# Extract URL
# ------------------------------------------------------------

urls = re.findall(
    r"https?://[^\s]+",
    text
)


# ------------------------------------------------------------
# Extract Numbers
# ------------------------------------------------------------

numbers = re.findall(
    r"\d+",
    text
)


# ------------------------------------------------------------
# Extract Words
# ------------------------------------------------------------

words = re.findall(
    r"\b[A-Za-z]+\b",
    text
)


# ------------------------------------------------------------
# Word Frequency
# ------------------------------------------------------------

frequency = Counter(
    word.lower()
    for word in words
)


# ------------------------------------------------------------
# Display Results
# ------------------------------------------------------------

print("Emails:", emails)

print("URLs:", urls)

print("Numbers:", numbers)

print("Words:", words)

print("Word Frequency:", frequency)


# ============================================================
# Q30. SMART TEXT ANALYZER
# COMPLETE MINI CHALLENGE
# ============================================================

import re

from collections import Counter


# ------------------------------------------------------------
# Take paragraph from user
# ------------------------------------------------------------

text = input(
    "Enter your paragraph:\n"
)


# ------------------------------------------------------------
# Convert to lowercase for word analysis
# ------------------------------------------------------------

lower_text = text.lower()


# ------------------------------------------------------------
# Extract words
# ------------------------------------------------------------

words = re.findall(
    r"\b\w+\b",
    lower_text
)


# ------------------------------------------------------------
# Total words
# ------------------------------------------------------------

total_words = len(words)


# ------------------------------------------------------------
# Unique words
# ------------------------------------------------------------

unique_words = len(
    set(words)
)


# ------------------------------------------------------------
# Word frequency
# ------------------------------------------------------------

word_frequency = Counter(words)


# ------------------------------------------------------------
# Top 5 words
# ------------------------------------------------------------

top_words = word_frequency.most_common(5)


# ------------------------------------------------------------
# Extract numbers
# ------------------------------------------------------------

numbers = re.findall(
    r"\d+",
    text
)


# ------------------------------------------------------------
# Extract emails
# ------------------------------------------------------------

emails = re.findall(
    r"[\w.-]+@[\w.-]+\.\w+",
    text
)


# ------------------------------------------------------------
# Extract URLs
# ------------------------------------------------------------

urls = re.findall(
    r"https?://[^\s]+",
    text
)


# ------------------------------------------------------------
# Extract hashtags
# ------------------------------------------------------------

hashtags = re.findall(
    r"#\w+",
    text
)


# ------------------------------------------------------------
# Extract mentions
# ------------------------------------------------------------

mentions = re.findall(
    r"@\w+",
    text
)


# ------------------------------------------------------------
# Character frequency
# ------------------------------------------------------------

characters = Counter(
    char.lower()
    for char in text
    if not char.isspace()
)


# ------------------------------------------------------------
# DISPLAY RESULTS
# ------------------------------------------------------------

print("\n==============================")
print("SMART TEXT ANALYZER")
print("==============================")

print(
    "\nTotal Words:",
    total_words
)

print(
    "Unique Words:",
    unique_words
)

print(
    "\nTop 5 Words:"
)

for word, count in top_words:

    print(
        word,
        "->",
        count
    )


print(
    "\nNumbers:",
    numbers
)


print(
    "\nEmails:",
    emails
)


print(
    "\nURLs:",
    urls
)


print(
    "\nHashtags:",
    hashtags
)


print(
    "\nMentions:",
    mentions
)


print(
    "\nCharacter Frequency:"
)

for char, count in characters.most_common():

    print(
        char,
        "->",
        count
    )


print(
    "\nWord Frequency:"
)

for word, count in word_frequency.most_common():

    print(
        word,
        "->",
        count
    )


# ============================================================
# END OF DAY 19 — PART 5
# ============================================================