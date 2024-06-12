#!/usr/bin/python3
# API for managing cities

from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager
import uuid
from datetime import datetime

ns = Namespace('cities', description='Operations related to cities')
data_manager = DataManager()

# Model definition for a City
city_model = ns.model('City', {
    'id': fields.String(required=True, description='City ID'),
    'name': fields.String(required=True, description='City name'),
    'country_id': fields.Integer(required=True, description='Country ID'),
    'created_at': fields.DateTime(required=True, description='Date and time when the city was created'),
    'updated_at': fields.DateTime(required=True, description='Date and time when the city was last updated')
})
