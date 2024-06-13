#!/usr/bin/python3

import unittest
from unittest.mock import MagicMock
from data_manager import DataManager
from model.place import Place
from model.user import User
from model.review import Review
from model.amenity import Amenity
from model.country import Country
from model.city import City


class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

        # Mocking repositories
        self.data_manager.place_repository = MagicMock()
        self.data_manager.user_repository = MagicMock()
        self.data_manager.review_repository = MagicMock()
        self.data_manager.amenity_repository = MagicMock()
        self.data_manager.country_repository = MagicMock()
        self.data_manager.city_repository = MagicMock()

    def test_save_place(self):
        place_data = {'name': 'Test Place', 'description': 'A place for testing'}
        place_id = 'place_123'
        self.data_manager.place_repository.save.return_value = place_id

        result = self.data_manager.save_place(place_data)

        self.data_manager.place_repository.save.assert_called_once()
        self.assertEqual(result, place_id)

    def test_get_place(self):
        place_id = 'place_123'
        place = Place(place_id=place_id, name='Test Place', description='A place for testing')
        self.data_manager.place_repository.get.return_value = place

        result = self.data_manager.get_place(place_id)

        self.data_manager.place_repository.get.assert_called_once_with(place_id)
        self.assertEqual(result, place)

    def test_update_place(self):
        place_id = 'place_123'
        new_data = {'name': 'Updated Place', 'description': 'Updated description'}
        updated_place = Place(place_id=place_id, name=new_data['name'], description=new_data['description'])
        self.data_manager.place_repository.update.return_value = updated_place

        result = self.data_manager.update_place(place_id, new_data)

        self.data_manager.place_repository.update.assert_called_once_with(place_id, new_data)
        self.assertEqual(result, updated_place)

    def test_delete_place(self):
        place_id = 'place_123'
        self.data_manager.place_repository.delete.return_value = True

        result = self.data_manager.delete_place(place_id)

        self.data_manager.place_repository.delete.assert_called_once_with(place_id)
        self.assertTrue(result)

    def test_get_all_places(self):
        places = [Place(place_id='place_123', name='Test Place', description='A place for testing')]
        self.data_manager.place_repository.get_all.return_value = places

        result = self.data_manager.get_all_places()

        self.data_manager.place_repository.get_all.assert_called_once()
        self.assertEqual(result, places)

    # Similar tests for User
    def test_save_user(self):
        user_data = {'username': 'testuser', 'email': 'test@example.com'}
        user_id = 'user_123'
        self.data_manager.user_repository.save.return_value = user_id

        result = self.data_manager.save_user(user_data)

        self.data_manager.user_repository.save.assert_called_once()
        self.assertEqual(result, user_id)

    def test_get_user(self):
        user_id = 'user_123'
        user = User(user_id=user_id, username='testuser', email='test@example.com')
        self.data_manager.user_repository.get.return_value = user

        result = self.data_manager.get_user(user_id)

        self.data_manager.user_repository.get.assert_called_once_with(user_id)
        self.assertEqual(result, user)

    def test_update_user(self):
        user_id = 'user_123'
        new_data = {'username': 'updateduser', 'email': 'updated@example.com'}
        updated_user = User(user_id=user_id, username=new_data['username'], email=new_data['email'])
        self.data_manager.user_repository.update.return_value = updated_user

        result = self.data_manager.update_user(user_id, new_data)

        self.data_manager.user_repository.update.assert_called_once_with(user_id, new_data)
        self.assertEqual(result, updated_user)

    def test_delete_user(self):
        user_id = 'user_123'
        self.data_manager.user_repository.delete.return_value = True

        result = self.data_manager.delete_user(user_id)

        self.data_manager.user_repository.delete.assert_called_once_with(user_id)
        self.assertTrue(result)

    def test_get_all_users(self):
        users = [User(user_id='user_123', username='testuser', email='test@example.com')]
        self.data_manager.user_repository.get_all.return_value = users

        result = self.data_manager.get_all_users()

        self.data_manager.user_repository.get_all.assert_called_once()
        self.assertEqual(result, users)

    # Similar tests for Review, Amenity, Country, City

    # Add similar test cases for the Review, Amenity, Country, and City methods.

if __name__ == '__main__':
    unittest.main()
