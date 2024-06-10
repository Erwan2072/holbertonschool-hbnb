#!/usr/bin/python3
"""Main file for configuring and running the Flask application."""


import sys
import os

"""Add the parent directory to PYTHONPATH"""
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'user')))

from flask import Flask, request
from flask_restx import Api, Resource, Namespace
from user.model_user import create_user_model, create_user_input_model
from user.data_user import validate_email, find_user
from user.persistence_user import get_users, add_user, update_user, delete_user

"""Create the Flask application instance"""
app = Flask(__name__)
api = Api(app, version='1.0', title='User API', description='A simple User API')

"""Define the Namespace for user operations"""
ns = Namespace('users', description='User operations')

user_model = create_user_model(ns)
user_input_model = create_user_input_model(ns)

@ns.route('/')
class UserList(Resource):
    @ns.doc('list_users')
    @ns.marshal_list_with(user_model)
    def get(self):
        """
        Retrieve a list of all users.
        Returns a list of user objects with status code 200.
        """
        return get_users(), 200

    @ns.doc('create_user')
    @ns.expect(user_input_model)
    @ns.response(201, 'User created successfully')
    @ns.response(400, 'Invalid data')
    @ns.response(409, 'Email already exists')
    def post(self):
        """
        Create a new user.
        Expects a JSON payload with email, first_name, and last_name.
        Validates the input and checks for uniqueness of the email.
        Returns the created user object with status code 201.
        """
        data = request.json
        if not validate_email(data['email']):
            return {'message': 'Invalid email format'}, 400
        if not data['first_name'] or not data['last_name']:
            return {'message': 'First name and last name cannot be empty'}, 400
        if any(user['email'] == data['email'] for user in get_users()):
            return {'message': 'Email already exists'}, 409

        user = add_user(data)
        return user, 201

@ns.route('/<int:user_id>')
@ns.response(404, 'User not found')
class User(Resource):
    @ns.doc('get_user')
    @ns.marshal_with(user_model)
    def get(self, user_id):
        """
        Retrieve details of a specific user by ID.
        Returns the user object with status code 200 if found, else 404.
        """
        user = find_user(user_id, get_users())
        if not user:
            return {'message': 'User not found'}, 404
        return user, 200

    @ns.doc('update_user')
    @ns.expect(user_input_model)
    @ns.response(200, 'User updated successfully')
    @ns.response(400, 'Invalid data')
    @ns.response(404, 'User not found')
    @ns.response(409, 'Email already exists')
    def put(self, user_id):
        """
        Update an existing user by ID.
        Expects a JSON payload with email, first_name, and last_name.
        Validates the input and checks for uniqueness of the email.
        Returns the updated user object with status code 200 if successful,
        else 404 or 409.
        """
        user = find_user(user_id, get_users())
        if not user:
            return {'message': 'User not found'}, 404
        data = request.json
        if not validate_email(data['email']):
            return {'message': 'Invalid email format'}, 400
        if not data['first_name'] or not data['last_name']:
            return {'message': 'First name and last name cannot be empty'}, 400
        if any(u['email'] == data['email'] and u['id']
               != user_id for u in get_users()):
            return {'message': 'Email already exists'}, 409

        updated_user = update_user(user, data)
        return updated_user, 200

    @ns.doc('delete_user')
    @ns.response(204, 'User deleted successfully')
    def delete(self, user_id):
        """
        Delete a user by ID.
        Returns status code 204 if successful, else 404.
        """
        user = find_user(user_id, get_users())
        if not user:
            return {'message': 'User not found'}, 404
        delete_user(user)
        return '', 204

"""Add the user namespace to the API"""
api.add_namespace(ns)

if __name__ == '__main__':
    app.run(debug=True)
