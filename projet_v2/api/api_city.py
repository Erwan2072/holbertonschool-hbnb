#!/usr/bin/python3
# API for managing cities

from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager
from datetime import datetime
"""Importing the DataManager class to manage data operations"""
import uuid
"""For generating unique identifiers"""

"""Creating a namespace for the API endpoints related to cities"""
ns = Namespace('cities', description='Operations related to cities')
data_manager = DataManager()
"""Creating an instance of the DataManager class"""

"""Model definition for a City, specifying its structure"""
city_model = ns.model('City', {
    'id': fields.String(required=True, description='City ID'),
    'name': fields.String(required=True, description='City name'),
    'country_id': fields.Integer(required=True, description='Country ID'),
    'created_at': fields.DateTime(required=True, description='Date and time when the city was created'),
    'updated_at': fields.DateTime(required=True, description='Date and time when the city was last updated')
})


@ns.route('/')
class Cities(Resource):
    @ns.marshal_list_with(city_model)
    def get(self):
        """Fetch all cities from datamanager."""
        return data_manager.get_all_cities()

    @ns.expect(city_model)
    @ns.response(201, 'City created successfully')
    @ns.response(400, 'Invalid request')
    def post(self):
        """
        Create a new city.
        Getting the JSON data from the request
        Generating a unique ID for the new city
        Setting the creation timestamp
        Setting the update timestamp
        Saving the new city data
        Returning success response
        """
        new_city_data = request.json
        new_city_data['id'] = str(uuid.uuid4())
        new_city_data['created_at'] = datetime.now()
        new_city_data['updated_at'] = datetime.now()
        city_id = data_manager.save_city(new_city_data)
        return {'message': 'City created successfully', 'city_id': city_id}, 201


@ns.route('/<string:city_id>')
class CityResource(Resource):
    @ns.marshal_with(city_model)
    @ns.response(404, 'City not found')
    def get(self, city_id):
        """Fetch a city by its ID.
            Retrieving the city data by its ID
            Returning the city data if found
            Aborting with 404 error if city not found
        """
        city_data = data_manager.get_city(city_id)
        if city_data:
            return city_data
        else:
            ns.abort(404, "City not found")

    @ns.response(204, 'City deleted successfully')
    @ns.response(404, 'City not found')
    def delete(self, city_id):
        """Delete an existing city.
            Deleting the city and checking if successful
            Returning success response
            Aborting with 404 error if city not found
        """
        if data_manager.delete_city(city_id):
            return '', 204
        else:
            ns.abort(404, "City not found")

    @ns.expect(city_model)
    @ns.response(204, 'City updated successfully')
    @ns.response(400, 'Invalid request')
    @ns.response(404, 'City not found')
    def put(self, city_id):
        """Update an existing city.
            Getting the updated city data from the request
            Setting the ID of the city to update
            Setting the update timestamp
            Updating the city data and checking if successful
            Returning success response
            Aborting with 404 error if city not found
        """
        new_city_data = request.json
        new_city_data['id'] = city_id
        new_city_data['updated_at'] = datetime.now()
        if data_manager.update_city(city_id, new_city_data):
            return '', 204
        else:
            ns.abort(404, "City not found")
