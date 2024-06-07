#!/usr/bin/python3


import re

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def find_user(user_id, users):
    return next((user for user in users if user['id'] == user_id), None)
