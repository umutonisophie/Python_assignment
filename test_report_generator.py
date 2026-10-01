"""Tests for the student report generator.

Run with:  python -m unittest discover -v
"""

import unittest

from report_generator import (
    calculate_average,
    format_report,
    grade,
    student_report_dictionary,
)


class TestCalculateAverage(unittest.TestCase):
    def test_averages_three_marks(self):
        self.assertEqual(calculate_average(78, 85, 90), 84.33333333333333)

    def test_average_of_one_mark_is_that_mark(self):
        self.assertEqual(calculate_average(70), 70)

    def test_accepts_floats(self):
        self.assertAlmostEqual(calculate_average(70.5, 80.5), 75.5)

    def test_negative_marks_are_arithmetically_valid(self):
        self.assertEqual(calculate_average(-10, 10), 0)

    def test_requires_at_least_one_mark(self):
        with self.assertRaises(ValueError):
            calculate_average()


class TestGrade(unittest.TestCase):
    def test_grade_boundaries(self):
        cases = {
            100: "A", 80: "A", 79.9: "B",
            70: "B", 69.9: "C",
            60: "C", 59.9: "D",
            50: "D", 49.9: "E",
            0: "E",
        }
        for average, expected in cases.items():
            with self.subTest(average=average):
                self.assertEqual(grade(average), expected)

    def test_rejects_average_above_range(self):
        with self.assertRaises(ValueError):
            grade(101)

    def test_rejects_negative_average(self):
        with self.assertRaises(ValueError):
            grade(-1)


class TestStudentReportDictionary(unittest.TestCase):
    def test_builds_a_complete_report(self):
        report = student_report_dictionary(
            "Sophie", Backend=78, Frontend=85, Design=90
        )
        self.assertEqual(report["name"], "Sophie")
        self.assertEqual(report["Backend"], 78)
        self.assertEqual(report["Frontend"], 85)
        self.assertEqual(report["Design"], 90)
        self.assertEqual(report["average"], 84.33)
        self.assertEqual(report["grade"], "A")  # 84.33 clears the 80 threshold

    def test_rounds_average_to_two_places(self):
        report = student_report_dictionary("A", Backend=1, Frontend=2, Design=2)
        self.assertEqual(report["average"], 1.67)

    def test_rejects_out_of_range_mark(self):
        with self.assertRaises(ValueError):
            student_report_dictionary("A", Backend=120)

    def test_requires_at_least_one_subject(self):
        with self.assertRaises(ValueError):
            student_report_dictionary("A")

    def test_reports_all_offending_subjects_at_once(self):
        with self.assertRaises(ValueError) as ctx:
            student_report_dictionary("A", Backend=120, Frontend=-5, Design=50)
        self.assertIn("Backend", str(ctx.exception))
        self.assertIn("Frontend", str(ctx.exception))


class TestFormatReport(unittest.TestCase):
    def test_contains_name_marks_average_and_grade(self):
        report = student_report_dictionary("A", Backend=78, Frontend=85, Design=90)
        rendered = format_report(report)
        self.assertIn("A", rendered)
        self.assertIn("78", rendered)
        self.assertIn("84.33", rendered)
        self.assertIn("B", rendered)


if __name__ == "__main__":
    unittest.main()
