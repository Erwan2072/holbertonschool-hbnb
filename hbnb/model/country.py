#!/usr/bin/python3
"""Model for representing countries."""

class Country:
    """Class representing a country."""
    def __init__(self, name):
        self.country_id = None
        self.name = name

    def to_dict(self):
        """Returns the country data as a dictionary."""
        return {
            'country_id': self.country_id,
            'name': self.name
        }
