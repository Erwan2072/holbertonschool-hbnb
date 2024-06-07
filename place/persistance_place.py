#!/usr/bin/env python3

import json

# Module contenant la classe pour la persistance des données
class DataStore:
     # Initialisation du magasin de données avec des exemples de villes, équipements et lieux
    def __init__(self):
        self.data = {
            'cities': [{'id': 1, 'name': 'Paris'}, {'id': 2, 'name': 'Lyon'}],
            'amenities': [{'id': 1, 'name': 'WiFi'}, {'id': 2, 'name': 'Pool'}],
            'places': []
        }

    # Méthode pour ajouter un nouveau lieu
    def add_place(self, new_place):
        self.data['places'].append(new_place)
        # Return the ID of the newly added place
        return len(self.data['places'])

    # Méthode pour récupérer tous les lieux
    def get_all_places(self):
        return self.data['places']

    # Méthode pour récupérer un lieu par son ID
    def get_place_by_id(self, place_id):
        for place in self.data['places']:
            if place['id'] == place_id:
                return place
        return None

# Instance de la classe DataStore pour la persistance des donnée
data_store = DataStore()
