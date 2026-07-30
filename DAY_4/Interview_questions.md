# 🚀 DAY 04 – Python Strings Interview Questions

## 📚 Topic
Python Strings

---

# 1. What is a string in Python?

**Answer:**
A string is a sequence of characters enclosed within single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

Example:

```python
name = "Python"
```

---

# 2. Are Python strings mutable or immutable?

**Answer:**
Python strings are **immutable**, which means once a string is created, it cannot be changed directly.

Example:

```python
text = "Python"

# ❌ Invalid
# text[0] = "J"

# ✅ Correct
text = "Jython"
```

---

# 3. How do you create a string?

**Answer:**

```python
name = "Amir"
city = 'Patna'
message = """Welcome"""
```

---

# 4. What is string indexing?

**Answer:**
Indexing allows us to access individual characters in a string.

Example:

```python
text = "Python"

print(text[0])
```

Output

```
P
```

---

# 5. What is negative indexing?

**Answer:**
Negative indexing starts from the end of the string.

Example:

```python
text = "Python"

print(text[-1])
```

Output

```
n
```

---

# 6. What is string slicing?

**Answer:**
Slicing extracts a portion of a string.

Syntax

```python
string[start:stop:step]
```

Example

```python
text = "Python"

print(text[1:4])
```

Output

```
yth
```

---

# 7. How do you reverse a string?

**Answer:**

```python
text = "Python"

print(text[::-1])
```

Output

```
nohtyP
```

---

# 8. How do you find the length of a string?

**Answer:**

```python
len(text)
```

---

# 9. What is the difference between upper() and lower()?

**Answer:**

upper() converts all characters to uppercase.

lower() converts all characters to lowercase.

---

# 10. What does title() do?

**Answer:**

It converts the first letter of every word into uppercase.

Example

```python
"python programming".title()
```

Output

```
Python Programming
```

---

# 11. What is capitalize()?

**Answer:**

It capitalizes only the first character of the string.

---

# 12. What is replace()?

**Answer:**

Used to replace one substring with another.

Example

```python
text.replace("Python", "Java")
```

---

# 13. What is split()?

**Answer:**

It converts a string into a list.

Example

```python
sentence = "I Love Python"

sentence.split()
```

---

# 14. What is join()?

**Answer:**

It joins list elements into one string.

Example

```python
"-".join(["AI","ML"])
```

Output

```
AI-ML
```

---

# 15. What is strip()?

**Answer:**

It removes extra spaces from the beginning and end of a string.

---

# 16. What is find()?

**Answer:**

It returns the index of the first occurrence of a substring.

---

# 17. What is count()?

**Answer:**

It counts how many times a character or substring appears.

---

# 18. What is string concatenation?

**Answer:**

Joining two or more strings.

Example

```python
first = "Hello"

second = "World"

print(first + " " + second)
```

---

# 19. How do you repeat a string?

**Answer:**

```python
print("Hi" * 3)
```

Output

```
HiHiHi
```

---

# 20. How do you check whether a substring exists?

**Answer:**

Using the **in** operator.

Example

```python
"AI" in "OpenAI"
```

---

# 21. How do you compare two strings?

**Answer:**

Using comparison operators.

```python
if str1 == str2:
    print("Equal")
```

---

# 22. How do you check if a string is a palindrome?

**Answer:**

Compare the string with its reverse.

```python
text == text[::-1]
```

---

# 23. What is an anagram?

**Answer:**

Two strings are anagrams if they contain the same characters in a different order.

Example:

```
listen
silent
```

---

# 24. What is a substring?

**Answer:**

A substring is a smaller part of a string.

Example:

```
Python

Substring = "thon"
```

---

# 25. How do you remove duplicate characters?

**Answer:**

By traversing the string and storing only unique characters.

---

# 26. Give some real-world applications of strings.

**Answer:**

- Chat Applications
- Search Engines
- Email Validation
- Password Validation
- AI Chatbots
- NLP
- Resume Parsing

---

# 27. What are escape characters?

**Answer:**

Special characters used inside strings.

Examples:

```
\n

\t

\\

\"
```

---

# 28. Why are strings important in AI?

**Answer:**

Strings are used in:

- Natural Language Processing (NLP)
- Chatbots
- Sentiment Analysis
- Text Classification
- Translation Systems

---

# 29. What are common mistakes while working with strings?

**Answer:**

- Wrong indexing
- Incorrect slicing
- Forgetting immutability
- Case-sensitive comparisons
- Ignoring whitespace

---

# 30. Why should every Python programmer master strings?

**Answer:**

Because almost every real-world application involves processing text. Mastering strings improves problem-solving skills and is essential for web development, automation, data analysis, and AI applications.

---

# 🎯 Interview Tips

✅ Learn indexing thoroughly.

✅ Practice slicing questions.

✅ Remember strings are immutable.

✅ Master common string methods.

✅ Practice palindrome and anagram problems.

✅ Solve real interview coding questions.

---

# 🌟 Key Takeaway

> "Strings are the language of computers. Master them to build smarter applications."