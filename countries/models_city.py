#!/usr/bin/env python3

from datetime import datetime

class City:
    _id_counter = 1

    def __init__(self, name, country_code):
        self.id = City._id_counter
        self.name = name
        self.country_code = country_code
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        City._id_counter += 1

# In-memory database of cities
CITIES = []
