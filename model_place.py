#!/usr/bin/env python3

import json
from flask import Flask, request , jsonify
from flask_restx import Api, Resource, fields
from datetime import datetime

app = Flask(__name__)
api = Api(app)

data_store = {
    'city': [{'id': 1, 'name': 'Paris'}, {'id': 2, 'name': 'Lyon'}],
    'amenity': [{'id': 1, 'name': 'WiFi'}, {'id': 2, 'name': 'Pool'}],
    'places': [{}]
}

json_data = json.dumps(data_store)

# Fonctions utilitaires pour obtenir des entités par ID
def get_city_by_id(city_id):
    data = request.json
    cities = data_store.get('city')
    city = next((city for city in cities if city['id'] == city_id), None)
    if city:
        return city
    return None

def get_amenities_by_ids(amenity_ids):
    data = request.json
    amenities = data.get('amenity')
    amenity = next((amenity for amenity in amenities if amenity['id'] in amenity_ids), None)
    if amenity:
        return amenity
    return None

# Endpoint pour récupérer toutes les places
@api.route('/places')
class GetPlaces(Resource):
    def get(self):
        places = data_store.get('places')
        return places, 200

    def post(self):
        places = data_store.get('places')
        # new_place = request.get_json()
        places.append(new_place)
        return places, 201

# Endpoint pour supprimer une place
@api.route('/places/<int:place_id>')
class Place_by_id(Resource):
    def get(self, place_id):
        data = request.get_json(self)
        places = data_store.get('places')
        place = next((p for p in places if p['id'] == place_id), None)
        if place:
            return place, 200
        else:
            return {'message': 'Place non trouvée'}, 404

    def put(self, place_id):
        data = request.get_json(self)
        places = data_store.get('places')
        place = next((p for p in places if p['id'] == place_id), None)
        if not place:
            return {'message': 'Place non trouvée'}, 404

        city_id = data.get('city_id')
        amenity_ids = data.get('amenity_ids', [])

        # Valider city_id
        if not get_city_by_id(city_id):
            return {'message': 'ID de la ville invalide'}, 400

        # Valider les amenities
        amenities = get_amenities_by_ids(amenity_ids)
        if len(amenities) != len(amenity_ids):
            return {'message': 'Un ou plusieurs ID d\'amenities sont invalides'}, 400


    def delete(self, place_id):
        data = request.get_json(self)
        places = data_store.get('places')
        place = next((p for p in places if p['id'] == place_id), None)
        if place:
            places.remove(place)
            return {}, 204
        return {'message': 'Place non trouvée'}, 404

if __name__ == '__main__':
    app.run(debug=True)
