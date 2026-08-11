
# 🚀 DAY 17 / 365 — MINI PROJECT

# 🧠 SMART DATA PROCESSOR USING ITERATORS & GENERATORS

---

## 📅 Project Information

**Project Name:** Smart Data Processor Using Iterators & Generators

**Day:** 17 / 365

**Language:** Python

**Project Type:** Python Mini Project

---

# 📌 PROJECT DESCRIPTION

The **Smart Data Processor** is a Python mini project created to demonstrate the practical use of **Iterators and Generators**.

The project processes a collection of numbers step by step using iterators, generator functions, generator expressions, filtering, and data transformation.

The main purpose of this project is to understand how Python can process data efficiently without unnecessarily storing every intermediate result in memory.

---

# 🎯 PROJECT OBJECTIVES

The main objectives of this project are:

- Understand Python iterators
- Use `iter()`
- Use `next()`
- Understand `StopIteration`
- Create generator functions
- Use `yield`
- Create generator expressions
- Understand lazy evaluation
- Filter data using generators
- Transform data using generators
- Create a generator pipeline
- Practice memory-efficient data processing

---

# 🧠 CONCEPTS USED

```text
Iterables
Iterators
iter()
next()
StopIteration
Custom Iterator Concepts
Generators
yield
Generator Functions
Generator Expressions
Lazy Evaluation
Data Filtering
Data Transformation
Generator Pipeline
````

---

# 🔄 HOW THE PROJECT WORKS

The project starts with a list of numbers.

```python
numbers = [
    12, 5, 28, 7, 44,
    19, 60, 3, 72, 15,
    90, 21, 36, 8, 55
]
```

The data then passes through different processing stages.

```text
Input Data
    ↓
Iterator
    ↓
Even Number Generator
    ↓
Square Generator
    ↓
Filter Values > 100
    ↓
Final Result
```

---

# ⚙️ PROJECT FEATURES

## 1. Iterator Processing

The project converts the list into an iterator using:

```python
iter(data)
```

The next values are retrieved using:

```python
next(iterator)
```

---

## 2. Even Number Generator

The project generates only even numbers.

Example:

```python
def even_numbers(data):

    for number in data:

        if number % 2 == 0:

            yield number
```

---

## 3. Square Generator

The project calculates squares using a generator.

Example:

```python
def square_numbers(data):

    for number in data:

        yield number ** 2
```

---

## 4. Value Filtering

The project filters values greater than `100`.

Example:

```python
def greater_than_100(data):

    for number in data:

        if number > 100:

            yield number
```

---

## 5. Running Total

The project also demonstrates a running total generator.

Example:

```python
def running_total(data):

    total = 0

    for number in data:

        total += number

        yield total
```

---

## 6. Generator Expression

The project demonstrates generator expressions.

Example:

```python
generator = (
    number * 2
    for number in data
    if number % 2 == 0
)
```

---

## 7. Generator Pipeline

The most important feature of the project is the generator pipeline.

Multiple generators are connected together.

```text
Input
  ↓
Even Numbers
  ↓
Squares
  ↓
Values Greater Than 100
  ↓
Final Output
```

This allows data to be processed step by step.

---

# 💻 EXAMPLE

Suppose the input is:

```text
[2, 3, 4, 5, 6]
```

First, even numbers are selected:

```text
2
4
6
```

Then squares are calculated:

```text
4
16
36
```

Then values greater than 10 are selected:

```text
16
36
```

Final result:

```text
16
36
```

---

# 🛠️ TECHNOLOGIES USED

```text
Python
Python Iterators
Python Generators
iter()
next()
yield
StopIteration
Generator Expressions
Lazy Evaluation
```

---

# 📂 PROJECT STRUCTURE

```text
Day17/
│
├── README.md
├── notes.md
├── practice_questions.md
├── practice_codes.py
├── interview_questions.md
├── mcqs.md
├── reflection.md
├── learning_outcomes.md
├── project.md
│
└── mini_project/
    │
    └── main.py
```

---

# ▶️ HOW TO RUN THE PROJECT

## Step 1

Open the project folder in VS Code.

---

## Step 2

Open the terminal.

---

## Step 3

Move into the mini project folder:

```bash
cd mini_project
```

---

## Step 4

Run the program:

```bash
python main.py
```

---

# 📊 PROJECT FLOW

```text
                 SMART DATA PROCESSOR
                          │
                          ▼
                    Input Numbers
                          │
                          ▼
                      Iterator
                          │
                          ▼
                 Even Number Filter
                          │
                          ▼
                   Square Generator
                          │
                          ▼
                 Value Filter > 100
                          │
                          ▼
                    Final Result
```

---

# 🧠 WHY USE GENERATORS?

Generators are useful because they generate values only when required.

Instead of creating and storing a complete list of intermediate values, generators can process values one at a time.

This is especially useful when working with large datasets.

---

# 💾 MEMORY EFFICIENCY

Normal list processing may store many values in memory.

Generators use lazy evaluation.

```text
Normal Processing:

All Data
   ↓
Memory
   ↓
Processing


Generator Processing:

Data
 ↓
One Value
 ↓
Process
 ↓
Next Value
 ↓
Process
```

---

# 🌍 REAL-WORLD APPLICATIONS

The concepts demonstrated in this project can be used for:

* Large file processing
* Log file processing
* Data streaming
* API data processing
* Database records
* Machine learning pipelines
* Large datasets
* Data transformation
* Memory-efficient applications
* Infinite data streams

---

# 📈 FUTURE IMPROVEMENTS

This project can be improved by adding:

* User input
* CSV file processing
* JSON file processing
* File-based data processing
* Data visualization
* Menu-driven interface
* Exception handling
* Performance comparison
* Memory usage comparison
* Large dataset testing
* Database integration

---

# 🎯 LEARNING OUTCOMES

After completing this project, I learned how to:

* Create iterators
* Use `iter()`
* Use `next()`
* Handle `StopIteration`
* Create generator functions
* Use `yield`
* Create generator expressions
* Apply lazy evaluation
* Filter data
* Transform data
* Build generator pipelines
* Process data efficiently

---

# 🏆 PROJECT ACHIEVEMENT

```text
Iterators
    ↓
iter()
    ↓
next()
    ↓
Generators
    ↓
yield
    ↓
Lazy Evaluation
    ↓
Data Filtering
    ↓
Data Transformation
    ↓
Generator Pipeline
    ↓
Smart Data Processor
    ↓
Mini Project Completed ✅
```

---

# 💡 KEY LEARNING

> Generators allow Python programs to process data one value at a time, making them especially useful for efficient and memory-conscious data processing.

---

# 🔥 365 DAYS OF GROWTH

**Day 17 / 365**

```text
████░░░░░░░░░░░░░░░░  4.7%
```

---

# 🚀 FINAL THOUGHT

This mini project helped me move from learning the theory of Iterators and Generators to actually using them in a practical Python application.

I learned that writing efficient code is not only about getting the correct output, but also about understanding how data flows through a program.

**Day 17 — Mini Project Completed 🚀**

**17 / 365 — Keep Growing.**

