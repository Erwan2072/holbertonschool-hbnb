#!/usr/bin/env python3


import unittest
from app_amenity import app
import json

class AmenityTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.amenity_id = None

    def tearDown(self):
        pass

    def test_create_amenity(self):
        data = {'name': 'Pool'}
        response = self.app.post('/amenities', json=data)
        self.assertEqual(response.status_code, 201)
        amenity_data = json.loads(response.data)
        self.assertIn('id', amenity_data)
        self.amenity_id = amenity_data['id']

    def test_get_amenities(self):
        response = self.app.get('/amenities')
        self.assertEqual(response.status_code, 200)
        amenities_data = json.loads(response.data)
        self.assertIsInstance(amenities_data, list)

    def test_get_amenity(self):
        if self.amenity_id:
            response = self.app.get(f'/amenities/{self.amenity_id}')
            self.assertEqual(response.status_code, 200)
            amenity_data = json.loads(response.data)
            self.assertEqual(amenity_data['id'], self.amenity_id)

    def test_update_amenity(self):
        if self.amenity_id:
            data = {'name': 'New Pool'}
            response = self.app.put(f'/amenities/{self.amenity_id}', json=data)
            self.assertEqual(response.status_code, 200)
            updated_amenity_data = json.loads(response.data)
            self.assertEqual(updated_amenity_data['name'], 'New Pool')

    def test_delete_amenity(self):
        if self.amenity_id:
            response = self.app.delete(f'/amenities/{self.amenity_id}')
            self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
