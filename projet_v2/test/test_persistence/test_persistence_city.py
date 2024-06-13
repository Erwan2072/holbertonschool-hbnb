#!/usr/bin/python3
import unittest
from unittest.mock import MagicMock
import sys
import os


# Ajouter le répertoire racine du projet au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from model.city import City
from persistence.city_repository import CityRepository
import uuid
from datetime import datetime


class TestCityRepository(unittest.TestCase):

    def setUp(self):
        self.repo = CityRepository()
        self.city = City(name="Paris", country_id="FR")

    def test_save(self):
        # Test saving a new city
        self.repo.save(self.city)
        self.assertIn(self.city.city_id, self.repo.cities)
        self.assertEqual(self.repo.cities[self.city.city_id], self.city)

        # Test saving an object that is not an instance of City
        with self.assertRaises(ValueError):
            self.repo.save("not_a_city")

    def test_get(self):
        # Test getting a city
        self.repo.save(self.city)
        fetched_city = self.repo.get(self.city.city_id)
        self.assertEqual(fetched_city, self.city)

        # Test getting a non-existent city
        self.assertIsNone(self.repo.get("non_existent_id"))

    def test_get_all(self):
        # Test getting all cities
        self.repo.save(self.city)
        all_cities = self.repo.get_all()
        self.assertEqual(len(all_cities), 1)
        self.assertEqual(all_cities[0], self.city)

    def test_update(self):
        # Mock the update_from_dict method in the City class
        self.city.update_from_dict = MagicMock()

        # Test updating an existing city
        self.repo.save(self.city)
        new_data = {"name": "Updated Paris"}
        result = self.repo.update(self.city.city_id, new_data)
        self.city.update_from_dict.assert_called_once_with(new_data)
        self.assertTrue(result)

        # Test updating a non-existent city
        result = self.repo.update("non_existent_id", new_data)
        self.assertFalse(result)

    def test_delete(self):
        # Test deleting an existing city
        self.repo.save(self.city)
        result = self.repo.delete(self.city.city_id)
        self.assertNotIn(self.city.city_id, self.repo.cities)
        self.assertTrue(result)

        # Test deleting a non-existent city
        result = self.repo.delete("non_existent_id")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
