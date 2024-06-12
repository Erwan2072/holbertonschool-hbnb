#!/usr/bin/env python3

import os
import unittest
from api import app
from DataManager import DataManager
from models_city import City
from models_country import Country

class TestResources(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.data_manager = DataManager(city_file='test_cities.json', country_file='test_countries.json')

        # Add some initial data
        cls.data_manager.countries = [Country(code='FR', name='France'), Country(code='US', name='United States')]
        cls.data_manager._save_to_file('test_countries.json', cls.data_manager.countries)

        cls.data_manager.cities = []
        cls.data_manager._save_to_file('test_cities.json', cls.data_manager.cities)

    @classmethod
    def tearDownClass(cls):
        os.remove('test_cities.json')
        os.remove('test_countries.json')

    def test_get_all_countries(self):
        response = self.client.get('/countries')
        self.assertEqual(response.status_code, 200)
        self.assertIn({'code': 'FR', 'name': 'France'}, response.json)
        self.assertIn({'code': 'US', 'name': 'United States'}, response.json)

    def test_get_country(self):
        response = self.client.get('/countries/FR')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'code': 'FR', 'name': 'France'})

        response = self.client.get('/countries/XX')
        self.assertEqual(response.status_code, 404)

    def test_create_city(self):
        response = self.client.post('/cities', json={'name': 'Paris', 'country_code': 'FR'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'Paris')
        self.assertEqual(response.json['country_code'], 'FR')

        # Test with invalid country code
        response = self.client.post('/cities', json={'name': 'New City', 'country_code': 'XX'})
        self.assertEqual(response.status_code, 400)

    def test_get_all_cities(self):
        response = self.client.post('/cities', json={'name': 'Paris', 'country_code': 'FR'})
        response = self.client.get('/cities')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json), 0)

    def test_get_city(self):
        response = self.client.post('/cities', json={'name': 'Paris', 'country_code': 'FR'})
        city_id = response.json['id']
        response = self.client.get(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Paris')

        response = self.client.get('/cities/999')
        self.assertEqual(response.status_code, 404)

    def test_update_city(self):
        response = self.client.post('/cities', json={'name': 'Paris', 'country_code': 'FR'})
        city_id = response.json['id']

        response = self.client.put(f'/cities/{city_id}', json={'name': 'Lyon', 'country_code': 'FR'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Lyon')

        response = self.client.put(f'/cities/999', json={'name': 'Nonexistent', 'country_code': 'FR'})
        self.assertEqual(response.status_code, 404)

    def test_delete_city(self):
        response = self.client.post('/cities', json={'name': 'Paris', 'country_code': 'FR'})
        city_id = response.json['id']

        response = self.client.delete(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 204)

        response = self.client.delete(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
