#!usr/bin/python3

from model_amenity import Amenity

class AmenityPersistence:
    def __init__(self):
        self.amenities = []
        self.counter = 1

    def create_amenity(self, amenity):
        for existing_amenity in self.amenities:
            if existing_amenity.name == amenity.name:
                return False, None
        amenity.amenity_id = str(self.counter)
        self.counter += 1
        self.amenities.append(amenity)
        return True, amenity

    def get_amenities(self):
        return self.amenities

    def get_amenity_by_id(self, amenity_id):
        for amenity in self.amenities:
            if amenity.amenity_id == amenity_id:
                return amenity
        return None

    def update_amenity(self, updated_amenity):
        for i, amenity in enumerate(self.amenities):
            if amenity.amenity_id == updated_amenity.amenity_id:
                updated_amenity.created_at = amenity.created_at
                updated_amenity.updated_at = datetime.now()
                self.amenities[i] = updated_amenity
                return True, updated_amenity
        return False, None

    def delete_amenity(self, amenity_id):
        for i, amenity in enumerate(self.amenities):
            if amenity.amenity_id == amenity_id:
                del self.amenities[i]
                return True
        return False
