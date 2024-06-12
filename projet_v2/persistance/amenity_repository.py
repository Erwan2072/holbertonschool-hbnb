#!/usr/bin/python3
# Persistence for amenities

from model.amenity import Amenity
from persistence.ipersistence_manager import IPersistenceManager

class AmenityRepository(IPersistenceManager):
    """Class for managing the persistence of amenities."""
    def __init__(self):
        self.amenities = {}
        self.next_id = 1

    def save(self, amenity):
        """Saves an amenity."""
        if not hasattr(amenity, 'amenity_id'):
            amenity.amenity_id = self.next_id
            self.next_id += 1
        self.amenities[amenity.amenity_id] = amenity

    def get(self, amenity_id):
        """Fetches an amenity."""
        return self.amenities.get(amenity_id)

    def get_all(self):
        """Fetches all amenities."""
        return list(self.amenities.values())

    def update(self, amenity_id, new_amenity_data):
        """Updates an existing amenity."""
        if amenity_id in self.amenities:
            amenity = self.amenities[amenity_id]
            for key, value in new_amenity_data.items():
                setattr(amenity, key, value)
            self.save(amenity)
            return True
        return False

    def delete(self, amenity_id):
        """Deletes an existing amenity."""
        if amenity_id in self.amenities:
            del self.amenities[amenity_id]
            return True
        return False
