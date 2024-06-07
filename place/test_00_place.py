#!/usr/bin/env python3
import unittest
import json
from Api_place import app, data_store

class PlaceApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Réinitialiser le magasin de données avant chaque test
        data_store.data = {
            'cities': [{'id': 1, 'name': 'Paris'}, {'id': 2, 'name': 'Lyon'}],
            'amenities': [{'id': 1, 'name': 'WiFi'}, {'id': 2, 'name': 'Pool'}],
            'places': []
        }
        data_store.next_id = 1

    def test_get_all_places(self):
        response = self.app.get('/places')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_place(self):
        new_place = {
            'name': 'Charming Studio',
            'description': 'A charming studio in the heart of the city',
            'address': '123 Main St',
            'city_id': 1,
            'latitude': 48.8566,
            'longitude': 2.3522,
            'host_id': 'host_123',
            'number_of_rooms': 1,
            'number_of_bathrooms': 1,
            'price_per_night': 75.0,
            'max_guests': 2,
            'amenity_ids': [1, 2]
        }
        response = self.app.post('/places', data=json.dumps(new_place), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        new_place['id'] = 1  # L'ID attendu
        self.assertEqual(response.json, new_place)

    def test_get_place_by_id(self):
        new_place = {
            'name': 'Charming Studio',
            'description': 'A charming studio in the heart of the city',
            'address': '123 Main St',
            'city_id': 1,
            'latitude': 48.8566,
            'longitude': 2.3522,
            'host_id': 'host_123',
            'number_of_rooms': 1,
            'number_of_bathrooms': 1,
            'price_per_night': 75.0,
            'max_guests': 2,
            'amenity_ids': [1, 2]
        }
        place_id = data_store.add_place(new_place)
        response = self.app.get(f'/places/{place_id}')
        self.assertEqual(response.status_code, 200)
        new_place['id'] = place_id  # L'ID attendu
        self.assertEqual(response.json, new_place)

    def test_get_place_by_id_not_found(self):
        response = self.app.get('/places/999')
        self.assertEqual(response.status_code, 404)

    def test_update_place(self):
        new_place = {
            'name': 'Charming Studio',
            'description': 'A charming studio in the heart of the city',
            'address': '123 Main St',
            'city_id': 1,
            'latitude': 48.8566,
            'longitude': 2.3522,
            'host_id': 'host_123',
            'number_of_rooms': 1,
            'number_of_bathrooms': 1,
            'price_per_night': 75.0,
            'max_guests': 2,
            'amenity_ids': [1, 2]
        }
        place_id = data_store.add_place(new_place)

        updated_place = new_place.copy()
        updated_place['name'] = 'Updated Charming Studio'
        response = self.app.put(f'/places/{place_id}', data=json.dumps(updated_place), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        updated_place['id'] = place_id
        self.assertEqual(response.json, updated_place)

    def test_update_place_not_found(self):
        updated_place = {
            'name': 'Updated Charming Studio',
            'description': 'An updated charming studio in the heart of the city',
            'address': '123 Main St',
            'city_id': 1,
            'latitude': 48.8566,
            'longitude': 2.3522,
            'host_id': 'host_123',
            'number_of_rooms': 1,
            'number_of_bathrooms': 1,
            'price_per_night': 80.0,
            'max_guests': 2,
            'amenity_ids': [1, 2]
        }
        response = self.app.put('/places/999', data=json.dumps(updated_place), content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_delete_place(self):
        new_place = {
            'name': 'Charming Studio',
            'description': 'A charming studio in the heart of the city',
            'address': '123 Main St',
            'city_id': 1,
            'latitude': 48.8566,
            'longitude': 2.3522,
            'host_id': 'host_123',
            'number_of_rooms': 1,
            'number_of_bathrooms': 1,
            'price_per_night': 75.0,
            'max_guests': 2,
            'amenity_ids': [1, 2]
        }
        place_id = data_store.add_place(new_place)
        response = self.app.delete(f'/places/{place_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, new_place)

    def test_delete_place_not_found(self):
        response = self.app.delete('/places/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
