#!usr/bin/python3


from datetime import datetime

class Amenity:
    def __init__(self, name, amenity_id=None):
        self.amenity_id = amenity_id
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def serialize(self):
          return {
            'id': self.amenity_id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
