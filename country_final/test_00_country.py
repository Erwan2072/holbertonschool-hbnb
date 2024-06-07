#!/usr/bin/env python3
"""
test the classe country_and_city.py
"""


import json
import unittest
from resources_city import CityList, City
from resources_country import Countries, Country, CitiesByCountry
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_countries(self):
        response = self.app.get('/countries')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data) > 0)

    def test_get_country_by_code(self):
        response = self.app.get('/countries/FR')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "France")

    def test_get_country_by_invalid_code(self):
        response = self.app.get('/countries/ZZ')
        data = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["error"], "Country not found")

    def test_get_cities_by_country(self):
        response = self.app.get('/countries/FR/cities')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data) >= 0)

    def test_manage_cities_GET(self):
        response = self.app.get('/cities')
        self.assertEqual(response.status_code, 200)

    def test_manage_cities_POST(self):
        new_city = {"name": "Paris", "country_code": "FR"}
        response = self.app.post('/cities', json=new_city)
        self.assertEqual(response.status_code, 201)

    def test_manage_city_GET(self):
        response = self.app.get('/cities/1')
        self.assertEqual(response.status_code, 200)

    def test_manage_city_PUT(self):
        updated_city = {"name": "New York", "country_code": "US"}
        response = self.app.put('/cities/1', json=updated_city)
        self.assertEqual(response.status_code, 200)

    def test_manage_city_DELETE(self):
        response = self.app.delete('/cities/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
