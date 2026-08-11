# ============================================================
# 🚀 DAY 17 / 365 — MINI PROJECT
# SMART DATA PROCESSOR USING ITERATORS & GENERATORS
# ============================================================

"""
This mini project demonstrates:

1. Iterators
2. Generators
3. iter()
4. next()
5. yield
6. Generator Expressions
7. Lazy Evaluation
8. Data Filtering
9. Data Transformation
10. Generator Pipeline
"""

# ============================================================
# SAMPLE DATA
# ============================================================

numbers = [
    12, 5, 28, 7, 44,
    19, 60, 3, 72, 15,
    90, 21, 36, 8, 55
]


# ============================================================
# 1. ITERATOR
# ============================================================

def create_iterator(data):
    """
    Converts a list into an iterator.
    """

    return iter(data)


# ============================================================
# 2. EVEN NUMBER GENERATOR
# ============================================================

def even_numbers(data):
    """
    Generates only even numbers.
    """

    for number in data:

        if number % 2 == 0:

            yield number


# ============================================================
# 3. SQUARE GENERATOR
# ============================================================

def square_numbers(data):
    """
    Generates the square of every number.
    """

    for number in data:

        yield number ** 2


# ============================================================
# 4. FILTER GREATER THAN 100
# ============================================================

def greater_than_100(data):
    """
    Generates only values greater than 100.
    """

    for number in data:

        if number > 100:

            yield number


# ============================================================
# 5. RUNNING TOTAL GENERATOR
# ============================================================

def running_total(data):
    """
    Generates running totals.
    """

    total = 0

    for number in data:

        total += number

        yield total


# ============================================================
# 6. DISPLAY ITERATOR DATA
# ============================================================

def display_iterator(data):

    iterator = create_iterator(data)

    print("\n--- ITERATOR OUTPUT ---")

    while True:

        try:

            value = next(iterator)

            print(value)

        except StopIteration:

            break


# ============================================================
# 7. DISPLAY EVEN NUMBERS
# ============================================================

def display_even_numbers(data):

    print("\n--- EVEN NUMBERS ---")

    for number in even_numbers(data):

        print(number)


# ============================================================
# 8. DISPLAY SQUARES
# ============================================================

def display_squares(data):

    print("\n--- SQUARES ---")

    for number in square_numbers(data):

        print(number)


# ============================================================
# 9. DISPLAY VALUES GREATER THAN 100
# ============================================================

def display_greater_than_100(data):

    print("\n--- VALUES GREATER THAN 100 ---")

    for number in greater_than_100(data):

        print(number)


# ============================================================
# 10. GENERATOR PIPELINE
# ============================================================

def process_data(data):

    """
    Generator pipeline:

    Input
      ↓
    Even Numbers
      ↓
    Square
      ↓
    Greater Than 100
      ↓
    Final Output
    """

    even = even_numbers(data)

    squared = square_numbers(even)

    filtered = greater_than_100(squared)

    for value in filtered:

        yield value


# ============================================================
# 11. RUNNING TOTAL
# ============================================================

def display_running_total(data):

    print("\n--- RUNNING TOTAL ---")

    for total in running_total(data):

        print(total)


# ============================================================
# 12. GENERATOR EXPRESSION
# ============================================================

def display_generator_expression(data):

    print("\n--- GENERATOR EXPRESSION ---")

    generator = (
        number * 2
        for number in data
        if number % 2 == 0
    )

    for value in generator:

        print(value)


# ============================================================
# 13. FINAL PROCESSING
# ============================================================

def final_processing(data):

    print("\n--- FINAL GENERATOR PIPELINE ---")

    result = process_data(data)

    for value in result:

        print(value)


# ============================================================
# 14. PROJECT SUMMARY
# ============================================================

def show_summary(data):

    print("\n" + "=" * 60)

    print("PROJECT SUMMARY")

    print("=" * 60)

    print("Total Numbers:", len(data))

    print("Minimum Value:", min(data))

    print("Maximum Value:", max(data))

    print("Total Sum:", sum(data))

    print("=" * 60)


# ============================================================
# 15. MAIN PROGRAM
# ============================================================

print("=" * 60)

print("      SMART DATA PROCESSOR")

print("   ITERATORS & GENERATORS")

print("=" * 60)


print("\nOriginal Data:")

print(numbers)


# ============================================================
# ITERATOR DEMONSTRATION
# ============================================================

display_iterator(numbers)


# ============================================================
# GENERATOR DEMONSTRATION
# ============================================================

display_even_numbers(numbers)


# ============================================================
# SQUARE GENERATOR
# ============================================================

display_squares(numbers)


# ============================================================
# FILTERING
# ============================================================

display_greater_than_100(numbers)


# ============================================================
# RUNNING TOTAL
# ============================================================

display_running_total(numbers)


# ============================================================
# GENERATOR EXPRESSION
# ============================================================

display_generator_expression(numbers)


# ============================================================
# GENERATOR PIPELINE
# ============================================================

final_processing(numbers)


# ============================================================
# PROJECT SUMMARY
# ============================================================

show_summary(numbers)


# ============================================================
# COMPLETION MESSAGE
# ============================================================

print("\n" + "=" * 60)

print("🎉 MINI PROJECT COMPLETED SUCCESSFULLY!")

print("=" * 60)

print("\nConcepts Used:")

print("✓ Iterators")
print("✓ iter()")
print("✓ next()")
print("✓ StopIteration")
print("✓ Generators")
print("✓ yield")
print("✓ Generator Expressions")
print("✓ Lazy Evaluation")
print("✓ Data Filtering")
print("✓ Data Transformation")
print("✓ Generator Pipeline")

print("\n🚀 Day 17 — Keep Growing!")