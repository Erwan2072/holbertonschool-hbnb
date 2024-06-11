#!/usr/bin/python3
# API for managing amenities

from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager

ns = Namespace('amenities', description='Operations related to amenities')
data_manager = DataManager()

# Model definition for an Amenity
amenity_model = ns.model('Amenity', {
    'name': fields.String(required=True, description='Amenity name')
})

@ns.route('/')
class Amenities(Resource):
    @ns.marshal_list_with(amenity_model)
    def get(self):
        """Fetch all amenities."""
        return data_manager.get_all_amenities()

    @ns.expect(amenity_model)
    @ns.response(201, 'Amenity created successfully')
    @ns.response(400, 'Invalid request')
    def post(self):
        """Create a new amenity."""
        new_amenity_data = request.json
        amenity_id = data_manager.save_amenity(new_amenity_data)
        return {'message': 'Amenity created successfully', 'amenity_id': amenity_id}, 201

@ns.route('/<int:amenity_id>')
class AmenityResource(Resource):
    @ns.marshal_with(amenity_model)
    @ns.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Fetch an amenity by its ID."""
        amenity_data = data_manager.get_amenity(amenity_id)
        if amenity_data:
            return amenity_data
        else:
            ns.abort(404, "Amenity not found")

    @ns.response(204, 'Amenity deleted successfully')
    @ns.response(404, 'Amenity not found')
    def delete(self, amenity_id):
        """Delete an existing amenity."""
        if data_manager.delete_amenity(amenity_id):
            return '', 204
        else:
            ns.abort(404, "Amenity not found")

    @ns.expect(amenity_model)
    @ns.response(204, 'Amenity updated successfully')
    @ns.response(400, 'Invalid request')
    @ns.response(404, 'Amenity not found')
    def put(self, amenity_id):
        """Update an existing amenity."""
        new_amenity_data = request.json
        if data_manager.update_amenity(amenity_id, new_amenity_data):
            return '', 204
        else:
            ns.abort(404, "Amenity not found")
