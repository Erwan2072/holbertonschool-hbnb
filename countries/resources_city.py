#!/usr/bin/env python3

from flask_restx import Namespace, Resource, fields, reqparse
from models_city import City, CITIES
from models_country import COUNTRIES

api = Namespace('cities', description='City related operations')

city_model = api.model('City', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True),
    'country_code': fields.String(required=True),
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime
})

city_parser = reqparse.RequestParser()
city_parser.add_argument('name', required=True, help='Name of the city')
city_parser.add_argument('country_code', required=True, help='Country code')

@api.route('/')
class CityList(Resource):
    @api.marshal_list_with(city_model)
    def get(self):
        return CITIES

    @api.expect(city_parser)
    @api.response(201, 'City created successfully')
    @api.response(400, 'Invalid input')
    @api.response(409, 'City name already exists in the country')
    def post(self):
        args = city_parser.parse_args()
        country_code = args['country_code']
        if not any(c.code == country_code for c in COUNTRIES):
            api.abort(400, "Invalid country code")

        if any(city.name == args['name'] and city.country_code == country_code for city in CITIES):
            api.abort(409, "City name already exists in the country")

        new_city = City(name=args['name'], country_code=country_code)
        CITIES.append(new_city)
        return new_city, 201

@api.route('/<int:city_id>')
class CityDetail(Resource):
    @api.marshal_with(city_model)
    @api.response(404, 'City not found')
    def get(self, city_id):
        city = next((city for city in CITIES if city.id == city_id), None)
        if not city:
            api.abort(404, "City not found")
        return city

    @api.expect(city_parser)
    @api.response(200, 'City updated successfully')
    @api.response(400, 'Invalid input')
    @api.response(404, 'City not found')
    @api.response(409, 'City name already exists in the country')
    def put(self, city_id):
        city = next((city for city in CITIES if city.id == city_id), None)
        if not city:
            api.abort(404, "City not found")

        args = city_parser.parse_args()
        country_code = args['country_code']
        if not any(c.code == country_code for c in COUNTRIES):
            api.abort(400, "Invalid country code")

        if any(c.name == args['name'] and c.country_code == country_code and c.id != city_id for c in CITIES):
            api.abort(409, "City name already exists in the country")

        city.name = args['name']
        city.country_code = args['country_code']
        city.updated_at = datetime.utcnow()
        return city

    @api.response(204, 'City deleted successfully')
    @api.response(404, 'City not found')
    def delete(self, city_id):
        global CITIES
        city = next((city for city in CITIES if city.id == city_id), None)
        if not city:
            api.abort(404, "City not found")
        CITIES = [c for c in CITIES if c.id != city_id]
        return '', 204
