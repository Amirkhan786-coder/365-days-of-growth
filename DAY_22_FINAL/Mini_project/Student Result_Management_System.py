from dataclasses import dataclass
from functools import reduce
from contextlib import contextmanager


# ============================================================
# CUSTOM EXCEPTION
# ============================================================

class InvalidMarksError(Exception):
    """Raised when marks are outside the valid range."""

    pass


# ============================================================
# STUDENT DATACLASS
# ============================================================

@dataclass
class Student:
    name: str
    marks: list[int]

    def total_marks(self) -> int:
        """Return total marks."""

        return reduce(
            lambda first, second: first + second,
            self.marks
        )

    def average_marks(self) -> float:
        """Return average marks."""

        return self.total_marks() / len(self.marks)

    def grade(self) -> str:
        """Return grade based on average marks."""

        average = self.average_marks()

        if average >= 90:
            return "A+"

        if average >= 80:
            return "A"

        if average >= 70:
            return "B"

        if average >= 60:
            return "C"

        if average >= 50:
            return "D"

        return "F"

    def status(self) -> str:
        """Return PASS or FAIL."""

        if self.average_marks() >= 40:
            return "PASS"

        return "FAIL"


# ============================================================
# MARKS VALIDATION
# ============================================================

def validate_marks(marks: list[int]) -> None:
    """Validate all student marks."""

    for mark in marks:

        if not 0 <= mark <= 100:

            raise InvalidMarksError(
                f"Invalid mark: {mark}. "
                "Marks must be between 0 and 100."
            )


# ============================================================
# CUSTOM CONTEXT MANAGER
# ============================================================

@contextmanager
def report_file(filename: str):

    file = None

    try:

        file = open(
            filename,
            "w",
            encoding="utf-8"
        )

        print(
            f"Creating report: {filename}"
        )

        yield file

    finally:

        if file is not None:

            file.close()

            print(
                "Report file closed."
            )


# ============================================================
# DISPLAY STUDENT RESULT
# ============================================================

def display_student(
    rank: int,
    student: Student
) -> None:

    print(
        f"{rank}. "
        f"{student.name} | "
        f"Total: {student.total_marks()} | "
        f"Average: {student.average_marks():.2f} | "
        f"Grade: {student.grade()} | "
        f"Status: {student.status()}"
    )


# ============================================================
# GENERATE REPORT
# ============================================================

def generate_report(
    students: list[Student],
    filename: str
) -> None:

    ranked_students = sorted(
        students,
        key=lambda student: student.average_marks(),
        reverse=True
    )

    with report_file(filename) as file:

        file.write(
            "STUDENT RESULT MANAGEMENT SYSTEM\n"
        )

        file.write(
            "=" * 45 + "\n\n"
        )

        for rank, student in enumerate(
            ranked_students,
            start=1
        ):

            file.write(
                f"{rank}. {student.name}\n"
            )

            file.write(
                f"   Marks: {student.marks}\n"
            )

            file.write(
                f"   Total: "
                f"{student.total_marks()}\n"
            )

            file.write(
                f"   Average: "
                f"{student.average_marks():.2f}\n"
            )

            file.write(
                f"   Grade: "
                f"{student.grade()}\n"
            )

            file.write(
                f"   Status: "
                f"{student.status()}\n\n"
            )

        passed_students = list(
            filter(
                lambda student:
                student.status() == "PASS",
                students
            )
        )

        file.write(
            "PASSED STUDENTS\n"
        )

        file.write(
            "-" * 20 + "\n"
        )

        for student in passed_students:

            file.write(
                f"{student.name}\n"
            )

        file.write("\n")

        total_marks = reduce(
            lambda first, second:
            first + second,
            [
                student.total_marks()
                for student in students
            ]
        )

        file.write(
            f"Grand Total: {total_marks}\n"
        )

    print(
        f"\nReport saved successfully to {filename}"
    )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main() -> None:

    students = [
        Student(
            "Amir",
            [90, 85, 88, 92, 95]
        ),
        Student(
            "Rahul",
            [78, 82, 75, 80, 77]
        ),
        Student(
            "Aman",
            [35, 42, 38, 40, 36]
        ),
        Student(
            "Riya",
            [95, 96, 92, 94, 98]
        )
    ]

    try:

        # Validate all marks
        for student in students:

            validate_marks(
                student.marks
            )

        # Rank students
        ranked_students = sorted(
            students,
            key=lambda student:
            student.average_marks(),
            reverse=True
        )

        print()
        print(
            "STUDENT RESULT MANAGEMENT SYSTEM"
        )

        print(
            "=" * 45
        )

        # Display rankings
        for rank, student in enumerate(
            ranked_students,
            start=1
        ):

            display_student(
                rank,
                student
            )

        # Passed students
        passed_students = list(
            filter(
                lambda student:
                student.status() == "PASS",
                students
            )
        )

        print()
        print("PASSED STUDENTS")
        print("-" * 20)

        for student in passed_students:

            print(
                student.name
            )

        # Generate report
        generate_report(
            students,
            "student_result_report.txt"
        )

    except InvalidMarksError as error:

        print(
            "Validation Error:",
            error
        )

    except ZeroDivisionError:

        print(
            "Error: Student marks cannot be empty."
        )

    except Exception as error:

        print(
            "Unexpected Error:",
            error
        )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()