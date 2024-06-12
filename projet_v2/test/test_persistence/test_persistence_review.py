#!/usr/bin/python3
import unittest
from unittest.mock import MagicMock
import sys
import os

# Ajouter le répertoire racine du projet au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from model.review import Review
from review_repository import ReviewRepository

class TestReviewRepository(unittest.TestCase):
    def setUp(self):
        self.repo = ReviewRepository()
        self.review1 = Review("Great product", "This product exceeded my expectations.", rating=5)
        self.review2 = Review("Not satisfied", "The product didn't meet my expectations.", rating=2)
        self.review3 = Review("Average product", "It's okay, but nothing special.", rating=3)

    def test_save(self):
        self.repo.save(self.review1)
        self.assertEqual(len(self.repo.reviews), 1)

    def test_get(self):
        self.repo.save(self.review1)
        self.repo.save(self.review2)
        self.assertEqual(self.repo.get(1), self.review1)
        self.assertEqual(self.repo.get(2), self.review2)

    def test_get_all(self):
        self.repo.save(self.review1)
        self.repo.save(self.review2)
        self.repo.save(self.review3)
        self.assertEqual(len(self.repo.get_all()), 3)

    def test_update(self):
        self.repo.save(self.review1)
        updated_data = {'title': 'Updated Title', 'content': 'Updated content'}
        self.assertTrue(self.repo.update(1, updated_data))
        self.assertEqual(self.repo.get(1).title, 'Updated Title')
        self.assertEqual(self.repo.get(1).content, 'Updated content')

    def test_delete(self):
        self.repo.save(self.review1)
        self.repo.save(self.review2)
        self.assertTrue(self.repo.delete(1))
        self.assertEqual(len(self.repo.reviews), 1)
        self.assertIsNone(self.repo.get(1))

if __name__ == '__main__':
    unittest.main()
