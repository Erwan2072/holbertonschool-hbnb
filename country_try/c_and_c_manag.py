#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Données de pays pré-chargées
countries = [
    {"name": "France", "code": "FR"},
    {"name": "États-Unis", "code": "US"},
    {"name": "Allemagne", "code": "DE"}
]

# Données des villes
cities = []
city_id_counter = 1

# Endpoint pour récupérer les pays
@app.route('/countries', methods=['GET'])
def get_countries():
    return jsonify(countries)

@app.route('/countries/<string:country_code>', methods=['GET'])
def get_country_by_code(country_code):
    return

# Endpoint pour les villes par pays
@app.route('/countries/<string:country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    return jsonify([city for city in cities if city['country_code'] == country_code])

# Endpoints pour la liste et la création des villes
@app.route('/cities', methods=['GET', 'POST'])
def manage_cities():
    if request.method == 'GET':
        return jsonify(cities)
    elif request.method == 'POST':
        new_city = request.json
        # Validation des données
        if new_city['country_code'] not in [country['code'] for country in countries]:
            return {"error": "Code de pays invalide"}, 400
        if any(city['name'] == new_city['name'] and city['country_code'] == new_city['country_code'] for city in cities):
            return {"error": "Le nom de la ville existe déjà dans le pays"}, 400
        new_city['id'] = city_id_counter
        city_id_counter += 1
        cities.append(new_city)
        return new_city, 201

# Endpoints pour une ville spécifique
@app.route('/cities/<int:city_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_city(city_id):
    city = next((city for city in cities if city['id'] == city_id), None)
    if not city:
        return {"error": "Ville non trouvée"}, 404

    if request.method == 'GET':
        return city
    elif request.method == 'PUT':
        data = request.json
        city.update(data)
        return city
    elif request.method == 'DELETE':
        cities.remove(city)
        return "", 204

if __name__ == '__main__':
    app.run(debug=True)
