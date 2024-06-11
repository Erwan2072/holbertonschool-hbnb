#!/usr/bin/python3
"""Model for representing cities."""

class City:
    """Class representing a city."""
    def __init__(self, name, country_id):
        self.city_id = None
        self.name = name
        self.country_id = country_id

    def to_dict(self):
        """Returns the city data as a dictionary."""
        return {
            'city_id': self.city_id,
            'name': self.name,
            'country_id': self.country_id
        }
