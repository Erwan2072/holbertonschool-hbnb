#!/usr/bin/python3
import unittest
from unittest.mock import MagicMock
import sys
import os

# Ajouter le répertoire racine du projet au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from model.country import Country
from persistence.country_repository import CountryRepository
import uuid
from datetime import datetime

class TestCountryRepository(unittest.TestCase):

    def setUp(self):
        self.repo = CountryRepository()
        self.country = Country(name="France")

    def test_save(self):
        # Test saving a new country
        self.repo.save(self.country)
        self.assertIn(self.country.country_id, self.repo.countries)
        self.assertEqual(self.repo.countries[self.country.country_id], self.country)

        # Test saving an object that is not an instance of Country
        with self.assertRaises(ValueError):
            self.repo.save("not_a_country")

    def test_get(self):
        # Test getting a country
        self.repo.save(self.country)
        fetched_country = self.repo.get(self.country.country_id)
        self.assertEqual(fetched_country, self.country)

        # Test getting a non-existent country
        self.assertIsNone(self.repo.get("non_existent_id"))

    def test_get_all(self):
        # Test getting all countries
        self.repo.save(self.country)
        all_countries = self.repo.get_all()
        self.assertEqual(len(all_countries), 1)
        self.assertEqual(all_countries[0], self.country)

    def test_update(self):
        # Mock the update_from_dict method in the Country class
        self.country.update_from_dict = MagicMock()

        # Test updating an existing country
        self.repo.save(self.country)
        new_data = {"name": "Updated France"}
        result = self.repo.update(self.country.country_id, new_data)
        self.country.update_from_dict.assert_called_once_with(new_data)
        self.assertTrue(result)

        # Test updating a non-existent country
        result = self.repo.update("non_existent_id", new_data)
        self.assertFalse(result)

    def test_delete(self):
        # Test deleting an existing country
        self.repo.save(self.country)
        result = self.repo.delete(self.country.country_id)
        self.assertNotIn(self.country.country_id, self.repo.countries)
        self.assertTrue(result)

        # Test deleting a non-existent country
        result = self.repo.delete("non_existent_id")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
