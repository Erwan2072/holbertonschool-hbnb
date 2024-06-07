#!/usr/bin/env python3


# test_review.py
import unittest
from Reviews import Review


class TestReview(unittest.TestCase):
    # Test de l'initialisation de la classe Review
    def test_initialization(self):
        review = Review("Great course!", "5 stars")
        self.assertEqual(review.feedbacks, "Great course!")
        self.assertEqual(review.rating, "5 stars")

    # Test du setter pour feedbacks
    def test_feedbacks_setter(self):
        review = Review("Great course!", "5 stars")
        review.feedbacks = "Excellent teaching!"
        self.assertEqual(review.feedbacks, "Excellent teaching!")

    # Test du setter pour rating
    def test_rating_setter(self):
        review = Review("Great course!", "5 stars")
        review.rating = "4.5 stars"
        self.assertEqual(review.rating, "4.5 stars")

    # Test de la méthode __str__ pour la représentation de l'objet
    def test_str_method(self):
        review = Review("Great course!", "5 stars")
        self.assertEqual(str(review), "Feedbacks: Great course!, Rating: 5 stars")

    # Test des valeurs invalides pour feedbacks
    def test_invalid_feedbacks(self):
        with self.assertRaises(ValueError):
            Review("", "5 stars") # Chaîne vide
        with self.assertRaises(ValueError):
            Review(None, "5 stars") # None
        with self.assertRaises(ValueError):
            review = Review("Great course!", "5 stars")
            review.feedbacks = "" # Chaîne vide pour le setter

    # Test des valeurs invalides pour rating
    def test_invalid_rating(self):
        with self.assertRaises(ValueError):
            Review("Great course!", "") # Chaîne vide
        with self.assertRaises(ValueError):
            Review("Great course!", None) # None
        with self.assertRaises(ValueError):
            review = Review("Great course!", "5 stars")
            review.rating = "" # Chaîne vide pour le setter

    # Test pour une chaîne longue dans feedbacks
    def test_long_feedbacks(self):
        long_feedback = "a" * 1000  # Longue chaîne de 1000 caractères
        review = Review(long_feedback, "5 stars")
        self.assertEqual(review.feedbacks, long_feedback)

# Test pour une chaîne longue dans rating
    def test_long_rating(self):
        long_rating = "a" * 100  # Longue chaîne de 100 caractères
        review = Review("Great course!", long_rating)
        self.assertEqual(review.rating, long_rating)

    # Test des modifications successives des attributs
    def test_successive_modifications(self):
        review = Review("Good", "4 stars")
        review.feedbacks = "Very good"
        self.assertEqual(review.feedbacks, "Very good")
        review.feedbacks = "Excellent"
        self.assertEqual(review.feedbacks, "Excellent")

        review.rating = "4.5 stars"
        self.assertEqual(review.rating, "4.5 stars")
        review.rating = "5 stars"
        self.assertEqual(review.rating, "5 stars")

    # Test des valeurs non standards mais valides pour feedbacks et rating
    def test_non_standard_but_valid_feedbacks_and_rating(self):
        review = Review("   Great course!   ", "   5 stars   ")
        self.assertEqual(review.feedbacks, "   Great course!   ")
        self.assertEqual(review.rating, "   5 stars   ")

if __name__ == '__main__':
    unittest.main()
