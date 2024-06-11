#!/usr/bin/python3
# API for managing cities

from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager

api = Namespace('cities', description='Operations related to cities')
data_manager = DataManager()

# Model definition for a City
city_model = api.model('City', {
    'name': fields.String(required=True, description='City name'),
    'country_id': fields.Integer(required=True, description='Country ID')
})

@api.route('/')
class Cities(Resource):
    @api.marshal_list_with(city_model)
    def get(self):
        """Fetch all cities."""
        return data_manager.get_all_cities()

    @api.expect(city_model)
    @api.response(201, 'City created successfully')
    @api.response(400, 'Invalid request')
    def post(self):
        """Create a new city."""
        new_city_data = request.json
        city_id = data_manager.save_city(new_city_data)
        return {'message': 'City created successfully', 'city_id': city_id}, 201

@api.route('/<int:city_id>')
class CityResource(Resource):
    @api.marshal_with(city_model)
    @api.response(404, 'City not found')
    def get(self, city_id):
        """Fetch a city by its ID."""
        city_data = data_manager.get_city(city_id)
        if city_data:
            return city_data
        else:
            api.abort(404, "City not found")

    @api.response(204, 'City deleted successfully')
    @api.response(404, 'City not found')
    def delete(self, city_id):
        """Delete an existing city."""
        if data_manager.delete_city(city_id):
            return '', 204
        else:
            api.abort(404, "City not found")

    @api.expect(city_model)
    @api.response(204, 'City updated successfully')
    @api.response(400, 'Invalid request')
    @api.response(404, 'City not found')
    def put(self, city_id):
        """Update an existing city."""
        new_city_data = request.json
        if data_manager.update_city(city_id, new_city_data):
            return '', 204
        else:
            api.abort(404, "City not found")
