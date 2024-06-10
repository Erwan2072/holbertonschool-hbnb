#!/usr/bin/python3
"""Contains user validation and search functions."""

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

def validate_email(email):
    """Validate the format of an email address."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def find_user(user_id):
    """Find a user by their ID."""
    users = load_users()
    return next((user for user in users if user['id'] == user_id), None)

# Fonctions supplémentaires selon les besoins

def add_user(data):
    """ Add a new user to the list of users."""
    users = load_users()
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

def update_user(user_id, data):
    """ Update an existing user with new data."""
    users = load_users()
    user = find_user(user_id)
    if user:
        user.update(data)
        user['updated_at'] = datetime.now().isoformat()
        save_users(users)
        return user
    return None

def delete_user(user_id):
    """ Delete a user by ID."""
    users = load_users()
    user = find_user(user_id)
    if user:
        users.remove(user)
        save_users(users)
        return True
    return False
