# DAY 21 — PYTHON ADVANCED
# MINI PROJECT
# Student Performance Analyzer

from dataclasses import dataclass
from contextlib import contextmanager
from functools import reduce
from typing import List


# --------------------------------
# STUDENT DATACLASS
# --------------------------------

@dataclass
class Student:

    name: str
    marks: List[int]

    def total_marks(self) -> int:

        return reduce(
            lambda a, b: a + b,
            self.marks
        )

    def average_marks(self) -> float:

        return self.total_marks() / len(self.marks)

    def is_passed(self) -> bool:

        return self.average_marks() >= 40


# --------------------------------
# CONTEXT MANAGER
# --------------------------------

@contextmanager
def report_file(filename: str):

    file = open(
        filename,
        "w",
        encoding="utf-8"
    )

    try:

        yield file

    finally:

        file.close()


# --------------------------------
# STUDENT DATA
# --------------------------------

students: List[Student] = [

    Student(
        "Amir",
        [85, 90, 78, 88, 92]
    ),

    Student(
        "Rahul",
        [70, 65, 80, 75, 72]
    ),

    Student(
        "Aman",
        [35, 42, 38, 45, 40]
    ),

    Student(
        "Riya",
        [92, 95, 89, 90, 94]
    ),

    Student(
        "Neha",
        [55, 60, 58, 62, 57]
    )
]


# --------------------------------
# CALCULATE RANKING
# --------------------------------

ranked_students = sorted(
    students,
    key=lambda student: student.average_marks(),
    reverse=True
)


# --------------------------------
# DISPLAY STUDENT REPORT
# --------------------------------

print("\nSTUDENT PERFORMANCE ANALYZER")

print("-" * 40)


for rank, student in enumerate(
    ranked_students,
    start=1
):

    print(
        f"{rank}. "
        f"{student.name} | "
        f"Total: {student.total_marks()} | "
        f"Average: {student.average_marks():.2f} | "
        f"Status: "
        f"{'PASS' if student.is_passed() else 'FAIL'}"
    )


# --------------------------------
# FILTER PASSED STUDENTS
# --------------------------------

passed_students = list(
    filter(
        lambda student: student.is_passed(),
        students
    )
)


print("\nPASSED STUDENTS")

for student in passed_students:

    print(
        student.name
    )


# --------------------------------
# CALCULATE TOTAL MARKS
# --------------------------------

all_marks = [

    mark

    for student in students

    for mark in student.marks
]


grand_total = reduce(
    lambda a, b: a + b,
    all_marks
)


print(
    "\nGrand Total Marks:",
    grand_total
)


# --------------------------------
# SUBJECT-WISE AVERAGE
# --------------------------------

subject_names = [
    "Python",
    "SQL",
    "DSA",
    "Math",
    "AI"
]


print("\nSUBJECT-WISE ANALYSIS")

for subject, index in zip(
    subject_names,
    range(len(subject_names))
):

    subject_marks = [

        student.marks[index]

        for student in students
    ]

    average = sum(
        subject_marks
    ) / len(
        subject_marks
    )

    print(
        f"{subject}: {average:.2f}"
    )


# --------------------------------
# SAVE REPORT USING CONTEXT MANAGER
# --------------------------------

with report_file(
    "student_report.txt"
) as file:

    file.write(
        "STUDENT PERFORMANCE REPORT\n"
    )

    file.write(
        "-" * 40 + "\n"
    )

    for rank, student in enumerate(
        ranked_students,
        start=1
    ):

        status = (
            "PASS"
            if student.is_passed()
            else "FAIL"
        )

        file.write(
            f"{rank}. "
            f"{student.name} | "
            f"Total: {student.total_marks()} | "
            f"Average: "
            f"{student.average_marks():.2f} | "
            f"Status: {status}\n"
        )

    file.write(
        f"\nGrand Total: {grand_total}\n"
    )


print(
    "\nReport saved to student_report.txt"
)


