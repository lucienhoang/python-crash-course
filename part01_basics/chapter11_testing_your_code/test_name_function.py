import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Test for 'name_functions.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")


unittest.main()

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
