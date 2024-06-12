#!/usr/bin/python3
# API for managing countries

from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager

api = Namespace('countries', description='Operations related to countries')
data_manager = DataManager()

# Model definition for a Country
country_model = api.model('Country', {
    'name': fields.String(required=True, description='Country name')
})

@api.route('/')
class Countries(Resource):
    @api.marshal_list_with(country_model)
    def get(self):
        """Fetch all countries."""
        return data_manager.get_all_countries()

    @api.expect(country_model)
    @api.response(201, 'Country created successfully')
    @api.response(400, 'Invalid request')
    def post(self):
        """Create a new country."""
        new_country_data = request.json
        country_id = data_manager.save_country(new_country_data)
        return {'message': 'Country created successfully', 'country_id': country_id}, 201

@api.route('/<int:country_id>')
class CountryResource(Resource):
    @api.marshal_with(country_model)
    @api.response(404, 'Country not found')
    def get(self, country_id):
        """Fetch a country by its ID."""
        country_data = data_manager.get_country(country_id)
        if country_data:
            return country_data
        else:
            api.abort(404, "Country not found")

    @api.response(204, 'Country deleted successfully')
    @api.response(404, 'Country not found')
    def delete(self, country_id):
        """Delete an existing country."""
        if data_manager.delete_country(country_id):
            return '', 204
        else:
            api.abort(404, "Country not found")

    @api.expect(country_model)
    @api.response(204, 'Country updated successfully')
    @api.response(400, 'Invalid request')
    @api.response(404, 'Country not found')
    def put(self, country_id):
        """Update an existing country."""
        new_country_data = request.json
        if data_manager.update_country(country_id, new_country_data):
            return '', 204
        else:
            api.abort(404, "Country not found")
