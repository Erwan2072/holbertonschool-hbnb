#!/usr/bin/python3
"""Main file for configuring and running the Flask application."""

from flask import Flask
from flask_restx import Api
from api_user import ns as user_namespace

"""Create the Flask application instance"""
app = Flask(__name__)
api = Api(app, version='1.0', title='User API', description='A simple User API')

api.add_namespace(user_namespace)

if __name__ == '__main__':
    app.run(debug=True)
