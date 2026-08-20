import unittest

from city_functions import city_country


class TestCityCountry(unittest.TestCase):
    """Testing city_country() function."""

    def test_city_country(self):
        name = city_country("santiago", "chile")
        self.assertEqual(name, "Santiago, Chile.")


unittest.main()

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# # OK
