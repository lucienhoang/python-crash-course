import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test default and custom salary annual raise."""

    def setUp(self):
        self.my_employee = Employee("luci", "hoang", 80000)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 85000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.annual_salary, 90000)


unittest.main()

# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
