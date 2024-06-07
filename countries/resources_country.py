#!/usr/bin/env python3

from flask_restx import Namespace, Resource
from models_country import COUNTRIES

api = Namespace('countries', description='Country related operations')

@api.route('/')
class CountryList(Resource):
    def get(self):
        return [{'code': c.code, 'name': c.name} for c in COUNTRIES]

@api.route('/<string:country_code>')
class CountryDetail(Resource):
    def get(self, country_code):
        country = next((c for c in COUNTRIES if c.code == country_code), None)
        if not country:
            api.abort(404, "Country not found")
        return {'code': country.code, 'name': country.name}
