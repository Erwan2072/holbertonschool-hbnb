#!/usr/bin/python3
"""Defines the user data models for the API."""

from flask_restx import fields

def create_user_model(api):
    """Create a model for representing user data in the API."""
    return api.model('User', {
        'id': fields.Integer(readOnly=True, description='The user unique identifier'),
        'email': fields.String(required=True, description='The user email'),
        'first_name': fields.String(required=True, description='The user first name'),
        'last_name': fields.String(required=True, description='The user last name'),
        'created_at': fields.DateTime(description='The user creation date'),
        'updated_at': fields.DateTime(description='The user last update date'),
    })

def create_user_input_model(api):
    """Create a model for representing user input data in the API"""
    return api.model('UserInput', {
        'email': fields.String(required=True, description='The user email'),
        'first_name': fields.String(required=True, description='The user first name'),
        'last_name': fields.String(required=True, description='The user last name'),
    })
