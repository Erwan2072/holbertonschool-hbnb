#!/usr/bin/python3


from datetime import datetime

users = []
user_id_counter = 1

def get_users():
    return users

def add_user(data):
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
    user['email'] = data['email']
    user['first_name'] = data['first_name']
    user['last_name'] = data['last_name']
    user['updated_at'] = datetime.strptime()
    return user

def delete_user(user):
    global users
    users = [u for u in users if u['id'] != user['id']]
