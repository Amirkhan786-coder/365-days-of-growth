# 🚀 DAY 06 — PYTHON TUPLES
# ❓ MCQs

## 365 Days of Growth

---

## Q1. Tuple ko Python me kaise represent kiya jata hai?

A. `[ ]`  
B. `( )`  
C. `{ }`  
D. `< >`

**Answer:** B. `( )`

---

## Q2. Tuple ki sabse important property kya hai?

A. Mutable  
B. Immutable  
C. Unordered  
D. Random

**Answer:** B. Immutable

---

## Q3. Python me indexing kis number se start hoti hai?

A. 1  
B. -1  
C. 0  
D. 2

**Answer:** C. 0

---

## Q4. Is Tuple ka first element kya hoga?

```python
numbers = (10, 20, 30)
```

A. 10  
B. 20  
C. 30  
D. Error

**Answer:** A. 10

---

## Q5. Iska output kya hoga?

```python
numbers = (10, 20, 30)
print(numbers[-1])
```

A. 10  
B. 20  
C. 30  
D. Error

**Answer:** C. 30

---

## Q6. Tuple ki length kaise find karenge?

A. `length()`  
B. `size()`  
C. `len()`  
D. `count()`

**Answer:** C. `len()`

---

## Q7. Single-element Tuple ka correct syntax kya hai?

A. `(10)`  
B. `[10]`  
C. `(10,)`  
D. `{10}`

**Answer:** C. `(10,)`

---

## Q8. `(10)` ka data type kya hoga?

A. Tuple  
B. List  
C. Integer  
D. Set

**Answer:** C. Integer

---

## Q9. Tuple me duplicate values allowed hain?

A. Yes  
B. No  
C. Only strings  
D. Only numbers

**Answer:** A. Yes

---

## Q10. Tuple me different data types store kar sakte hain?

A. Yes  
B. No  
C. Only numbers  
D. Only strings

**Answer:** A. Yes

---

# 🟡 INTERMEDIATE MCQs

## Q11. Output kya hoga?

```python
numbers = (10, 20, 30, 40)
print(numbers[1:3])
```

A. `(10, 20)`  
B. `(20, 30)`  
C. `(20, 30, 40)`  
D. `(10, 20, 30)`

**Answer:** B. `(20, 30)`

---

## Q12. Tuple ko reverse karne ke liye kaunsa slicing use kar sakte hain?

A. `[::1]`  
B. `[::2]`  
C. `[::-1]`  
D. `[1::]`

**Answer:** C. `[::-1]`

---

## Q13. `count()` method ka use kisliye hota hai?

A. Index find karne ke liye  
B. Element count karne ke liye  
C. Tuple delete karne ke liye  
D. Tuple reverse karne ke liye

**Answer:** B. Element count karne ke liye

---

## Q14. `index()` method kya return karta hai?

A. Element ka value  
B. Tuple ki length  
C. Element ka index  
D. Tuple ka size

**Answer:** C. Element ka index

---

## Q15. Output kya hoga?

```python
numbers = (10, 20, 10, 30)
print(numbers.count(10))
```

A. 1  
B. 2  
C. 3  
D. 4

**Answer:** B. 2

---

## Q16. Output kya hoga?

```python
numbers = (10, 20, 30)
print(20 in numbers)
```

A. True  
B. False  
C. 20  
D. Error

**Answer:** A. True

---

## Q17. Tuple ko List me convert karne ke liye kya use karenge?

A. `tuple()`  
B. `list()`  
C. `convert()`  
D. `change()`

**Answer:** B. `list()`

---

## Q18. List ko Tuple me convert karne ke liye kya use karenge?

A. `tuple()`  
B. `list()`  
C. `convert()`  
D. `change()`

**Answer:** A. `tuple()`

---

## Q19. Do Tuples ko combine karne ke liye kaunsa operator use hota hai?

A. `-`  
B. `*`  
C. `+`  
D. `/`

**Answer:** C. `+`

---

## Q20. Tuple repetition ke liye kaunsa operator use hota hai?

A. `+`  
B. `*`  
C. `/`  
D. `%`

**Answer:** B. `*`

---

# 🟠 ADVANCED MCQs

## Q21. Tuple packing kya hai?

A. Tuple delete karna  
B. Multiple values ko Tuple me store karna  
C. Tuple ko List me convert karna  
D. Tuple ko reverse karna

**Answer:** B. Multiple values ko Tuple me store karna

---

## Q22. Tuple unpacking kya hai?

A. Tuple ko delete karna  
B. Tuple elements ko separate variables me assign karna  
C. Tuple ko reverse karna  
D. Tuple ko sort karna

**Answer:** B. Tuple elements ko separate variables me assign karna

---

## Q23. Output kya hoga?

```python
student = ("Amir", 101, 85)

name, roll, marks = student

print(name)
```

A. Amir  
B. 101  
C. 85  
D. Error

**Answer:** A. Amir

---

## Q24. Nested Tuple kya hota hai?

A. Empty Tuple  
B. Tuple ke andar Tuple  
C. Tuple ke andar List only  
D. Duplicate Tuple

**Answer:** B. Tuple ke andar Tuple

---

## Q25. Output kya hoga?

```python
data = (
    ("Amir", 101),
    ("Rahul", 102)
)

print(data[1][0])
```

A. Amir  
B. 101  
C. Rahul  
D. 102

**Answer:** C. Rahul

---

## Q26. Tuple ko modify karne ki koshish karne par generally kya hoga?

```python
numbers = (10, 20, 30)
numbers[0] = 100
```

A. Value change ho jayegi  
B. TypeError  
C. IndexError  
D. ValueError

**Answer:** B. TypeError

---

## Q27. Inme se kaunsa Tuple method hai?

A. `append()`  
B. `remove()`  
C. `count()`  
D. `sort()`

**Answer:** C. `count()`

---

## Q28. Inme se kaunsa Tuple method nahi hai?

A. `count()`  
B. `index()`  
C. `append()`  
D. None

**Answer:** C. `append()`

---

## Q29. Tuple ka first index kya hota hai?

A. 0  
B. 1  
C. -1  
D. 2

**Answer:** A. 0

---

## Q30. Tuple ka last element negative indexing me kis index par hota hai?

A. 0  
B. 1  
C. -1  
D. -2

**Answer:** C. -1

---

# 🔴 OUTPUT-BASED MCQs

## Q31. Output kya hoga?

```python
x = (1, 2, 3)
print(len(x))
```

A. 2  
B. 3  
C. 4  
D. Error

**Answer:** B. 3

---

## Q32. Output kya hoga?

```python
x = (1, 2, 3)
print(x[0] + x[2])
```

A. 3  
B. 4  
C. 5  
D. 6

**Answer:** C. 4

---

## Q33. Output kya hoga?

```python
x = (1, 2, 3)
print(x * 2)
```

A. `(2, 4, 6)`  
B. `(1, 2, 3, 1, 2, 3)`  
C. `(1, 2, 3, 2)`  
D. Error

**Answer:** B. `(1, 2, 3, 1, 2, 3)`

---

## Q34. Output kya hoga?

```python
x = (10, 20, 30, 40)
print(x[::-1])
```

A. `(10, 20, 30, 40)`  
B. `(40, 30, 20, 10)`  
C. `(20, 30)`  
D. Error

**Answer:** B. `(40, 30, 20, 10)`

---

## Q35. Output kya hoga?

```python
x = (10, 20, 10, 30)
print(x.index(10))
```

A. 0  
B. 1  
C. 2  
D. 3

**Answer:** A. 0

---

# 🧠 CONCEPT MCQs

## Q36. List aur Tuple me main difference kya hai?

A. List ordered hoti hai, Tuple unordered  
B. List mutable hoti hai, Tuple immutable  
C. List immutable hoti hai, Tuple mutable  
D. Dono same hain

**Answer:** B. List mutable hoti hai, Tuple immutable

---

## Q37. Tuples ko commonly kab use karna useful hota hai?

A. Jab data ko baar-baar modify karna ho  
B. Jab data ko fixed rakhna ho  
C. Jab sirf strings store karni ho  
D. Jab sorting karni ho

**Answer:** B. Jab data ko fixed rakhna ho

---

## Q38. Kaunsa statement correct hai?

A. Tuple me indexing nahi hoti  
B. Tuple me slicing nahi hoti  
C. Tuple ordered hoti hai  
D. Tuple me duplicate values allowed nahi hain

**Answer:** C. Tuple ordered hoti hai

---

## Q39. Tuple me kitne built-in methods commonly available hote hain?

A. 2  
B. 5  
C. 10  
D. 15

**Answer:** A. 2

---

## Q40. Ye dono methods kaunse hain?

A. `append()` and `remove()`  
B. `sort()` and `reverse()`  
C. `count()` and `index()`  
D. `insert()` and `pop()`

**Answer:** C. `count()` and `index()`

---

# 🏆 SCORE

```text
36–40 → 🔥 Excellent
31–35 → 💪 Very Good
25–30 → 👍 Good
20–24 → 📚 Need More Practice
Below 20 → 🔄 Revise Tuples Again
```

---

# 🎯 DAY 06 MCQ TARGET

**Minimum Target: 30/40**

Agar score 30 se kam aaye:

```text
Revise Notes
     ↓
Practice Programs
     ↓
Attempt MCQs Again
```

> **Don't memorize the answers. Understand the concepts.**

---

# 🚀 DAY 06

**Learn → Practice → Test → Improve → Build**