#!/usr/bin/python3
# NS for managing places

from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager

ns = Namespace('places', description='Operations related to places')
data_manager = DataManager()

# Model definition for a Place
place_model = ns.model('Place', {
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

@ns.route('/')
class Places(Resource):
    @ns.marshal_list_with(place_model)
    def get(self):
        """Fetch all places."""
        return data_manager.get_all_places()

    @ns.expect(place_model)
    @ns.response(201, 'Place created successfully')
    @ns.response(400, 'Invalid request')
    def post(self):
        """Create a new place."""
        new_place_data = request.json
        place_id = data_manager.save_place(new_place_data)
        return {'message': 'Place created successfully', 'place_id': place_id}, 201

@ns.route('/<int:place_id>')
class PlaceResource(Resource):
    @ns.marshal_with(place_model)
    @ns.response(404, 'Place not found')
    def get(self, place_id):
        """Fetch a place by its ID."""
        place_data = data_manager.get_place(place_id)
        if place_data:
            return place_data
        else:
            ns.abort(404, "Place not found")

    @ns.response(204, 'Place deleted successfully')
    @ns.response(404, 'Place not found')
    def delete(self, place_id):
        """Delete an existing place."""
        if data_manager.delete_place(place_id):
            return '', 204
        else:
            ns.abort(404, "Place not found")

    @ns.expect(place_model)
    @ns.response(204, 'Place updated successfully')
    @ns.response(400, 'Invalid request')
    @ns.response(404, 'Place not found')
    def put(self, place_id):
        """Update an existing place."""
        new_place_data = request.json
        if data_manager.update_place(place_id, new_place_data):
            return '', 204
        else:
            ns.abort(404, "Place not found")