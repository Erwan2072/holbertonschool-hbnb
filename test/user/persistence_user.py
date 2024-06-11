#!/usr/bin/python3
"""Manages the persistence of user data in memory."""

import json
from datetime import datetime

USERS_DATA_FILE = 'users_data.json'

def load_users():
    """Load the list of all users from the JSON file."""
    try:
        with open(USERS_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users(users):
    """Save the list of users to the JSON file."""
    with open(USERS_DATA_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def get_users():
    """Retrieve the list of all users."""
    return load_users()

def add_user(data):
    """ Add a new user to the list of users."""
    users = get_users()
    user_id = 1 if not users else max(user['id'] for user in users) + 1
    user = {
        'id': user_id,
        'email': data['email'],
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    users.append(user)
    save_users(users)
    return user

def update_user(user, data):
    """Update an existing user with new data."""
    user['email'] = data['email']
    user['first_name'] = data['first_name']
    user['last_name'] = data['last_name']
    user['updated_at'] = datetime.now().isoformat()
    save_users(get_users())
    return user

def delete_user(user):
    """ Delete a user from the list of users."""
    users = [u for u in users if u['id'] != user['id']]
    save_users(users)
