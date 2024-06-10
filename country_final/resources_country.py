#!/usr/bin/env python3

from flask_restx import Namespace, Resource
from models_country import COUNTRIES
from models_city import CITIES
from resources_city import city_model

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

"""Ajouter une route supplémentaire, chemin pour récupérer
toutes les villes d'un pays spécifique"""
@api.route('/<string:country_code>/cities')
class CountryCities(Resource):
    @api.marshal_list_with(city_model)
    def get(self, country_code):
        if not any(c.code == country_code for c in COUNTRIES):
            api.abort(404, "Country not found")
        return [city for city in CITIES if city.country_code == country_code]
