#!/usr/bin/python3

import unittest
from datetime import datetime
from city import City  # Assure-toi d'importer correctement la classe City

class TestCity(unittest.TestCase):

    def setUp(self):
        # Créer une instance de City pour une utilisation dans les tests
        self.city = City("Paris", "FR")

    def test_creation_city(self):
        # Vérifier que la city a été créée avec les attributs corrects
        self.assertEqual(self.city.name, "Paris")
        self.assertEqual(self.city.country_id, "FR")

        # Vérifier que la city a un identifiant non vide
        self.assertTrue(self.city.city_id)

        # Vérifier que les horodatages de création et de mise à jour sont définis et qu'ils sont proches dans le temps
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertAlmostEqual((self.city.updated_at - self.city.created_at).total_seconds(), 0, delta=1)

    def test_to_dict(self):
        # Vérifier que la méthode to_dict renvoie un dictionnaire contenant les bonnes clés
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn('city_id', city_dict)
        self.assertIn('name', city_dict)
        self.assertIn('country_id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)

        # Vérifier que les valeurs du dictionnaire correspondent aux attributs de la city
        self.assertEqual(city_dict['name'], self.city.name)
        self.assertEqual(city_dict['country_id'], self.city.country_id)
        self.assertEqual(city_dict['city_id'], self.city.city_id)
        self.assertEqual(city_dict['created_at'], self.city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'], self.city.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
