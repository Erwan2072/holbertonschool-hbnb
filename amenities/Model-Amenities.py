#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# Dummy data to store amenities
amenities = []

# Amenity model
amenity_model = api.model('Amenity', {
    'id': fields.Integer,
    'name': fields.String(required=True),
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime
})

# Utility function to get an amenity by ID
def get_amenity_by_id(amenity_id):
    for amenity in amenities:
        if amenity['id'] == amenity_id:
            return amenity
    return None

# Endpoint to create a new amenity
@api.route('/amenities')
class CreateAmenity(Resource):
    @api.expect(amenity_model)
    def post(self):
        data = request.json
        name = data.get('name')

        # Check if amenity name is unique
        if any(amenity['name'] == name for amenity in amenities):
            return {'message': 'Amenity with this name already exists'}, 409

        amenity = {
            'id': len(amenities) + 1,
            'name': name,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        amenities.append(amenity)
        return amenity, 201

# Endpoint to retrieve all amenities
@api.route('/amenities')
class GetAmenities(Resource):
    def get(self):
        return amenities, 200

# Endpoint to retrieve a specific amenity
@api.route('/amenities/<int:amenity_id>')
class GetAmenity(Resource):
    def get(self, amenity_id):
        amenity = get_amenity_by_id(amenity_id)
        if amenity:
            return amenity, 200
        else:
            return {'message': 'Amenity not found'}, 404

# Endpoint to update an amenity
@api.route('/amenities/<int:amenity_id>')
class UpdateAmenity(Resource):
    @api.expect(amenity_model)
    def put(self, amenity_id):
        data = request.json
        amenity = get_amenity_by_id(amenity_id)
        if not amenity:
            return {'message': 'Amenity not found'}, 404
        name = data.get('name')

        # Check if new name conflicts with existing names
        if any(a['name'] == name for a in amenities if a['id'] != amenity_id):
            return {'message': 'Amenity with this name already exists'}, 409

        amenity['name'] = name
        amenity['updated_at'] = datetime.now()
        return amenity, 200

# Endpoint to delete an amenity
@api.route('/amenities/<int:amenity_id>')
class DeleteAmenity(Resource):
    def delete(self, amenity_id):
        amenity = get_amenity_by_id(amenity_id)
        if amenity:
            amenities.remove(amenity)
            return '', 204
        else:
            return {'message': 'Amenity not found'}, 404

if __name__ == '__main__':
    app.run(debug=True)

