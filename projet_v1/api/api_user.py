#!/usr/bin/python3
# API for managing users

from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager

ns = Namespace('users', description='Operations related to users')
data_manager = DataManager()

# Model definition for a User
user_model = ns.model('User', {
    'username': fields.String(required=True, description='Username'),
    'email': fields.String(required=True, description='Email'),
    'password': fields.String(required=True, description='Password')
})

@ns.route('/')
class Users(Resource):
    @ns.marshal_list_with(user_model)
    def get(self):
        """Fetch all users."""
        return data_manager.get_all_users()

    @ns.expect(user_model)
    @ns.response(201, 'User created successfully')
    @ns.response(400, 'Invalid request')
    def post(self):
        """Create a new user."""
        new_user_data = request.json
        user_id = data_manager.save_user(new_user_data)
        return {'message': 'User created successfully', 'user_id': user_id}, 201

@ns.route('/<int:user_id>')
class UserResource(Resource):
    @ns.marshal_with(user_model)
    @ns.response(404, 'User not found')
    def get(self, user_id):
        """Fetch a user by their ID."""
        user_data = data_manager.get_user(user_id)
        if user_data:
            return user_data
        else:
            ns.abort(404, "User not found")

    @ns.response(204, 'User deleted successfully')
    @ns.response(404, 'User not found')
    def delete(self, user_id):
        """Delete an existing user."""
        if data_manager.delete_user(user_id):
            return '', 204
        else:
            ns.abort(404, "User not found")

    @ns.expect(user_model)
    @ns.response(204, 'User updated successfully')
    @ns.response(400, 'Invalid request')
    @ns.response(404, 'User not found')
    def put(self, user_id):
        """Update an existing user."""
        new_user_data = request.json
        if data_manager.update_user(user_id, new_user_data):
            return '', 204
        else:
            ns.abort(404, "User not found")
