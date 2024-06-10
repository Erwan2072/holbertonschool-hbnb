#!/usr/bin/env python3

from flask import Flask, request
from flask_restx import Api, Resource, fields
from model_place import PlaceModel # Import du modèle de lieu
from persistance_place import data_store # Import du magasin de données

app = Flask(__name__)
api = Api(app)

# Définition du modèle de lieu pour la documentation
place_model = api.model('Place', {
    'name': fields.String(required=True, description='Nom du lieu'),
    'description': fields.String(description='Description du lieu'),
    'address': fields.String(required=True, description='Adresse du lieu'),
    'city_id': fields.Integer(required=True, description='ID de la ville associée'),
    'latitude': fields.Float(description='Latitude du lieu'),
    'longitude': fields.Float(description='Longitude du lieu'),
    'host_id': fields.String(description='ID de l\'hôte du lieu'),
    'number_of_rooms': fields.Integer(description='Nombre de chambres'),
    'number_of_bathrooms': fields.Integer(description='Nombre de salles de bains'),
    'price_per_night': fields.Float(description='Prix par nuit'),
    'max_guests': fields.Integer(description='Capacité maximale d\'hébergement'),
    'amenity_ids': fields.List(fields.Integer, description='Liste des IDs des équipements associés')
})

@api.route('/places')
class Places(Resource):
    # Endpoint pour récupérer tous les lieux
    @api.marshal_with(place_model)
    def get(self):
        return data_store.get_all_places(), 200

    # Endpoint pour créer un nouveau lieu
    @api.expect(place_model)
    @api.marshal_with(place_model, code=201)
    def post(self):
        new_place = request.json
        place_id = data_store.add_place(new_place)
        return data_store.get_place_by_id(place_id), 201

# Endpoint pour récupérer, mettre à jour et supprimer un lieu par son ID
@api.route('/places/<int:place_id>')
class Place(Resource):
    # Récupérer un lieu par son ID
    @api.marshal_with(place_model)
    def get(self, place_id):
        place = data_store.get_place_by_id(place_id)
        if place:
            return place, 200
        else:
            api.abort(404, message='Place non trouvée')

    # Mettre à jour un lieu par son ID
    @api.expect(place_model)
    @api.marshal_with(place_model)
    def put(self, place_id):
        # Implémenter la logique de mise à jour d'une place
        place = data_store.get_place_by_id(place_id)
        if place:
            updated_place = request.json
            updated_place['id'] = place_id
            index = data_store.data['places'].index(place)
            data_store.data['places'][index] = updated_place
            return updated_place, 200
        else:
            api.abort(404, message='Place non trouvée')

    # Supprimer un lieu par son ID
    @api.marshal_with(place_model)
    def delete(self, place_id):
        # Implémenter la logique de suppression d'une place
        place = data_store.get_place_by_id(place_id)
        if place:
            data_store.data['places'].remove(place)
            return place, 200
        else:
            api.abort(404, message='Place non trouvée')

if __name__ == '__main__':
    app.run(debug=True)
