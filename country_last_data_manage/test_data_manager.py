#!/usr/bin/env python3

import os
import unittest
from datetime import datetime
from DataManager import DataManager
from models_city import City
from models_country import Country

class TestDataManager(unittest.TestCase):

    def setUp(self):
        # Initialize the DataManager with test files
        self.data_manager = DataManager(city_file='test_cities.json', country_file='test_countries.json')
        self.data_manager.cities = []
        self.data_manager.countries = []
        self.data_manager._save_to_file('test_cities.json', self.data_manager.cities)
        self.data_manager._save_to_file('test_countries.json', self.data_manager.countries)

    def tearDown(self):
        # Clean up test files
        os.remove('test_cities.json')
        os.remove('test_countries.json')

    def test_save_city(self):
        city = City(name='Paris', country_code='FR')
        self.data_manager.save(city)
        self.assertIn(city, self.data_manager.cities)

    def test_save_country(self):
        country = Country(code='FR', name='France')
        self.data_manager.save(country)
        self.assertIn(country, self.data_manager.countries)

    def test_get_city(self):
        city = City(name='Paris', country_code='FR')
        self.data_manager.save(city)
        retrieved_city = self.data_manager.get(city.id, 'city')
        self.assertEqual(retrieved_city.name, 'Paris')
        self.assertEqual(retrieved_city.country_code, 'FR')

    def test_get_country(self):
        country = Country(code='FR', name='France')
        self.data_manager.save(country)
        retrieved_country = self.data_manager.get(country.code, 'country')
        self.assertEqual(retrieved_country.name, 'France')
        self.assertEqual(retrieved_country.code, 'FR')

    def test_update_city(self):
        city = City(name='Paris', country_code='FR')
        self.data_manager.save(city)
        city.name = 'Lyon'
        self.data_manager.update(city)
        updated_city = self.data_manager.get(city.id, 'city')
        self.assertEqual(updated_city.name, 'Lyon')

    def test_update_country(self):
        country = Country(code='FR', name='France')
        self.data_manager.save(country)
        country.name = 'Republic of France'
        self.data_manager.update(country)
        updated_country = self.data_manager.get(country.code, 'country')
        self.assertEqual(updated_country.name, 'Republic of France')

    def test_delete_city(self):
        city = City(name='Paris', country_code='FR')
        self.data_manager.save(city)
        self.data_manager.delete(city.id, 'city')
        deleted_city = self.data_manager.get(city.id, 'city')
        self.assertIsNone(deleted_city)

    def test_delete_country(self):
        country = Country(code='FR', name='France')
        self.data_manager.save(country)
        self.data_manager.delete(country.code, 'country')
        deleted_country = self.data_manager.get(country.code, 'country')
        self.assertIsNone(deleted_country)

if __name__ == '__main__':
    unittest.main()
