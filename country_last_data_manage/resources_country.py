#!/usr/bin/env python3

from flask_restx import Namespace, Resource, fields
from models_country import Country
from DataManager import DataManager

api = Namespace('countries', description='Country related operations')
data_manager = DataManager()

country_model = api.model('Country', {
    'code': fields.String(readonly=True),
    'name': fields.String(required=True)
})

@api.route('/')
class CountryList(Resource):
    def get(self):
        return data_manager.countries

@api.route('/<string:country_code>')
class CountryDetail(Resource):
    def get(self, country_code):
        country = data_manager.get(country_code, 'country')
        if not country:
            api.abort(404, "Country not found")
        return country

@api.route('/<string:country_code>/cities')
class CountryCities(Resource):
    @api.marshal_list_with(api.model('City', {
        'id': fields.Integer(readonly=True),
        'name': fields.String(required=True),
        'country_code': fields.String(required=True),
        'created_at': fields.String,
        'updated_at': fields.String
    }))
    def get(self, country_code):
        if not any(c.code == country_code for c in data_manager.countries):
            api.abort(404, "Country not found")
        return [city for city in data_manager.cities if city.country_code == country_code]
