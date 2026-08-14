# ============================================================
# DAY 19 — 30 INTERVIEW QUESTIONS
# REGULAR EXPRESSIONS + COLLECTIONS
# ============================================================


# ============================================================
# BEGINNER LEVEL — Q1 TO Q10
# ============================================================


# Q1. What is Regular Expression in Python?

Answer:

Regular Expression (Regex) is a pattern used to search,
match, extract, validate, replace, and manipulate text.

Python provides the built-in `re` module for working with
Regular Expressions.

Example:

import re

text = "Python is powerful"

result = re.search(
    r"Python",
    text
)

print(result)


# ============================================================
# Q2. Which module is used for Regular Expressions in Python?

Answer:

Python provides the built-in `re` module.

Example:

import re


# ============================================================
# Q3. What is the difference between re.search() and
# re.match()?

Answer:

re.search():

- Searches for a pattern anywhere in the string.
- Returns the first match it finds.

re.match():

- Checks only from the beginning of the string.

Example:

import re

text = "I love Python"

print(
    re.search(
        r"Python",
        text
    )
)

print(
    re.match(
        r"Python",
        text
    )
)

search() finds Python.

match() returns None because Python is not at the beginning.


# ============================================================
# Q4. What is re.fullmatch()?

Answer:

re.fullmatch() checks whether the entire string matches
the specified pattern.

Example:

import re

result = re.fullmatch(
    r"\d+",
    "12345"
)

print(result)

The complete string must contain only digits for a match.


# ============================================================
# Q5. What does re.findall() do?

Answer:

re.findall() searches for all matches and returns them
as a list.

Example:

import re

text = "Python 123 Java 456"

numbers = re.findall(
    r"\d+",
    text
)

print(numbers)

Output:

['123', '456']


# ============================================================
# Q6. What is the difference between findall() and finditer()?

Answer:

findall():

- Returns matching values.
- Usually returns a list.

finditer():

- Returns an iterator.
- Produces Match objects.

Example:

import re

text = "Python 123 Java 456"

print(
    re.findall(
        r"\d+",
        text
    )
)

for match in re.finditer(
    r"\d+",
    text
):
    print(match.group())


# ============================================================
# Q7. What is re.sub()?

Answer:

re.sub() is used to replace text that matches a Regex pattern.

Syntax:

re.sub(
    pattern,
    replacement,
    string
)

Example:

import re

text = "Python is difficult"

result = re.sub(
    r"difficult",
    "powerful",
    text
)

print(result)

Output:

Python is powerful


# ============================================================
# Q8. What is re.split()?

Answer:

re.split() splits a string using a Regex pattern.

Example:

import re

text = "Python,Java;C++"

result = re.split(
    r"[,;]",
    text
)

print(result)

Output:

['Python', 'Java', 'C++']


# ============================================================
# Q9. What does \d mean in Regex?

Answer:

\d matches a digit.

Example:

import re

text = "Python 123"

result = re.findall(
    r"\d",
    text
)

print(result)

Output:

['1', '2', '3']


# ============================================================
# Q10. What does \w and \s mean?

Answer:

\w matches word characters.

It generally includes:

- Letters
- Digits
- Underscore

\s matches whitespace characters such as:

- Space
- Tab
- Newline

Example:

r"\w+"

r"\s+"


# ============================================================
# INTERMEDIATE LEVEL — Q11 TO Q20
# ============================================================


# Q11. What are Regex quantifiers?

Answer:

Quantifiers specify how many times a pattern should occur.

Common quantifiers are:

*       Zero or more
+       One or more
?       Zero or one
{n}     Exactly n
{n,m}   Between n and m

Example:

r"\d+"

means one or more digits.


# ============================================================
# Q12. What is the difference between * and +?

Answer:

`*` matches zero or more occurrences.

`+` matches one or more occurrences.

Example:

r"ab*"

Can match:

a
ab
abb
abbb

Example:

r"ab+"

Can match:

ab
abb
abbb

But it cannot match only:

a


# ============================================================
# Q13. What are character classes in Regex?

Answer:

Character classes define a set or range of characters
that can be matched.

Examples:

[abc]

Matches:

a
b
c

[a-z]

Matches lowercase letters.

[A-Z]

Matches uppercase letters.

[0-9]

Matches digits.


# ============================================================
# Q14. What is the purpose of ^ and $ in Regex?

Answer:

`^` represents the beginning of a string or line.

`$` represents the end of a string or line.

Example:

r"^Python"

Means the string should start with Python.

Example:

r"Python$"

Means the string should end with Python.


# ============================================================
# Q15. What is a Regex group?

Answer:

Parentheses `()` are used to create groups in Regex.

Groups allow us to capture specific parts of a match.

Example:

import re

text = "123-456-7890"

match = re.search(
    r"(\d{3})-(\d{3})-(\d{4})",
    text
)

print(match.group(1))
print(match.group(2))
print(match.group(3))

Output:

123
456
7890


# ============================================================
# Q16. What is a word boundary in Regex?

Answer:

`\b` represents a word boundary.

It is useful when we want to match a complete word.

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

Pythonic is not matched because Python is not a complete
word there.


# ============================================================
# Q17. Why are raw strings commonly used with Regex?

Answer:

Regex patterns frequently contain backslashes.

Raw strings make these patterns easier to write and read
because Python does not process most backslashes as normal
string escape sequences.

Example:

pattern = r"\d+"

This is clearer than writing patterns with escaped
backslashes manually.


# ============================================================
# Q18. What is re.compile()?

Answer:

re.compile() creates a reusable compiled Regex pattern.

It is useful when the same pattern needs to be used
multiple times.

Example:

import re

pattern = re.compile(
    r"\d+"
)

text = "123 456 789"

print(
    pattern.findall(text)
)


# ============================================================
# Q19. What is re.IGNORECASE?

Answer:

re.IGNORECASE allows Regex matching without considering
uppercase and lowercase differences.

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


# ============================================================
# Q20. How can Regex be used to extract emails?

Answer:

A basic practical email pattern can be used.

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

[
    'amir@gmail.com',
    'test@example.com'
]

Note:

This is a practical basic pattern, not a complete
RFC-level email validator.


# ============================================================
# ADVANCED LEVEL — Q21 TO Q30
# ============================================================


# Q21. What is the collections module in Python?

Answer:

The collections module provides specialized container
data types that extend the functionality of Python's
built-in containers.

Important classes include:

Counter
defaultdict
deque
namedtuple
OrderedDict
ChainMap


# ============================================================
# Q22. What is Counter?

Answer:

Counter is a dictionary-like class used to count
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
# Q23. What does Counter.most_common() do?

Answer:

most_common() returns the elements with the highest
frequency.

Example:

from collections import Counter

text = "banana"

counter = Counter(text)

print(
    counter.most_common(2)
)

Output:

[
    ('a', 3),
    ('n', 2)
]


# ============================================================
# Q24. What is defaultdict?

Answer:

defaultdict is a dictionary subclass that automatically
creates a default value when a missing key is accessed.

Example:

from collections import defaultdict

data = defaultdict(list)

data["CSE"].append("Python")
data["CSE"].append("SQL")

print(dict(data))

Output:

{
    'CSE': [
        'Python',
        'SQL'
    ]
}


# ============================================================
# Q25. Why is defaultdict(int) useful?

Answer:

defaultdict(int) is useful for counting because a missing
key automatically starts with the value 0.

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
# Q26. What is deque?

Answer:

deque stands for Double-Ended Queue.

It allows efficient insertion and removal of elements
from both the left and right ends.

Example:

from collections import deque

queue = deque()

queue.append("A")
queue.append("B")

queue.appendleft("Start")

print(queue)


# ============================================================
# Q27. What is the difference between a list and a deque?

Answer:

List:

- Good for random access and indexing.
- append() at the end is efficient.
- Removing from the beginning can be expensive.

Deque:

- Designed for operations at both ends.
- append() adds to the right.
- appendleft() adds to the left.
- pop() removes from the right.
- popleft() removes from the left.

Therefore, deque is usually preferred for queue-like
operations.


# ============================================================
# Q28. What is namedtuple?

Answer:

namedtuple creates tuple-like objects whose values can
be accessed using meaningful field names.

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

Advantages:

- Readable
- Lightweight
- Immutable like tuples
- Fields can be accessed by name


# ============================================================
# Q29. What is ChainMap?

Answer:

ChainMap combines multiple mappings into a single view.

It searches the mappings from left to right.

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

The user's theme overrides the default theme.


# ============================================================
# Q30. How can Regex and Collections be combined
# for a real-world application?
# ============================================================

Answer:

Regex can be used to extract and clean information from
text, while Collections can be used to count, group, or
process the extracted data.

Example:

import re

from collections import Counter


text = """
Python is powerful.
Python is easy.
Python is popular.
"""


# Step 1: Extract words

words = re.findall(
    r"\b\w+\b",
    text.lower()
)


# Step 2: Count words

frequency = Counter(words)


# Step 3: Display most common words

print(
    frequency.most_common(5)
)


This combination can be used in:

- Text analytics
- Log analysis
- Resume analysis
- NLP preprocessing
- Data cleaning
- Search systems
- Social media analysis
- Document processing


# ============================================================
# QUICK INTERVIEW REVISION
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

.       Any character
^       Start
$       End
*       Zero or more
+       One or more
?       Zero or one
{}      Specific repetitions
[]      Character set
()      Group
|       OR


CHARACTER CLASSES:

\d      Digit
\D      Non-digit
\w      Word character
\W      Non-word character
\s      Whitespace
\S      Non-whitespace
\b      Word boundary


COLLECTIONS:

Counter
defaultdict
deque
namedtuple
OrderedDict
ChainMap


COUNTER:

Counter()
most_common()


DEFAULTDICT:

defaultdict(list)
defaultdict(int)
defaultdict(set)


DEQUE:

append()
appendleft()
pop()
popleft()


# ============================================================
# DAY 19 INTERVIEW GOAL
# ============================================================

After completing these 30 questions, you should be able to
explain:

1. What Regex is
2. How the re module works
3. Difference between search(), match(), and fullmatch()
4. How findall() and finditer() work
5. Regex quantifiers
6. Character classes
7. Groups and word boundaries
8. Regex flags
9. Counter
10. defaultdict
11. deque
12. namedtuple
13. ChainMap
14. Practical Regex + Collections applications