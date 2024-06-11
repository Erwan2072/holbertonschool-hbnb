#!/usr/bin/python3
# API for managing places

from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager

api = Namespace('places', description='Operations related to places')
data_manager = DataManager()

# Model definition for a Place
place_model = api.model('Place', {
    'name': fields.String(required=True, description='Place name'),
    'description': fields.String(description='Place description'),
    'address': fields.String(description='Place address'),
    'city_id': fields.Integer(description='City ID'),
    'latitude': fields.Float(description='Latitude'),
    'longitude': fields.Float(description='Longitude'),
    'host_id': fields.Integer(description='Host ID'),
    'number_of_rooms': fields.Integer(description='Number of rooms'),
    'number_of_bathrooms': fields.Integer(description='Number of bathrooms'),
    'price_per_night': fields.Float(description='Price per night'),
    'max_guests': fields.Integer(description='Maximum number of guests'),
    'amenity_ids': fields.List(fields.String, description='List of amenity IDs')
})

@api.route('/')
class Places(Resource):
    @api.marshal_list_with(place_model)
    def get(self):
        """Fetch all places."""
        return data_manager.get_all_places()

    @api.expect(place_model)
    @api.response(201, 'Place created successfully')
    @api.response(400, 'Invalid request')
    def post(self):
        """Create a new place."""
        new_place_data = request.json
        place_id = data_manager.save_place(new_place_data)
        return {'message': 'Place created successfully', 'place_id': place_id}, 201

@api.route('/<int:place_id>')
class PlaceResource(Resource):
    @api.marshal_with(place_model)
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Fetch a place by its ID."""
        place_data = data_manager.get_place(place_id)
        if place_data:
            return place_data
        else:
            api.abort(404, "Place not found")

    @api.response(204, 'Place deleted successfully')
    @api.response(404, 'Place not found')
    def delete(self, place_id):
        """Delete an existing place."""
        if data_manager.delete_place(place_id):
            return '', 204
        else:
            api.abort(404, "Place not found")

    @api.expect(place_model)
    @api.response(204, 'Place updated successfully')
    @api.response(400, 'Invalid request')
    @api.response(404, 'Place not found')
    def put(self, place_id):
        """Update an existing place."""
        new_place_data = request.json
        if data_manager.update_place(place_id, new_place_data):
            return '', 204
        else:
            api.abort(404, "Place not found")
