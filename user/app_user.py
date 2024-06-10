#!/usr/bin/python3


from flask import Flask
from flask_restx import Api
from api_user import ns as user_namespace

app = Flask(__name__)
api = Api(app, version='1.0', title='User API', description='A simple User API')

api.add_namespace(user_namespace)

if __name__ == '__main__':
    app.run(debug=True)
