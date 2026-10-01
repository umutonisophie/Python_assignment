# functions-assignment

An introductory Python exercise on writing and composing functions, using a
student report card generator as the running example.

## What it demonstrates

Breaking a small problem into single-purpose functions and then composing them:

| Function | Responsibility |
|---|---|
| `calculate_average(*marks)` | arithmetic mean of the supplied marks |
| `grade(average)` | maps an average to a letter grade |
| `student_report_dictionary(name, **marks)` | composes both into a report |
| `format_report(report)` | renders a report as an aligned text block |

The main lesson is the `__main__` guard. The first version of this script called
`input()` at module level, which meant importing the file blocked on the console
and none of the functions could be tested. Moving the interaction into `main()`
left the module free of side effects, which is what made the test suite possible.

## Validation

The functions raise `ValueError` rather than returning a misleading value:

- an average requires at least one mark
- averages and individual marks must fall in the 0-100 range
- every offending subject is reported at once, so a caller sees all errors in a
  single pass instead of fixing them one at a time

## Grade bands

| Average | Grade |
|---|---|
| 80-100 | A |
| 70-79.9 | B |
| 60-69.9 | C |
| 50-59.9 | D |
| 0-49.9 | E |

## Running

```bash
python3 report_generator.py
```

```
Enter your name: Sophie
Enter your Backend mark (0-100): 78
Enter your Frontend mark (0-100): 85
Enter your Design mark (0-100): 90

STUDENT REPORT: Sophie
----------------------------------
  Backend      78.0
  Frontend     85.0
  Design       90.0
----------------------------------
  Average      84.33
  Grade        A
```

Input is re-prompted until a valid mark in range is entered.

## Tests

```bash
python3 -m unittest discover -v
```

14 tests using only the standard library, covering the grade boundaries
(including 79.9 -> B and 80 -> A), range rejection, rounding, and the fact that
importing the module produces no output.

## Project layout

```
report_generator.py          the functions and the interactive entry point
test_report_generator.py     unittest suite
```

## Requirements

Python 3.7 or newer. No third-party dependencies.
