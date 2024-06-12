#!/usr/bin/python3
"""Model for representing amenities."""

import uuid
from datetime import datetime

class Amenity:
    """Class representing an amenity."""
    def __init__(self, name):
        self.amenity_id = str(uuid.uuid4())  # Generate a UUID4 for unique identification
        self.name = name
        self.created_at = datetime.now()  # Record creation timestamp
        self.updated_at = datetime.now()  # Record update timestamp

    def to_dict(self):
        """Returns the amenity data as a dictionary."""
        return {
            'amenity_id': self.amenity_id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),  # Convert datetime to ISO 8601 format
            'updated_at': self.updated_at.isoformat()  # Convert datetime to ISO 8601 format
        }

