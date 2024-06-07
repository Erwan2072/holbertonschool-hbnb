#!/usr/bin/python3


from flask import request
from flask_restx import Resource, Namespace
from model_user import create_user_model, create_user_input_model
from data_user import validate_email, find_user
from persistence_user import get_users, add_user, update_user, delete_user

ns = Namespace('users', description='User operations')

user_model = create_user_model(ns)
user_input_model = create_user_input_model(ns)

@ns.route('/')
class UserList(Resource):
    @ns.doc('list_users')
    @ns.marshal_list_with(user_model)
    def get(self):
        return get_users(), 200

    @ns.doc('create_user')
    @ns.expect(user_input_model)
    @ns.response(201, 'User created successfully')
    @ns.response(400, 'Invalid data')
    @ns.response(409, 'Email already exists')
    def post(self):
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
        user = find_user(user_id, get_users())
        if not user:
            return {'message': 'User not found'}, 404
        data = request.json
        if not validate_email(data['email']):
            return {'message': 'Invalid email format'}, 400
        if not data['first_name'] or not data['last_name']:
            return {'message': 'First name and last name cannot be empty'}, 400
        if any(u['email'] == data['email'] and u['id'] != user_id for u in get_users()):
            return {'message': 'Email already exists'}, 409

        updated_user = update_user(user, data)
        return updated_user, 200

    @ns.doc('delete_user')
    @ns.response(204, 'User deleted successfully')
    def delete(self, user_id):
        user = find_user(user_id, get_users())
        if not user:
            return {'message': 'User not found'}, 404
        delete_user(user)
        return '', 204

