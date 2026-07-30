# 🚀 DAY 04 – Python Strings

> "Strings are one of the most important data types in Python. Almost every real-world application works with text."

---

# 📚 What is a String?

A string is a sequence of characters enclosed inside single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

Examples:

```python
name = "Amir Khan"

college = 'XYZ College'

message = """Welcome to Python"""
```

---

# Why are Strings Important?

Strings are used everywhere.

Examples

• Login Systems

• Chat Applications

• Search Engines

• AI Chatbots

• Password Validation

• Email Processing

• Text Analysis

• Machine Learning

---

# Creating Strings

```python
name = "Python"

city = 'Patna'

message = """Hello World"""
```

---

# Accessing Characters

Python uses Indexing.

Example

```python
language = "Python"

print(language[0])

print(language[1])

print(language[-1])
```

Output

```
P

y

n
```

---

# String Indexing

Positive Index

```
P  y  t  h  o  n

0  1  2  3  4  5
```

Negative Index

```
P  y  t  h  o  n

-6 -5 -4 -3 -2 -1
```

---

# String Slicing

Syntax

```python
string[start:stop:step]
```

Example

```python
text = "Python"

print(text[0:3])

print(text[2:])

print(text[:4])

print(text[::-1])
```

Output

```
Pyt

thon

Pyth

nohtyP
```

---

# String Length

```python
text = "Python"

print(len(text))
```

Output

```
6
```

---

# Common String Methods

## upper()

```python
text.upper()
```

Output

```
PYTHON
```

---

## lower()

```python
text.lower()
```

Output

```
python
```

---

## title()

```python
"python programming".title()
```

Output

```
Python Programming
```

---

## capitalize()

```python
text.capitalize()
```

Output

```
Python
```

---

## replace()

```python
text.replace("Python","Java")
```

---

## find()

```python
text.find("th")
```

---

## count()

```python
text.count("o")
```

---

## split()

```python
sentence = "I Love Python"

sentence.split()
```

Output

```
['I', 'Love', 'Python']
```

---

## join()

```python
words = ["Python","AI","ML"]

"-".join(words)
```

Output

```
Python-AI-ML
```

---

## strip()

Removes extra spaces.

```python
text.strip()
```

---

# Membership Operators

```python
"Py" in "Python"
```

Output

```
True
```

---

# String Comparison

```python
print("abc"=="abc")

print("abc"=="ABC")
```

---

# Escape Characters

```
\n New Line

\t Tab

\" Double Quote

\\ Backslash
```

---

# String Concatenation

```python
first = "Hello"

second = "World"

print(first + " " + second)
```

Output

```
Hello World
```

---

# String Repetition

```python
print("Python "*3)
```

Output

```
Python Python Python
```

---

# String Immutability

Strings cannot be modified directly.

Incorrect

```python
name="Python"

name[0]="J"
```

Correct

```python
name="Jython"
```

---

# Real-Life Applications

✅ Chat Applications

✅ Password Validation

✅ Email Processing

✅ Search Engines

✅ AI Chatbots

✅ Resume Parsing

✅ NLP

✅ Data Cleaning

---

# Common Mistakes

❌ Wrong Index

❌ Forgetting Quotes

❌ Incorrect Slicing

❌ Using replace() without assignment

---

# Interview Tips

✔ String vs List

✔ Indexing

✔ Slicing

✔ String Methods

✔ Immutability

✔ Membership Operators

---

# Quick Revision

✅ Strings

✅ Indexing

✅ Slicing

✅ String Methods

✅ Length

✅ Concatenation

✅ Membership

✅ Escape Characters

---

# Learning Outcome

After completing Day 04, I can:

✔ Create strings

✔ Access characters

✔ Slice strings

✔ Use important string methods

✔ Solve string-based problems

✔ Build mini projects using strings

---

# Quote of the Day

> "Master Strings today, and tomorrow you'll master text processing in AI and Machine Learning."