# Day 19 Mini Project — Smart Text Analyzer

## 1. Project Title

Smart Text Analyzer

---

## 2. Project Overview

Smart Text Analyzer is a Python command-line application
that analyzes user-provided text and extracts useful
information from it.

The project uses:

- Regular Expressions
- Counter
- Sets
- String Processing

It demonstrates how Python can process unstructured text
and convert it into useful information.

---

## 3. Problem Statement

A large amount of information is stored as plain text.

Finding emails, URLs, numbers, hashtags, mentions, and
frequently used words manually can be difficult.

This project automates basic text analysis using Python.

---

## 4. Objectives

The application should:

1. Accept text from the user.
2. Count total words.
3. Count unique words.
4. Find the top 5 most common words.
5. Extract numbers.
6. Extract email addresses.
7. Extract URLs.
8. Extract hashtags.
9. Extract @mentions.
10. Calculate character frequency.
11. Calculate word frequency.

---

## 5. Technologies Used

### Programming Language

Python 3

### Modules

```python
import re
from collections import Counter

6. Python Concepts Used
Regular Expressions

Used for:

Extracting numbers
Extracting emails
Extracting URLs
Extracting hashtags
Extracting mentions
Extracting words
Counter

Used for:

Word frequency
Character frequency
Finding most common words
Set

Used for:

Finding unique words
String Processing

Used for:

Lowercase conversion
Text cleaning
Input processing
7. Project Workflow
User Input
    ↓
Text Processing
    ↓
Regex Extraction
    ↓
Word Analysis
    ↓
Counter
    ↓
Generate Report
    ↓
Display Results
8. Features
Feature 1 — Total Word Count

Counts the total number of words in the entered text.

Feature 2 — Unique Word Count

Counts how many different words are present.

Feature 3 — Top 5 Words

Displays the five most frequently occurring words.

Feature 4 — Number Extraction

Extracts numbers from the text.

Example:

Python 2026

Output:

2026
Feature 5 — Email Extraction

Extracts email addresses.

Example:

Contact: amir@gmail.com

Output:

amir@gmail.com
Feature 6 — URL Extraction

Extracts HTTP and HTTPS URLs.

Example:

https://github.com
Feature 7 — Hashtag Extraction

Extracts hashtags.

Example:

#Python
#AI
#Coding
Feature 8 — Mention Extraction

Extracts mentions.

Example:

@developer
@amir
Feature 9 — Character Frequency

Counts how many times each character appears.

Feature 10 — Word Frequency

Counts how many times each word appears.

9. Example Input
Python is amazing.
I am learning Python in 2026.
Contact: amir@gmail.com
Visit https://github.com
#Python #Coding
Follow @developer
10. Example Output
==================================================
             SMART TEXT ANALYZER
==================================================


--- BASIC STATISTICS ---


Total Words: ...


Unique Words: ...


--- TOP 5 WORDS ---


python -> ...
is -> ...
amazing -> ...
...


--- NUMBERS ---


2026


--- EMAILS ---


amir@gmail.com


--- URLs ---


https://github.com


--- HASHTAGS ---


#Python
#Coding


--- MENTIONS ---


@developer


--- CHARACTER FREQUENCY ---


...


--- WORD FREQUENCY ---


python -> ...
...


==================================================
       ANALYSIS COMPLETED SUCCESSFULLY
==================================================

The exact word counts depend on the input.

11. Project Structure
Day-19/
│
├── mini-project/
│   │
│   ├── mini_project.md
│   └── smart_text_analyzer.py
│
└── README.md
12. How to Run

Open the terminal inside the mini-project folder.

Run:

python smart_text_analyzer.py

Enter your paragraph when prompted.

13. Sample Test Input
Python is powerful and Python is easy.
I am learning Python in 2026.
Email me at amir@gmail.com.
Visit https://github.com.
#Python #Coding
Follow @developer.
14. Learning Outcomes

After completing this project, I can:

Use Python Regular Expressions.
Extract useful information from text.
Validate and process strings.
Use Counter for frequency analysis.
Use sets for unique values.
Combine multiple Python concepts in one application.
Build a practical command-line text analyzer.
15. Future Improvements

The project can be extended with:

GUI interface
File upload
PDF text analysis
CSV export
Graphs and charts
Sentiment analysis
Keyword extraction
Stop-word removal
NLP integration
AI-powered text analysis