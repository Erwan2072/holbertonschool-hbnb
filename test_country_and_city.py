#!/usr/bin/env python3
"""
test the classe country_and_city.py
"""


import unittest
from country_and_city import Country_city

class TestCountryCity(unittest.TestCase):
    def test_valid_country_city(self):
        test_city = Country_city("France", "Paris")
        self.assertEqual(test_city._Country_city__country, "France")
        self.assertEqual(test_city._Country_city__city, "Paris")

    def test_invalid_country(self):
        with self.assertRaises(ValueError):
            Country_city("Germany", "Berlin")

    def test_invalid_city(self):
        with self.assertRaises(ValueError):
            Country_city("France", "Marseille2")

    def test_non_string_country(self):
        with self.assertRaises(TypeError):
            Country_city(123, "London")

    def test_non_string_city(self):
        with self.assertRaises(TypeError):
            Country_city("Spain", 456)

if __name__ == '__main__':
    unittest.main()
