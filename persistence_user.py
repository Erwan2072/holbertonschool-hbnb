#!/usr/bin/python3
"""Manages the persistence of user data in memory."""


from datetime import datetime

users = []
user_id_counter = 1

def get_users():
    """Retrieve the list of all users."""
    return users

def add_user(data):
    """ Add a new user to the list of users."""
    global users, user_id_counter
    user = {
        'id': user_id_counter,
        'email': data['email'],
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'created_at': datetime.strptime(),
        'updated_at': datetime.strptime()
    }
    users.append(user)
    user_id_counter += 1
    return user

def update_user(user, data):
    """Update an existing user with new data."""
    user['email'] = data['email']
    user['first_name'] = data['first_name']
    user['last_name'] = data['last_name']
    user['updated_at'] = datetime.strptime()
    return user

def delete_user(user):
    """ Delete a user from the list of users."""
    global users
    users = [u for u in users if u['id'] != user['id']]
