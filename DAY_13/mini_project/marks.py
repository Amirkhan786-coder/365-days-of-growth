# ============================================
# Day 13 - Mini Project
# Student Information System
# File: marks.py
# ============================================

def get_marks():
    python = float(input("Enter Python marks: "))
    java = float(input("Enter Java marks: "))
    maths = float(input("Enter Maths marks: "))

    return python, java, maths


def calculate_result(python, java, maths):

    total = python + java + maths
    percentage = total / 3

    if percentage >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    return total, percentage, result