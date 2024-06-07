#!/usr/bin/python3
"""Contains the user validation and search functions."""

import re

def validate_email(email):
    """Validate the format of an email address."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def find_user(user_id, users):
    """Find a user by their ID in a list of users."""
    return next((user for user in users if user['id'] == user_id), None)
