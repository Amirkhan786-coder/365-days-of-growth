
#  Python Operators Complete Notes

## 1. What are Operators?

Operators are special symbols or keywords used to perform operations on values and variables.

Example:

```python
a = 10
b = 5

result = a + b

print(result)
````

Output:

```text
15
```

Here:

* `a` and `b` are operands.
* `+` is the operator.
* `result` stores the result.

---

# 2. Types of Operators in Python

Python provides several types of operators:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Membership Operators
6. Identity Operators
7. Bitwise Operators

---

# 3. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Name           | Example   | Result |
| -------- | -------------- | --------- | ------ |
| `+`      | Addition       | `10 + 5`  | `15`   |
| `-`      | Subtraction    | `10 - 5`  | `5`    |
| `*`      | Multiplication | `10 * 5`  | `50`   |
| `/`      | Division       | `10 / 5`  | `2.0`  |
| `%`      | Modulus        | `10 % 3`  | `1`    |
| `//`     | Floor Division | `10 // 3` | `3`    |
| `**`     | Exponentiation | `2 ** 3`  | `8`    |

## Addition

```python
a = 10
b = 20

print(a + b)
```

Output:

```text
30
```

## Subtraction

```python
a = 20
b = 5

print(a - b)
```

Output:

```text
15
```

## Multiplication

```python
a = 10
b = 5

print(a * b)
```

Output:

```text
50
```

## Division

```python
a = 10
b = 3

print(a / b)
```

Output:

```text
3.3333333333333335
```

The `/` operator normally returns a float.

## Modulus `%`

The modulus operator returns the remainder.

```python
print(10 % 3)
```

Output:

```text
1
```

Because:

```text
10 ÷ 3

Quotient = 3
Remainder = 1
```

Modulus is very useful for checking whether a number is even or odd.

```python
number = 10

print(number % 2)
```

Output:

```text
0
```

Therefore, `10` is even.

## Floor Division `//`

Floor division returns the floor value of the division.

```python
print(10 // 3)
```

Output:

```text
3
```

Unlike `/`:

```python
print(10 / 3)
```

Output:

```text
3.3333333333333335
```

## Exponentiation `**`

Used to calculate powers.

```python
print(2 ** 3)
```

Output:

```text
8
```

Because:

```text
2 × 2 × 2 = 8
```

---

# 4. Assignment Operators

Assignment operators are used to assign values to variables.

The basic assignment operator is:

```python
=
```

Example:

```python
x = 10
```

Here `10` is assigned to `x`.

Python also provides compound assignment operators.

| Operator | Example   | Meaning      |
| -------- | --------- | ------------ |
| `=`      | `x = 10`  | Assign       |
| `+=`     | `x += 5`  | `x = x + 5`  |
| `-=`     | `x -= 5`  | `x = x - 5`  |
| `*=`     | `x *= 5`  | `x = x * 5`  |
| `/=`     | `x /= 5`  | `x = x / 5`  |
| `//=`    | `x //= 5` | `x = x // 5` |
| `%=`     | `x %= 5`  | `x = x % 5`  |
| `**=`    | `x **= 5` | `x = x ** 5` |

Example:

```python
x = 10

x += 5

print(x)
```

Output:

```text
15
```

---

# 5. Comparison Operators

Comparison operators compare two values.

The result is always:

```text
True
```

or:

```text
False
```

Operators:

```text
==
!=
>
<
>=
<=
```

## Equal `==`

```python
print(10 == 10)
```

Output:

```text
True
```

Important:

`=` means assignment.

`==` means comparison.

Example:

```python
x = 10
print(x == 10)
```

Output:

```text
True
```

## Not Equal `!=`

```python
print(10 != 5)
```

Output:

```text
True
```

## Greater Than `>`

```python
print(10 > 5)
```

Output:

```text
True
```

## Less Than `<`

```python
print(5 < 10)
```

Output:

```text
True
```

## Greater Than or Equal `>=`

```python
print(10 >= 10)
```

Output:

```text
True
```

## Less Than or Equal `<=`

```python
print(5 <= 10)
```

Output:

```text
True
```

---

# 6. Logical Operators

Logical operators are used to combine multiple conditions.

Python provides:

```text
and
or
not
```

---

## `and`

`and` returns `True` when both conditions are true.

Example:

```python
age = 20

print(age >= 18 and age <= 60)
```

Output:

```text
True
```

Both conditions are true.

### Truth Table

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

---

# 7. `or`

`or` returns `True` if at least one condition is true.

Example:

```python
age = 17

print(age == 17 or age == 18)
```

Output:

```text
True
```

### Truth Table

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

---

# 8. `not`

`not` reverses the Boolean value.

Example:

```python
print(not True)
```

Output:

```text
False
```

Another example:

```python
print(not False)
```

Output:

```text
True
```

---

# 9. Membership Operators

Membership operators check whether a value exists inside a sequence.

Operators:

```text
in
not in
```

They are commonly used with:

* Strings
* Lists
* Tuples
* Sets
* Dictionaries

Example:

```python
name = "Amir"

print("A" in name)
```

Output:

```text
True
```

Another example:

```python
name = "Amir"

print("z" in name)
```

Output:

```text
False
```

Using `not in`:

```python
name = "Amir"

print("z" not in name)
```

Output:

```text
True
```

---

# 10. Identity Operators

Identity operators check whether two variables refer to the same object.

Operators:

```text
is
is not
```

Example:

```python
x = None

print(x is None)
```

Output:

```text
True
```

`is` is different from `==`.

`==` checks whether values are equal.

`is` checks whether objects are identical.

For example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

The values are equal, but they are different list objects.

---

# 11. Bitwise Operators

Bitwise operators work with numbers at the binary level.

Operators:

```text
&
|
^
~
<<
>>
```

These operators are more advanced but are important for understanding low-level programming and computer systems.

---

## Bitwise AND `&`

```python
a = 5
b = 3

print(a & b)
```

Output:

```text
1
```

Binary representation:

```text
5 = 101
3 = 011

101
011
---
001
```

Therefore:

```text
1
```

---

## Bitwise OR `|`

```python
a = 5
b = 3

print(a | b)
```

Output:

```text
7
```

---

## Bitwise XOR `^`

```python
a = 5
b = 3

print(a ^ b)
```

Output:

```text
6
```

---

## Bitwise NOT `~`

```python
a = 5

print(~a)
```

Output:

```text
-6
```

---

## Left Shift `<<`

```python
print(5 << 1)
```

Output:

```text
10
```

---

## Right Shift `>>`

```python
print(5 >> 1)
```

Output:

```text
2
```

---

# 12. Operator Precedence

When multiple operators are used in one expression, Python follows a specific order.

Example:

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

Why?

Multiplication happens before addition.

```text
10 + 5 * 2
10 + 10
20
```

---

# 13. Parentheses

Parentheses can be used to control the order of operations.

Example:

```python
result = (10 + 5) * 2

print(result)
```

Output:

```text
30
```

Without parentheses:

```python
result = 10 + 5 * 2
```

Result:

```text
20
```

With parentheses:

```python
result = (10 + 5) * 2
```

Result:

```text
30
```

---

# 14. Basic Precedence Order

A simplified order is:

```text
1. Parentheses       ()
2. Exponentiation    **
3. Unary operators   +x, -x, ~x
4. *, /, //, %
5. +, -
6. Comparisons       <, >, ==, !=, <=, >=
7. not
8. and
9. or
```

When in doubt, use parentheses to make your intention clear.

---

# 15. Real-World Example — Calculator

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Remainder:", a % b)
```

---

# 16. Real-World Example — Even or Odd

The modulus operator is useful for checking even and odd numbers.

```python
number = int(input("Enter a number: "))

print(number % 2)
```

If the result is `0`, the number is even.

If the result is not `0`, the number is odd.

We will use this concept with `if-else` in upcoming days.

---

# 17. Real-World Example — Eligibility

Comparison and logical operators can be combined.

```python
age = int(input("Enter your age: "))

print(age >= 18)
```

If age is 20:

```text
True
```

This concept will become very important when learning conditional statements.

---

# 18. Important Difference: `=` vs `==`

This is a very common beginner mistake.

Assignment:

```python
x = 10
```

Comparison:

```python
x == 10
```

Remember:

```text
=   → Assign value

==  → Compare values
```

---

# 19. Important Difference: `/` vs `//`

Normal division:

```python
print(10 / 3)
```

Output:

```text
3.3333333333333335
```

Floor division:

```python
print(10 // 3)
```

Output:

```text
3
```

---

# 20. Important Difference: `%` vs `/`

Division:

```python
10 / 3
```

gives:

```text
3.3333333333333335
```

Modulus:

```python
10 % 3
```

gives:

```text
1
```

Division gives the quotient.

Modulus gives the remainder.

---

# 21. Common Beginner Mistakes

## Mistake 1

Using `=` instead of `==` for comparison.

Wrong concept:

```python
x = 10
```

when you want to compare.

Correct:

```python
x == 10
```

---

## Mistake 2

Forgetting that `/` produces a float.

```python
print(10 / 2)
```

Output:

```text
5.0
```

---

## Mistake 3

Confusing `%` with percentage.

In Python:

```text
% = Modulus / Remainder
```

---

## Mistake 4

Ignoring operator precedence.

Example:

```python
10 + 5 * 2
```

Result:

```text
20
```

not:

```text
30
```

---

# 22. Operators and Programming

Operators are used everywhere in programming.

They are required for:

* Calculations
* Conditions
* Loops
* Algorithms
* Data Structures
* Searching
* Sorting
* Games
* Applications
* Data Analysis
* Machine Learning
* Artificial Intelligence

For an AIML student, operators are fundamental because mathematical calculations are heavily used in:

* Statistics
* Probability
* Linear Algebra
* Machine Learning
* Data Processing
* Model Evaluation

---

# 🧠 Quick Revision

```text
Arithmetic
+
-
*
/
%
//
**

Assignment
=
+=
-=
*=
/=
%=

Comparison
==
!=
>
<
>=
<=

Logical
and
or
not

Membership
in
not in

Identity
is
is not

Bitwise
&
|
^
~
<<
>>
```

---

# 🎯 Day 005 Learning Checklist

* [ ] Understand arithmetic operators
* [ ] Understand modulus
* [ ] Understand floor division
* [ ] Understand exponentiation
* [ ] Understand assignment operators
* [ ] Understand comparison operators
* [ ] Understand logical operators
* [ ] Understand membership operators
* [ ] Understand identity operators
* [ ] Understand basic bitwise operators
* [ ] Understand operator precedence
* [ ] Solve practice questions
* [ ] Build the mini project

---

# 🚀 Learning Pattern

```text
Learn
  ↓
Understand
  ↓
Write Code
  ↓
Run Code
  ↓
Make Mistakes
  ↓
Debug
  ↓
Practice
  ↓
Build Project
```

## 💡 Final Takeaway

Operators may look simple, but they are one of the most important foundations of programming.

Mastering operators will make upcoming topics such as:

* if-else
* loops
* functions
* DSA
* algorithms
* data analysis
* machine learning

much easier.

