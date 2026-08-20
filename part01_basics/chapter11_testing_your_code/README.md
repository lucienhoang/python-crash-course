# Chapter 11 — Testing Your Code

## Key Concepts

- When a test fails, **don't change the test**. Instead, fix the code that caused the test to fail.
- Test method names must start with `test_` so `unittest` can automatically discover and run them.
- Test class names should be related to the function or class being tested.
- Import `unittest` to use Python's built-in testing framework.
- Test classes should inherit from `unittest.TestCase`.
- Whenever possible, **one test should focus on one behavior**. This makes failures easier to understand.
- Test both **normal cases and edge cases**, not just the happy path.
- Test functions and classes differently:
  - For **functions**, test their return values.
  - For **classes**, test their methods and object attributes/behavior.
- Keep production code and test code separate. Commonly, the actual code is in one `.py` file and the tests are in another.
- A good test suite gives you confidence when modifying or extending existing code.

## Common `unittest` Tools

| Tool / Method       | Purpose                                                                           |
| ------------------- | --------------------------------------------------------------------------------- |
| `unittest.TestCase` | Base class for creating test classes                                              |
| `setUp()`           | Runs automatically before each test; useful for creating common test objects/data |
| `assertEqual()`     | Checks whether the actual result matches the expected result                      |
| `unittest.main()`   | Runs the tests when the test file is executed                                     |

## Test Output

When running a test file:

```text
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

```

## Basic Test Structure

```python
import unittest

from city_functions import city_country

class TestCityCountry(unittest.TestCase):
"""Test the city_country() function."""

    def test_city_country(self):
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile.")

unittest.main()
```

## Testing a Class with setUp()

- When multiple tests need the same object, use setUp():

```python
class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("Luci", "Hoang", 80000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 85000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 90000)

```
