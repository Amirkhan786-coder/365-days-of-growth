# ============================================================
# 🚀 DAY 17 / 365 — PYTHON ITERATORS & GENERATORS
# PRACTICE CODES
# ============================================================


# ============================================================
# 1. BASIC ITERATOR
# ============================================================

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

print("Basic Iterator:")

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# ============================================================
# 2. STRING ITERATOR
# ============================================================

name = "PYTHON"

iterator = iter(name)

print("\nString Iterator:")

for character in iterator:
    print(character)


# ============================================================
# 3. RANGE ITERATOR
# ============================================================

iterator = iter(range(1, 6))

print("\nRange Iterator:")

for number in iterator:
    print(number)


# ============================================================
# 4. STOPITERATION HANDLING
# ============================================================

numbers = [10, 20, 30]

iterator = iter(numbers)

print("\nStopIteration Example:")

try:

    while True:

        print(next(iterator))

except StopIteration:

    print("Iteration completed.")


# ============================================================
# 5. CUSTOM ITERATOR — COUNTING
# ============================================================

class Counter:

    def __init__(self, limit):

        self.current = 1
        self.limit = limit

    def __iter__(self):

        return self

    def __next__(self):

        if self.current <= self.limit:

            value = self.current

            self.current += 1

            return value

        raise StopIteration


print("\nCustom Counter:")

counter = Counter(5)

for number in counter:

    print(number)


# ============================================================
# 6. CUSTOM ITERATOR — EVEN NUMBERS
# ============================================================

class EvenNumbers:

    def __init__(self, limit):

        self.current = 2
        self.limit = limit

    def __iter__(self):

        return self

    def __next__(self):

        if self.current <= self.limit:

            value = self.current

            self.current += 2

            return value

        raise StopIteration


print("\nCustom Even Number Iterator:")

even_numbers = EvenNumbers(10)

for number in even_numbers:

    print(number)


# ============================================================
# 7. CUSTOM ITERATOR — COUNTDOWN
# ============================================================

class Countdown:

    def __init__(self, start):

        self.current = start

    def __iter__(self):

        return self

    def __next__(self):

        if self.current >= 1:

            value = self.current

            self.current -= 1

            return value

        raise StopIteration


print("\nCountdown Iterator:")

countdown = Countdown(5)

for number in countdown:

    print(number)


# ============================================================
# 8. SIMPLE GENERATOR
# ============================================================

def simple_generator():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


print("\nSimple Generator:")

for number in simple_generator():

    print(number)


# ============================================================
# 9. GENERATOR — NUMBERS
# ============================================================

def generate_numbers(limit):

    for number in range(1, limit + 1):

        yield number


print("\nNumber Generator:")

for number in generate_numbers(5):

    print(number)


# ============================================================
# 10. GENERATOR — EVEN NUMBERS
# ============================================================

def generate_even_numbers(limit):

    for number in range(2, limit + 1, 2):

        yield number


print("\nEven Number Generator:")

for number in generate_even_numbers(20):

    print(number)


# ============================================================
# 11. GENERATOR — ODD NUMBERS
# ============================================================

def generate_odd_numbers(limit):

    for number in range(1, limit + 1, 2):

        yield number


print("\nOdd Number Generator:")

for number in generate_odd_numbers(20):

    print(number)


# ============================================================
# 12. GENERATOR — SQUARES
# ============================================================

def generate_squares(limit):

    for number in range(1, limit + 1):

        yield number * number


print("\nSquare Generator:")

for square in generate_squares(10):

    print(square)


# ============================================================
# 13. GENERATOR — CUBES
# ============================================================

def generate_cubes(limit):

    for number in range(1, limit + 1):

        yield number ** 3


print("\nCube Generator:")

for cube in generate_cubes(5):

    print(cube)


# ============================================================
# 14. GENERATOR — MULTIPLICATION TABLE
# ============================================================

def multiplication_table(number):

    for i in range(1, 11):

        yield f"{number} x {i} = {number * i}"


print("\nMultiplication Table:")

for result in multiplication_table(5):

    print(result)


# ============================================================
# 15. FIBONACCI GENERATOR
# ============================================================

def fibonacci(count):

    first = 0
    second = 1

    for _ in range(count):

        yield first

        first, second = second, first + second


print("\nFibonacci Generator:")

for number in fibonacci(10):

    print(number)


# ============================================================
# 16. PRIME NUMBER GENERATOR
# ============================================================

def is_prime(number):

    if number < 2:

        return False

    for i in range(2, int(number ** 0.5) + 1):

        if number % i == 0:

            return False

    return True


def prime_numbers(limit):

    for number in range(2, limit + 1):

        if is_prime(number):

            yield number


print("\nPrime Number Generator:")

for number in prime_numbers(50):

    print(number)


# ============================================================
# 17. DIVISIBLE BY 5 GENERATOR
# ============================================================

def divisible_by_five(limit):

    for number in range(1, limit + 1):

        if number % 5 == 0:

            yield number


print("\nNumbers Divisible by 5:")

for number in divisible_by_five(50):

    print(number)


# ============================================================
# 18. LIST FILTER GENERATOR
# ============================================================

def positive_numbers(numbers):

    for number in numbers:

        if number > 0:

            yield number


numbers = [-5, 10, -3, 20, 30, -7]

print("\nPositive Numbers:")

for number in positive_numbers(numbers):

    print(number)


# ============================================================
# 19. EVEN NUMBERS FROM LIST
# ============================================================

def even_from_list(numbers):

    for number in numbers:

        if number % 2 == 0:

            yield number


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print("\nEven Numbers From List:")

for number in even_from_list(numbers):

    print(number)


# ============================================================
# 20. WORD FILTER GENERATOR
# ============================================================

def long_words(words):

    for word in words:

        if len(word) > 5:

            yield word


words = [
    "Python",
    "AI",
    "Programming",
    "Code",
    "MachineLearning"
]

print("\nLong Words:")

for word in long_words(words):

    print(word)


# ============================================================
# 21. NUMBERS GREATER THAN 50
# ============================================================

def greater_than_50(numbers):

    for number in numbers:

        if number > 50:

            yield number


numbers = [10, 60, 20, 80, 30, 100]

print("\nNumbers Greater Than 50:")

for number in greater_than_50(numbers):

    print(number)


# ============================================================
# 22. REVERSE STRING GENERATOR
# ============================================================

def reverse_string(text):

    for character in reversed(text):

        yield character


print("\nReverse String:")

for character in reverse_string("PYTHON"):

    print(character)


# ============================================================
# 23. GENERATOR EXPRESSION — SQUARES
# ============================================================

squares = (
    number * number
    for number in range(1, 11)
)

print("\nGenerator Expression - Squares:")

for square in squares:

    print(square)


# ============================================================
# 24. GENERATOR EXPRESSION — EVEN NUMBERS
# ============================================================

even_numbers = (
    number
    for number in range(1, 21)
    if number % 2 == 0
)

print("\nGenerator Expression - Even Numbers:")

for number in even_numbers:

    print(number)


# ============================================================
# 25. LAZY EVALUATION
# ============================================================

def lazy_numbers():

    for number in range(1, 6):

        print("Generating:", number)

        yield number


print("\nLazy Evaluation:")

generator = lazy_numbers()

print(next(generator))
print(next(generator))
print(next(generator))


# ============================================================
# 26. INFINITE NUMBER GENERATOR
# ============================================================

def infinite_numbers():

    number = 1

    while True:

        yield number

        number += 1


print("\nInfinite Generator:")

generator = infinite_numbers()

for _ in range(5):

    print(next(generator))


# ============================================================
# 27. INFINITE EVEN NUMBER GENERATOR
# ============================================================

def infinite_even_numbers():

    number = 2

    while True:

        yield number

        number += 2


print("\nInfinite Even Generator:")

generator = infinite_even_numbers()

for _ in range(5):

    print(next(generator))


# ============================================================
# 28. RUNNING TOTAL GENERATOR
# ============================================================

def running_total(numbers):

    total = 0

    for number in numbers:

        total += number

        yield total


numbers = [10, 20, 30, 40]

print("\nRunning Total:")

for total in running_total(numbers):

    print(total)


# ============================================================
# 29. NUMBER PROCESSING GENERATOR
# ============================================================

def even_numbers_from_list(numbers):

    for number in numbers:

        if number % 2 == 0:

            yield number


def square_numbers(numbers):

    for number in numbers:

        yield number * number


def greater_than_50_filter(numbers):

    for number in numbers:

        if number > 50:

            yield number


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]

even_numbers = even_numbers_from_list(numbers)

squares = square_numbers(even_numbers)

final_result = greater_than_50_filter(squares)

print("\nGenerator Pipeline:")

for number in final_result:

    print(number)


# ============================================================
# 30. FINAL CHALLENGE
# ============================================================

def process_numbers(numbers):

    for number in numbers:

        if number % 2 == 0:

            square = number ** 2

            if square > 50:

                yield square


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]

print("\nFinal Challenge Result:")

for number in process_numbers(numbers):

    print(number)


# ============================================================
# 🎯 DAY 17 PRACTICE COMPLETED
# ============================================================

print("\n" + "=" * 60)

print("DAY 17 PRACTICE COMPLETED 🚀")

print("=" * 60)