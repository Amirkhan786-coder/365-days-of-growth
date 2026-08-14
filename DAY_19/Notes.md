# ============================================================
# DAY 19 — PYTHON ADVANCED
# REGULAR EXPRESSIONS + COLLECTIONS
# ============================================================


# ============================================================
# 1. REGULAR EXPRESSIONS (REGEX)
# ============================================================

Regular Expression, commonly called Regex, is a pattern used
to search, match, extract, replace, or validate text.

Python provides the built-in `re` module for Regular Expressions.

Example:

import re

text = "My email is amir@gmail.com"

result = re.findall(r"\w+@\w+\.\w+", text)

print(result)

Output:
['amir@gmail.com']


# ============================================================
# 2. WHY USE REGEX?
# ============================================================

Regex is useful for:

- Email extraction
- Phone number extraction
- URL extraction
- Hashtag extraction
- Username validation
- Password validation
- Finding specific words
- Replacing text
- Data cleaning
- Log analysis
- Text processing
- Data validation


# ============================================================
# 3. RAW STRINGS
# ============================================================

Regex patterns commonly use backslashes.

Python raw strings make Regex patterns easier to write.

Example:

pattern = r"\d+"

The `r` before the string means it is treated as a raw string.

Example:

import re

text = "My numbers are 123 and 456"

result = re.findall(r"\d+", text)

print(result)

Output:
['123', '456']


# ============================================================
# 4. BASIC REGEX SYMBOLS
# ============================================================

Symbol     Meaning

.          Any character except newline
^          Start of string/line
$          End of string/line
*          Zero or more occurrences
+          One or more occurrences
?          Zero or one occurrence
{n}        Exactly n occurrences
{n,m}      Between n and m occurrences
[]         Character set
()         Group
|          OR


# ============================================================
# 5. CHARACTER CLASSES
# ============================================================

## \d

Matches digits.

Example:

import re

text = "Python 123 Java 456"

result = re.findall(r"\d+", text)

print(result)

Output:
['123', '456']


## \D

Matches non-digit characters.

Example:

re.findall(r"\D+", "123ABC")

Output:

['ABC']


## \w

Matches word characters.

Generally includes:

- A-Z
- a-z
- 0-9
- _


Example:

re.findall(r"\w+", "Python_123")

Output:

['Python_123']


## \W

Matches non-word characters.


## \s

Matches whitespace characters.

Examples:

- Space
- Tab
- Newline


## \S

Matches non-whitespace characters.


# ============================================================
# 6. re.search()
# ============================================================

`re.search()` searches for the first occurrence of a pattern
anywhere in the string.

Example:

import re

text = "Python is powerful"

result = re.search("Python", text)

if result:
    print("Found")
else:
    print("Not Found")

Output:

Found


Important:

search() searches the complete string until it finds a match.


# ============================================================
# 7. re.match()
# ============================================================

`re.match()` checks for a match only at the beginning
of the string.

Example:

import re

text = "Python is powerful"

result = re.match("Python", text)

if result:
    print("Matched")
else:
    print("Not Matched")

Output:

Matched


Example:

text = "I love Python"

result = re.match("Python", text)

print(result)

Output:

None

Because Python is not at the beginning.


# ============================================================
# 8. re.fullmatch()
# ============================================================

`re.fullmatch()` checks whether the entire string matches
the given pattern.

Example:

import re

result = re.fullmatch(r"\d+", "12345")

print(result)

Output:

Match object


Example:

result = re.fullmatch(r"\d+", "123abc")

print(result)

Output:

None


Difference:

match()
    Checks from the beginning.

search()
    Searches anywhere.

fullmatch()
    Entire string must match.


# ============================================================
# 9. re.findall()
# ============================================================

`re.findall()` returns all matching values as a list.

Example:

import re

text = "Python 123 Java 456 C++ 789"

numbers = re.findall(r"\d+", text)

print(numbers)

Output:

['123', '456', '789']


Example:

text = "Python Java Python C++"

words = re.findall(r"\w+", text)

print(words)

Output:

['Python', 'Java', 'Python', 'C++']


# ============================================================
# 10. re.finditer()
# ============================================================

`re.finditer()` returns an iterator containing match objects.

Example:

import re

text = "Python 123 Java 456"

matches = re.finditer(r"\d+", text)

for match in matches:
    print(match.group())

Output:

123
456


Difference:

findall()
    Returns matched values.

finditer()
    Returns match objects.


# ============================================================
# 11. re.sub()
# ============================================================

`re.sub()` is used to replace matching text.

Syntax:

re.sub(pattern, replacement, string)


Example:

import re

text = "Python is difficult"

new_text = re.sub(
    "difficult",
    "powerful",
    text
)

print(new_text)

Output:

Python is powerful


Example:

import re

text = "My phone number is 9876543210"

result = re.sub(
    r"\d",
    "#",
    text
)

print(result)

Output:

My phone number is ##########


# ============================================================
# 12. re.split()
# ============================================================

`re.split()` splits a string using a Regex pattern.

Example:

import re

text = "Python,Java;C++;SQL"

result = re.split(
    r"[,;]",
    text
)

print(result)

Output:

['Python', 'Java', 'C++', 'SQL']


# ============================================================
# 13. QUANTIFIERS
# ============================================================

Quantifiers define how many times a pattern should occur.


## *

Zero or more occurrences.

Pattern:

r"ab*"

Matches:

a
ab
abb
abbb


## +

One or more occurrences.

Pattern:

r"ab+"

Matches:

ab
abb
abbb

Does NOT match:

a


## ?

Zero or one occurrence.

Pattern:

r"colou?r"

Matches:

color
colour


## {n}

Exactly n occurrences.

Example:

r"\d{4}"

Matches:

2026
1234


## {n,m}

Between n and m occurrences.

Example:

r"\d{2,4}"

Can match:

12
123
1234


# ============================================================
# 14. CHARACTER SETS
# ============================================================

Square brackets define a character set.

Example:

[abc]

Matches one character from:

a
b
c


Example:

import re

text = "apple banana cat"

result = re.findall(
    r"[abc]",
    text
)

print(result)


# ============================================================
# 15. CHARACTER RANGES
# ============================================================

## Lowercase letters

[a-z]


## Uppercase letters

[A-Z]


## Digits

[0-9]


## Both uppercase and lowercase

[A-Za-z]


Example:

import re

text = "Python ABC 123"

result = re.findall(
    r"[A-Z]",
    text
)

print(result)

Output:

['P', 'A', 'B', 'C']


# ============================================================
# 16. NEGATED CHARACTER SET
# ============================================================

The `^` inside square brackets means NOT.

Example:

[^0-9]

Means:

Match anything except digits.

Example:

import re

text = "Python123"

result = re.findall(
    r"[^0-9]+",
    text
)

print(result)

Output:

['Python']


Important:

^ outside []  -> Start of string/line

^ inside []   -> NOT


# ============================================================
# 17. REGEX GROUPS
# ============================================================

Parentheses `()` create groups.

Example:

pattern = r"(\d{3})-(\d{3})-(\d{4})"

Text:

123-456-7890


Example:

import re

text = "123-456-7890"

match = re.search(
    r"(\d{3})-(\d{3})-(\d{4})",
    text
)

if match:

    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

Output:

123
456
7890


# ============================================================
# 18. EMAIL EXTRACTION
# ============================================================

A basic email pattern:

r"[\w.-]+@[\w.-]+\.\w+"


Example:

import re

text = """
Contact amir@gmail.com
or test@example.com
"""

emails = re.findall(
    r"[\w.-]+@[\w.-]+\.\w+",
    text
)

print(emails)

Output:

['amir@gmail.com', 'test@example.com']


Note:

This is a practical basic pattern, not a complete RFC-level
email validator.


# ============================================================
# 19. PHONE NUMBER EXTRACTION
# ============================================================

For a basic 10-digit Indian mobile number:

r"\b[6-9]\d{9}\b"


Example:

import re

text = "Call me at 9876543210"

numbers = re.findall(
    r"\b[6-9]\d{9}\b",
    text
)

print(numbers)

Output:

['9876543210']


# ============================================================
# 20. URL EXTRACTION
# ============================================================

A basic URL pattern:

r"https?://[^\s]+"


Example:

import re

text = """
Visit https://github.com
or https://example.com
"""

urls = re.findall(
    r"https?://[^\s]+",
    text
)

print(urls)

Output:

['https://github.com', 'https://example.com']


# ============================================================
# 21. HASHTAG EXTRACTION
# ============================================================

Pattern:

r"#\w+"


Example:

import re

text = """
Learning #Python #Coding #Programming
"""

hashtags = re.findall(
    r"#\w+",
    text
)

print(hashtags)

Output:

['#Python', '#Coding', '#Programming']


# ============================================================
# 22. MENTION EXTRACTION
# ============================================================

Pattern:

r"@\w+"


Example:

import re

text = """
Hello @amir @developer @python
"""

mentions = re.findall(
    r"@\w+",
    text
)

print(mentions)

Output:

['@amir', '@developer', '@python']


# ============================================================
# 23. WORD BOUNDARY
# ============================================================

`\b` represents a word boundary.

Example:

r"\bPython\b"

This matches Python as a complete word.

Example:

import re

text = "Python Pythonic Python"

result = re.findall(
    r"\bPython\b",
    text
)

print(result)

Output:

['Python', 'Python']


It does not match:

Pythonic


# ============================================================
# 24. CASE-INSENSITIVE MATCHING
# ============================================================

Regex normally considers uppercase and lowercase letters
different.

Example:

import re

text = "Python PYTHON python"

result = re.findall(
    r"python",
    text,
    re.IGNORECASE
)

print(result)

Output:

['Python', 'PYTHON', 'python']


`re.IGNORECASE` allows case-insensitive matching.


# ============================================================
# 25. re.compile()
# ============================================================

`re.compile()` creates a reusable Regex pattern.

It is useful when the same pattern is used multiple times.

Example:

import re

pattern = re.compile(
    r"\d+"
)

text = "123 456 789"

numbers = pattern.findall(text)

print(numbers)

Output:

['123', '456', '789']


Advantages:

- Reusable pattern
- Cleaner code
- Useful for repeated matching


# ============================================================
# 26. COLLECTIONS MODULE
# ============================================================

Python provides a `collections` module containing specialized
container data structures.

Import example:

from collections import Counter

Important classes:

- Counter
- defaultdict
- deque
- namedtuple
- OrderedDict
- ChainMap


# ============================================================
# 27. COUNTER
# ============================================================

`Counter` is a dictionary-like class used to count
hashable objects.

Example:

from collections import Counter

numbers = [
    1,
    2,
    2,
    3,
    3,
    3
]

counter = Counter(numbers)

print(counter)

Output:

Counter({
    3: 3,
    2: 2,
    1: 1
})


# ============================================================
# 28. COUNTER WITH STRING
# ============================================================

Counter can count characters.

Example:

from collections import Counter

text = "banana"

counter = Counter(text)

print(counter)

Output:

Counter({
    'a': 3,
    'n': 2,
    'b': 1
})


# ============================================================
# 29. most_common()
# ============================================================

`most_common()` returns the most frequent elements.

Example:

from collections import Counter

text = "banana"

counter = Counter(text)

print(counter.most_common(2))

Output:

[
    ('a', 3),
    ('n', 2)
]


# ============================================================
# 30. COUNTER WITH WORDS
# ============================================================

Example:

from collections import Counter

text = """
python java python
python c++ java
"""

words = text.split()

counter = Counter(words)

print(counter)

Output will contain word frequencies.


# ============================================================
# 31. COUNTER ARITHMETIC
# ============================================================

Counter objects support operations such as:

+
-
&
|


Example:

from collections import Counter

a = Counter({
    "python": 3,
    "java": 2
})

b = Counter({
    "python": 1,
    "java": 4
})

result = a + b

print(result)


# ============================================================
# 32. DEFAULTDICT
# ============================================================

`defaultdict` is a dictionary subclass that automatically
provides a default value for missing keys.

Example:

from collections import defaultdict

data = defaultdict(list)

data["Python"].append("Regex")
data["Python"].append("Collections")

print(data)

Output:

defaultdict(
    <class 'list'>,
    {
        'Python': [
            'Regex',
            'Collections'
        ]
    }
)


# ============================================================
# 33. defaultdict(list)
# ============================================================

Very useful for grouping data.

Example:

from collections import defaultdict

students = [
    ("Amir", "CSE"),
    ("Rahul", "ECE"),
    ("Aman", "CSE"),
    ("Ravi", "ME")
]

groups = defaultdict(list)

for name, course in students:

    groups[course].append(name)

print(dict(groups))

Output:

{
    'CSE': ['Amir', 'Aman'],
    'ECE': ['Rahul'],
    'ME': ['Ravi']
}


# ============================================================
# 34. defaultdict(int)
# ============================================================

Useful for counting.

Example:

from collections import defaultdict

words = [
    "python",
    "java",
    "python"
]

count = defaultdict(int)

for word in words:

    count[word] += 1

print(dict(count))

Output:

{
    'python': 2,
    'java': 1
}


# ============================================================
# 35. defaultdict(set)
# ============================================================

Useful for grouping unique values.

Example:

from collections import defaultdict

groups = defaultdict(set)

groups["CSE"].add("Python")
groups["CSE"].add("SQL")
groups["CSE"].add("Python")

print(dict(groups))

Output:

{
    'CSE': {
        'Python',
        'SQL'
    }
}


# ============================================================
# 36. DEQUE
# ============================================================

`deque` means:

Double-Ended Queue.

It supports efficient insertion and removal from both ends.

Example:

from collections import deque

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")

print(queue)

Output:

deque(['A', 'B', 'C'])


# ============================================================
# 37. appendleft()
# ============================================================

`appendleft()` adds an element to the left side.

Example:

from collections import deque

queue = deque([
    "B",
    "C"
])

queue.appendleft("A")

print(queue)

Output:

deque(['A', 'B', 'C'])


# ============================================================
# 38. popleft()
# ============================================================

`popleft()` removes and returns the leftmost element.

Example:

from collections import deque

queue = deque([
    "A",
    "B",
    "C"
])

item = queue.popleft()

print(item)
print(queue)

Output:

A
deque(['B', 'C'])


# ============================================================
# 39. pop()
# ============================================================

`pop()` removes the rightmost element.

Example:

from collections import deque

queue = deque([
    "A",
    "B",
    "C"
])

item = queue.pop()

print(item)
print(queue)

Output:

C
deque(['A', 'B'])


# ============================================================
# 40. DEQUE AS A QUEUE
# ============================================================

A deque can be used to implement a queue.

Example:

from collections import deque

queue = deque([
    "Task 1",
    "Task 2",
    "Task 3"
])

while queue:

    task = queue.popleft()

    print(
        "Processing:",
        task
    )

Output:

Processing: Task 1
Processing: Task 2
Processing: Task 3


# ============================================================
# 41. LIST VS DEQUE
# ============================================================

List:

- Good for random access
- Good for indexing
- append() is efficient
- Removing from the beginning can be expensive

Deque:

- Efficient operations at both ends
- append()
- appendleft()
- pop()
- popleft()

Use deque when you frequently add/remove elements
from both ends.


# ============================================================
# 42. NAMEDTUPLE
# ============================================================

`namedtuple` creates tuple-like objects with named fields.

Example:

from collections import namedtuple

Student = namedtuple(
    "Student",
    [
        "name",
        "age"
    ]
)

student = Student(
    "Amir",
    20
)

print(student.name)
print(student.age)

Output:

Amir
20


# ============================================================
# 43. NAMEDTUPLE VS TUPLE
# ============================================================

Normal tuple:

student = (
    "Amir",
    20
)

Access:

student[0]
student[1]


namedtuple:

student.name
student.age


Advantages:

- More readable
- Lightweight
- Immutable like tuples
- Named fields


# ============================================================
# 44. CHAINMAP
# ============================================================

`ChainMap` combines multiple mappings into a single view.

Example:

from collections import ChainMap

defaults = {
    "theme": "light",
    "language": "English"
}

user = {
    "theme": "dark"
}

settings = ChainMap(
    user,
    defaults
)

print(settings["theme"])
print(settings["language"])

Output:

dark
English


# ============================================================
# 45. CHAINMAP SEARCH ORDER
# ============================================================

ChainMap searches mappings from left to right.

Example:

from collections import ChainMap

first = {
    "name": "Amir"
}

second = {
    "name": "Rahul",
    "age": 20
}

data = ChainMap(
    first,
    second
)

print(data["name"])

Output:

Amir

Because the first mapping has the key.


# ============================================================
# 46. ORDEREDDICT
# ============================================================

`OrderedDict` is available in the collections module.

Modern Python dictionaries preserve insertion order, so a
normal `dict` is usually enough for maintaining insertion order.

However, OrderedDict still provides useful order-specific
operations.

Example:

from collections import OrderedDict

data = OrderedDict()

data["a"] = 1
data["b"] = 2

print(data)


# ============================================================
# 47. REGEX + COLLECTIONS
# ============================================================

Regex and Collections can be combined to solve
real-world text-processing problems.

Example:

import re

from collections import Counter


text = """
Python is powerful.
Python is easy.
Python is popular.
"""


words = re.findall(
    r"\b\w+\b",
    text.lower()
)


frequency = Counter(words)

print(frequency)


This performs:

Text
  ↓
Regex
  ↓
Extract Words
  ↓
Counter
  ↓
Word Frequency


# ============================================================
# 48. TEXT PROCESSING PIPELINE
# ============================================================

A common text-processing pipeline is:

Raw Text
   ↓
Regex
   ↓
Clean / Extract
   ↓
Collections
   ↓
Count / Group
   ↓
Analyze
   ↓
Result


Example:

text = """
Python Python Java Java Python
"""


Step 1:

Extract words using Regex.

Step 2:

Normalize using lower().

Step 3:

Count using Counter.

Example:

import re

from collections import Counter


text = """
Python Python Java Java Python
"""


words = re.findall(
    r"\b\w+\b",
    text.lower()
)


frequency = Counter(words)


print(
    frequency
)


# ============================================================
# 49. REAL-WORLD APPLICATIONS
# ============================================================

Regex + Collections are useful in:

- Text analytics
- Log analysis
- Data cleaning
- Web scraping
- Search systems
- NLP preprocessing
- Email extraction
- Document processing
- Chat applications
- Validation systems
- Cybersecurity tools
- Data pipelines
- Resume analysis
- Content analysis
- Social media text analysis


# ============================================================
# 50. IMPORTANT DAY 19 SUMMARY
# ============================================================

REGEX:

re.search()
re.match()
re.fullmatch()
re.findall()
re.finditer()
re.sub()
re.split()
re.compile()


REGEX SYMBOLS:

.
^
$
*
+
?
{}
[]
()
|


CHARACTER CLASSES:

\d
\D
\w
\W
\s
\S
\b


COLLECTIONS:

Counter
defaultdict
deque
namedtuple
OrderedDict
ChainMap


IMPORTANT COUNTER METHODS:

most_common()


IMPORTANT DEQUE METHODS:

append()
appendleft()
pop()
popleft()


IMPORTANT CONCEPTS:

Pattern Matching
Text Extraction
Validation
Text Cleaning
Frequency Counting
Grouping
Queues
Structured Data
Text Analysis


# ============================================================
# DAY 19 FINAL LEARNING OUTCOME
# ============================================================

By the end of Day 19, you should be able to say:

"I can use Regular Expressions to search, validate, extract,
replace and manipulate text, and I can use Python Collections
for efficient counting, grouping, queuing and structured
data processing."


# ============================================================
# DAY 19 SKILL STACK
# ============================================================

REGEX
   ↓
Pattern Matching
   ↓
Text Extraction
   ↓
Data Cleaning
   ↓
Counter
   ↓
defaultdict
   ↓
deque
   ↓
namedtuple
   ↓
ChainMap
   ↓
Smart Text Analyzer