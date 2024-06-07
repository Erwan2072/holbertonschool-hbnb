#!/usr/bin/env python3

from flask import Flask
from flask_restx import Api
from resources_country import api as country_ns
from resources_city import api as city_ns

app = Flask(__name__)
api = Api(app, version='1.0', title='Country and City API', description='API for managing countries and cities')

api.add_namespace(country_ns, path='/countries')
api.add_namespace(city_ns, path='/cities')

if __name__ == '__main__':
    app.run(debug=True)
