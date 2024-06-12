#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from model_amenity import Amenity
from persistence_amenity import AmenityPersistence

# Create a blueprint for the amenity API
amenity_api = Blueprint('amenity_api', __name__)
amenity_persistence = AmenityPersistence()

# Endpoint to create a new amenity
@amenity_api.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.json
    if 'name' not in data or not data['name']:
        return jsonify({'error': 'Amenity name is required'}), 400
    amenity = Amenity(data['name'])
    success, created_amenity = amenity_persistence.create_amenity(amenity)
    if success:
        return jsonify(created_amenity.serialize()), 201
    else:
        return jsonify({'error': 'Amenity with the same name already exists'}), 409

# Endpoint to retrieve all amenities
@amenity_api.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = amenity_persistence.get_amenities()
    return jsonify([amenity.serialize() for amenity in amenities]), 200

# Endpoint to retrieve a specific amenity by ID
@amenity_api.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = amenity_persistence.get_amenity_by_id(amenity_id)
    if amenity:
        return jsonify(amenity.serialize()), 200
    else:
        return jsonify({'error': 'Amenity not found'}), 404

# Endpoint to update a specific amenity by ID
@amenity_api.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.json
    if 'name' not in data or not data['name']:
        return jsonify({'error': 'Amenity name is required'}), 400
    amenity = Amenity(data['name'], amenity_id)
    success, updated_amenity = amenity_persistence.update_amenity(amenity)
    if success:
        return jsonify(updated_amenity.serialize()), 200
    else:
        return jsonify({'error': 'Amenity not found'}), 404

# Endpoint to delete a specific amenity by ID
@amenity_api.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    success = amenity_persistence.delete_amenity(amenity_id)
    if success:
        return '', 204
    else:
        return jsonify({'error': 'Amenity not found'}), 404
