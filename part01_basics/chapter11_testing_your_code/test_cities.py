import unittest

from city_functions import city_country


class TestCityCountry(unittest.TestCase):
    """Testing city_country() function."""

    def test_city_country(self):
        name = city_country("santiago", "chile")
        self.assertEqual(name, "Santiago, Chile.")

    def test_city_country_population(self):
        name = city_country("santiago", "chile", 5000000)
        self.assertEqual(name, "Santiago, Chile - population 5000000.")


unittest.main()

# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK
