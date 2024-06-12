#!/usr/bin/python3
"""
Entry point for the application.

This module initializes the Flask application and sets up the API namespaces.
"""
import os
from flask import Flask
from flask_restx import Api
from api.api_place import ns as api_place
from api.api_user import ns as api_user
from api.api_review import ns as api_review
from api.api_amenity import ns as api_amenity
from api.api_country import ns as api_country
from api.api_city import ns as api_city

"""Initialize Flask app"""
app = Flask(__name__)

"""Initialize API with Flask app"""
ns = Api(app)

"""Adding namespaces for each entity"""
ns.add_namespace(api_place, path='/places')
ns.add_namespace(api_user, path='/users')
ns.add_namespace(api_review, path='/reviews')
ns.add_namespace(api_amenity, path='/amenities')
ns.add_namespace(api_country, path='/countries')
ns.add_namespace(api_city, path='/cities')


if __name__ == "__main__":
    """
    Run the Flask application.

    Retrieves port number from the environment variables or defaults to 5000.
    Runs the Flask application on host 0.0.0.0 and the specified port.

    Environment Variables:
        PORT (str): port number to run the application on (default is 5000).
    """
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

    """ Uncomment the following line to enable debug mode for Docker
    app.run(debug=True)"""
