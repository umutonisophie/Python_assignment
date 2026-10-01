"""
Student report card generator.

An introductory Python exercise on writing and composing functions: a function
that averages three subject marks, a function that maps an average to a letter
grade, and a function that composes both into a report dictionary.

The interactive input is isolated behind a ``main()`` guard so that importing
this module has no side effects, which is what makes the functions testable.
"""

from typing import Dict, List, Union

Number = Union[int, float]

#: Marks are conventionally graded on a 0-100 scale.
MAX_MARK = 100

#: Minimum average required for each letter grade, highest first.
GRADE_BANDS: List[tuple] = [
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0, "E"),
]

SUBJECTS = ("Backend", "Frontend", "Design")


def calculate_average(*marks: Number) -> float:
    """Return the arithmetic mean of the supplied marks.

    Args:
        *marks: One or more numeric marks.

    Returns:
        The mean of the marks as a float.

    Raises:
        ValueError: If no marks are supplied.
    """
    if not marks:
        raise ValueError("at least one mark is required to calculate an average")
    return sum(marks) / len(marks)


def grade(average: float) -> str:
    """Map an average to a letter grade.

    Args:
        average: The mean mark to grade.

    Returns:
        One of ``"A"``, ``"B"``, ``"C"``, ``"D"`` or ``"E"``.

    Raises:
        ValueError: If the average falls outside the 0-100 range.
    """
    if not 0 <= average <= MAX_MARK:
        raise ValueError(f"average must be between 0 and {MAX_MARK}, got {average}")
    for threshold, letter in GRADE_BANDS:
        if average >= threshold:
            return letter
    return "E"  # unreachable while the range check above holds


def student_report_dictionary(name: str, **marks: Number) -> Dict[str, object]:
    """Build a report dictionary for a student.

    Args:
        name: The student's name.
        **marks: Subject names mapped to numeric marks, for example
            ``Backend=78, Frontend=85, Design=90``.

    Returns:
        A dictionary with the student's name, each subject mark, the rounded
        average and the letter grade.

    Raises:
        ValueError: If no subject marks are supplied, or a mark is out of range.
    """
    if not marks:
        raise ValueError("at least one subject mark is required")

    invalid = {k: v for k, v in marks.items() if not 0 <= v <= MAX_MARK}
    if invalid:
        raise ValueError(f"marks must be between 0 and {MAX_MARK}: {invalid}")

    average = calculate_average(*marks.values())
    return {
        "name": name,
        **marks,
        "average": round(average, 2),
        "grade": grade(average),
    }


def format_report(report: Dict[str, object]) -> str:
    """Render a report dictionary as an aligned, human-readable block."""
    lines = [f"STUDENT REPORT: {report['name']}", "-" * 34]
    for key, value in report.items():
        if key in ("name", "average", "grade"):
            continue
        lines.append(f"  {key:<12} {value}")
    lines.append("-" * 34)
    lines.append(f"  {'Average':<12} {report['average']}")
    lines.append(f"  {'Grade':<12} {report['grade']}")
    return "\n".join(lines)


def main() -> None:
    """Prompt for a name and three subject marks, then print the report."""
    name = input("Enter your name: ").strip() or "Anonymous"

    collected = {}
    for subject in SUBJECTS:
        while True:
            raw = input(f"Enter your {subject} mark (0-{MAX_MARK}): ").strip()
            try:
                mark = float(raw)
            except ValueError:
                print("  please enter a number")
                continue
            if not 0 <= mark <= MAX_MARK:
                print(f"  marks must be between 0 and {MAX_MARK}")
                continue
            collected[subject] = mark
            break

    print()
    print(format_report(student_report_dictionary(name, **collected)))


if __name__ == "__main__":
    main()
