
# Questions & Answers

## Python Operators

---

# 🟢 BASIC QUESTIONS

### Q1. What is an operator?

An operator is a symbol or keyword used to perform an operation on one or more values.

Example:

```python
a = 10
b = 5

print(a + b)
````

Here:

* `a` and `b` are operands.
* `+` is the operator.

---

### Q2. What are operands?

Operands are the values or variables on which an operator performs an operation.

Example:

```python
10 + 5
```

Here:

* `10` → Operand
* `+` → Operator
* `5` → Operand

---

### Q3. What are the main types of operators in Python?

The main types are:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Membership Operators
6. Identity Operators
7. Bitwise Operators

---

# 🟢 ARITHMETIC OPERATORS

### Q4. What is the use of `+`?

It is used for addition.

```python
print(10 + 5)
```

Output:

```text
15
```

---

### Q5. What is the use of `-`?

It is used for subtraction.

```python
print(10 - 5)
```

Output:

```text
5
```

---

### Q6. What is the use of `*`?

It is used for multiplication.

```python
print(10 * 5)
```

Output:

```text
50
```

---

### Q7. What is the use of `/`?

It performs normal division and returns a floating-point result.

```python
print(10 / 3)
```

Output:

```text
3.3333333333333335
```

---

### Q8. What is the use of `%`?

The modulus operator returns the remainder.

```python
print(10 % 3)
```

Output:

```text
1
```

---

### Q9. What is the use of `//`?

It performs floor division.

```python
print(10 // 3)
```

Output:

```text
3
```

---

### Q10. What is the use of `**`?

It is used for exponentiation or power.

```python
print(2 ** 3)
```

Output:

```text
8
```

---

# 🟡 IMPORTANT DIFFERENCES

### Q11. Difference between `/` and `//`?

`/` performs normal division.

```python
10 / 3
```

Result:

```text
3.3333333333333335
```

`//` performs floor division.

```python
10 // 3
```

Result:

```text
3
```

---

### Q12. Difference between `=` and `==`?

`=` is an assignment operator.

```python
x = 10
```

It assigns `10` to `x`.

`==` is a comparison operator.

```python
x == 10
```

It checks whether `x` is equal to `10`.

---

### Q13. Difference between `%` and `/`?

`/` gives the division result.

```python
10 / 3
```

Result:

```text
3.3333333333333335
```

`%` gives the remainder.

```python
10 % 3
```

Result:

```text
1
```

---

# 🟡 ASSIGNMENT OPERATORS

### Q14. What does `+=` do?

It adds a value to the existing variable.

```python
x = 10
x += 5
```

Equivalent to:

```python
x = x + 5
```

Result:

```text
15
```

---

### Q15. What does `-=` do?

It subtracts a value from the existing variable.

```python
x = 10
x -= 3
```

Result:

```text
7
```

---

### Q16. What does `*=` do?

It multiplies the existing value.

```python
x = 10
x *= 2
```

Result:

```text
20
```

---

### Q17. What does `/=` do?

It divides the existing value.

```python
x = 10
x /= 2
```

Result:

```text
5.0
```

---

# 🟡 COMPARISON OPERATORS

### Q18. What are comparison operators?

Comparison operators compare two values.

They are:

```text
==
!=
>
<
>=
<=
```

They return:

```text
True
```

or:

```text
False
```

---

### Q19. What does `>` mean?

Greater than.

```python
print(10 > 5)
```

Output:

```text
True
```

---

### Q20. What does `<` mean?

Less than.

```python
print(5 < 10)
```

Output:

```text
True
```

---

### Q21. What does `>=` mean?

Greater than or equal to.

```python
print(10 >= 10)
```

Output:

```text
True
```

---

### Q22. What does `<=` mean?

Less than or equal to.

```python
print(5 <= 10)
```

Output:

```text
True
```

---

# 🟠 LOGICAL OPERATORS

### Q23. What are logical operators?

Logical operators are used to combine or reverse conditions.

Python provides:

```text
and
or
not
```

---

### Q24. How does `and` work?

`and` returns `True` only when both conditions are true.

```python
age = 20

print(age >= 18 and age <= 60)
```

Output:

```text
True
```

---

### Q25. How does `or` work?

`or` returns `True` when at least one condition is true.

```python
age = 20

print(age == 20 or age == 25)
```

Output:

```text
True
```

---

### Q26. How does `not` work?

`not` reverses a Boolean value.

```python
print(not True)
```

Output:

```text
False
```

---

# 🟠 MEMBERSHIP OPERATORS

### Q27. What are membership operators?

Membership operators check whether a value exists inside a sequence.

They are:

```text
in
not in
```

Example:

```python
name = "Amir"

print("A" in name)
```

Output:

```text
True
```

---

### Q28. Give an example of `not in`.

```python
languages = ["Python", "Java", "C"]

print("JavaScript" not in languages)
```

Output:

```text
True
```

---

# 🟠 IDENTITY OPERATORS

### Q29. What are identity operators?

Identity operators check whether two references point to the same object.

They are:

```text
is
is not
```

---

### Q30. What is the difference between `==` and `is`?

`==` checks whether values are equal.

`is` checks whether two references point to the same object.

Example:

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

---

# 🔴 BITWISE OPERATORS

### Q31. What are bitwise operators?

Bitwise operators perform operations on the binary representation of numbers.

They are:

```text
&
|
^
~
<<
>>
```

---

### Q32. What does `&` do?

It performs bitwise AND.

Example:

```python
print(5 & 3)
```

Output:

```text
1
```

---

### Q33. What does `|` do?

It performs bitwise OR.

```python
print(5 | 3)
```

Output:

```text
7
```

---

### Q34. What does `^` do?

It performs bitwise XOR.

```python
print(5 ^ 3)
```

Output:

```text
6
```

---

### Q35. What does `~` do?

It performs bitwise NOT.

```python
print(~5)
```

Output:

```text
-6
```

---

### Q36. What does `<<` do?

It shifts the bits to the left.

```python
print(5 << 1)
```

Output:

```text
10
```

---

### Q37. What does `>>` do?

It shifts the bits to the right.

```python
print(5 >> 1)
```

Output:

```text
2
```

---

# 🔴 OPERATOR PRECEDENCE

### Q38. What is operator precedence?

Operator precedence determines the order in which Python evaluates operators in an expression.

Example:

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

Multiplication is performed before addition.

---

### Q39. How can parentheses change the result?

Without parentheses:

```python
10 + 5 * 2
```

Result:

```text
20
```

With parentheses:

```python
(10 + 5) * 2
```

Result:

```text
30
```

---

# 🔥 OUTPUT-BASED QUESTIONS

### Q40.

What is the output?

```python
print(20 % 6)
```

Answer:

```text
2
```

---

### Q41.

What is the output?

```python
print(20 // 6)
```

Answer:

```text
3
```

---

### Q42.

What is the output?

```python
print(3 ** 3)
```

Answer:

```text
27
```

---

### Q43.

What is the output?

```python
x = 10
x += 10

print(x)
```

Answer:

```text
20
```

---

### Q44.

What is the output?

```python
print(10 > 20)
```

Answer:

```text
False
```

---

### Q45.

What is the output?

```python
print(10 == 10)
```

Answer:

```text
True
```

---

### Q46.

What is the output?

```python
print(True and False)
```

Answer:

```text
False
```

---

### Q47.

What is the output?

```python
print(True or False)
```

Answer:

```text
True
```

---

### Q48.

What is the output?

```python
print(not False)
```

Answer:

```text
True
```

---

### Q49.

What is the output?

```python
print("Python" in "I love Python")
```

Answer:

```text
True
```

---

### Q50.

What is the output?

```python
print(2 + 3 * 4)
```

Answer:

```text
14
```

---

# 🏆 INTERVIEW QUESTIONS

### Q51. Which operator is used to find the remainder?

Answer:

```text
%
```

---

### Q52. Which operator is used for power?

Answer:

```text
**
```

---

### Q53. Which operator is used for floor division?

Answer:

```text
//
```

---

### Q54. Which operators return Boolean values?

Comparison operators return Boolean values.

Examples:

```text
==
!=
>
<
>=
<=
```

Logical expressions also produce Boolean results.

---

### Q55. What is Boolean?

Boolean is a data type with two values:

```text
True
False
```

---

### Q56. Can operators be combined?

Yes.

Example:

```python
age = 20

result = age >= 18 and age <= 60
```

---

### Q57. Why are operators important?

Operators are fundamental to programming.

They are used in:

* Calculations
* Conditions
* Loops
* Algorithms
* Data Structures
* DSA
* Data Analysis
* Machine Learning
* AI applications

---

# 🧠 FINAL REVISION

```text
Arithmetic
+  -  *  /  %  //  **

Assignment
=  +=  -=  *=  /=  %=  //=  **=

Comparison
==  !=  >  <  >=  <=

Logical
and  or  not

Membership
in  not in

Identity
is  is not

Bitwise
&  |  ^  ~  <<  >>
```

---

#  DAY 005 COMPLETE

```text
Theory       ✅
Notes        ✅
Coding       ✅
Practice     ✅
Q&A          ✅
Mini Project ✅
Revision     ✅
```

## 365 Days of Growth

**Day 005 / 365 — Python Operators**

> Learn the concept.
> Write the code.
> Solve the problem.
> Build something.
> Repeat every day. 🚀

