#!usr/bin/python3


class Amenity:
    def __init__(self, name, amenity_id=None):
        self.amenity_id = amenity_id
        self.name = name

    def serialize(self):
        return {
            'id': self.amenity_id,
            'name': self.name
        }
