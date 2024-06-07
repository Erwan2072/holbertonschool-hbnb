#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

# Données de pays pré-chargées
countries = [
    {"name": "France", "code": "FR"},
    {"name": "États-Unis", "code": "US"},
    {"name": "Allemagne", "code": "DE"}
]

# Données des villes
cities = []

# Endpoint pour récupérer les pays
@api.route('/countries')
class Countries(Resource):
    def get(self):
        return jsonify(countries)

@api.route('/countries/<string:country_code>', methods=['GET'])
class Country(Resource):
    def get(self, country_code):
        country = next((country for country in countries if country["code"] == country_code), None)
        if country:
            return jsonify(country)
        return jsonify({"error": "Country not found"}), 404

# Endpoint pour les villes par pays
@api.route('/countries/<string:country_code>/cities')
class CitiesByCountry(Resource):
    def get(self, country_code):
        return jsonify([city for city in cities if city['country_code'] == country_code])

# Endpoints pour la liste et la création des villes
@api.route('/cities')
class CityList(Resource):
    def get(self):
        return jsonify(cities)

    def post(self):
        new_city = request.json
        # Validation des données
        # Vérifier si le code de pays est valide
        if new_city['country_code'] not in [country['code'] for country in countries]:
            return {"error": "Code de pays invalide"}, 400
        # Vérifier s'il y a un doublon de nom de ville dans le même pays
        if any(city['name'] == new_city['name'] and city['country_code'] == new_city['country_code'] for city in cities):
            return {"error": "Le nom de la ville existe déjà dans le pays"}, 400
        cities.append(new_city)
        return new_city, 201

# Endpoints pour une ville spécifique
@api.route('/cities/<int:city_id>')
class City(Resource):
    def get(self, city_id):
        city = next((city for city in cities if city['id'] == city_id), None)
        if city:
            return city
        return {"error": "Ville non trouvée"}, 404

    def put(self, city_id):
        city = next((city for city in cities if city['id'] == city_id), None)
        if not city:
            return {"error": "Ville non trouvée"}, 404
        data = request.json
        # Mettre à jour les informations de la ville
        city.update(data)
        return city

    def delete(self, city_id):
        city = next((city for city in cities if city['id'] == city_id), None)
        if not city:
            return {"error": "Ville non trouvée"}, 404
        cities.remove(city)
        return "", 204

if __name__ == '__main__':
    app.run(debug=True)
