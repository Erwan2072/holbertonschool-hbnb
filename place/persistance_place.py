#!/usr/bin/env python3

from flask import json

# Module contenant la classe pour la persistance des données
class DataStore:
    # Initialisation du magasin de données avec des exemples de villes, équipements et lieux
    def __init__(self):
        self.data = {
            'cities': [{'id': 1, 'name': 'Paris'}, {'id': 2, 'name': 'Lyon'}],
            'amenities': [{'id': 1, 'name': 'WiFi'}, {'id': 2, 'name': 'Pool'}],
            'places': []
        }
        self.next_id = 1  # Pour générer des IDs uniques

    # Méthode pour ajouter un nouveau lieu
    def add_place(self, new_place):
        new_place['id'] = self.next_id  # Ajouter un ID unique
        self.data['places'].append(new_place)
        self.next_id += 1  # Incrémenter l'ID pour le prochain lieu
        return new_place['id']

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
