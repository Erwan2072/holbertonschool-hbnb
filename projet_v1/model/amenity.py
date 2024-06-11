#!/usr/bin/python3
"""Model for representing amenities."""

class Amenity:
    """Class representing an amenity."""
    def __init__(self, name):
        self.amenity_id = None
        self.name = name

    def to_dict(self):
        """Returns the amenity data as a dictionary."""
        return {
            'amenity_id': self.amenity_id,
            'name': self.name
        }
