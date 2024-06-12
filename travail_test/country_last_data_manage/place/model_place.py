#!/usr/bin/env python3

# Module contenant la définition du modèle de lieu
class PlaceModel:
    # Méthode statique pour récupérer un lieu par son ID
    @staticmethod
    def get_place_by_id(place_id):
        # Utilisation du magasin de données pour récupérer le lieu
        return data_store.get_place_by_id(place_id)
