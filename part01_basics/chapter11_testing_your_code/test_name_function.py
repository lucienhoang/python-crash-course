import unittest

from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Test for 'name_functions.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")


unittest.main()

# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK
