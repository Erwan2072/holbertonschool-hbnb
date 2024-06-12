#!/usr/bin/python3

import unittest
import sys
import os
from unittest.mock import MagicMock

# Ajouter le répertoire racine du projet au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from model.amenity import Amenity
from persistence.amenity_repository import AmenityRepository
import uuid
from datetime import datetime

class TestAmenityRepository(unittest.TestCase):

    def setUp(self):
        self.repo = AmenityRepository()
        self.amenity = Amenity(name="Swimming Pool")

    def test_save(self):
        # Test saving a new amenity
        self.repo.save(self.amenity)
        self.assertIn(self.amenity.amenity_id, self.repo.amenities)
        self.assertEqual(self.repo.amenities[self.amenity.amenity_id], self.amenity)

        # Test saving an object that is not an instance of Amenity
        with self.assertRaises(ValueError):
            self.repo.save("not_an_amenity")

    def test_get(self):
        # Test getting an amenity
        self.repo.save(self.amenity)
        fetched_amenity = self.repo.get(self.amenity.amenity_id)
        self.assertEqual(fetched_amenity, self.amenity)

        # Test getting a non-existent amenity
        self.assertIsNone(self.repo.get("non_existent_id"))

    def test_get_all(self):
        # Test getting all amenities
        self.repo.save(self.amenity)
        all_amenities = self.repo.get_all()
        self.assertEqual(len(all_amenities), 1)
        self.assertEqual(all_amenities[0], self.amenity)

    def test_update(self):
        # Mock the update_from_dict method in the Amenity class
        self.amenity.update_from_dict = MagicMock()

        # Test updating an existing amenity
        self.repo.save(self.amenity)
        new_data = {"name": "Updated Pool"}
        result = self.repo.update(self.amenity.amenity_id, new_data)
        self.amenity.update_from_dict.assert_called_once_with(new_data)
        self.assertTrue(result)

        # Test updating a non-existent amenity
        result = self.repo.update("non_existent_id", new_data)
        self.assertFalse(result)

    def test_delete(self):
        # Test deleting an existing amenity
        self.repo.save(self.amenity)
        result = self.repo.delete(self.amenity.amenity_id)
        self.assertNotIn(self.amenity.amenity_id, self.repo.amenities)
        self.assertTrue(result)

        # Test deleting a non-existent amenity
        result = self.repo.delete("non_existent_id")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
