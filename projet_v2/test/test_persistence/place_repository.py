#!/usr/bin/python3
# Persistence for places

from model.place import Place
from persistence.ipersistence_manager import IPersistenceManager

class PlaceRepository(IPersistenceManager):
    """Class for managing the persistence of places."""
    def __init__(self):
        self.places = {}
        self.next_id = 1

    def save(self, place):
        """Saves a place."""
        if not hasattr(place, 'place_id'):
            place.place_id = self.next_id
            self.next_id += 1
        self.places[place.place_id] = place

    def get(self, place_id):
        """Fetches a place."""
        return self.places.get(place_id)

    def get_all(self):
        """Fetches all places."""
        return list(self.places.values())

    def update(self, place_id, new_place_data):
        """Updates an existing place."""
        if place_id in self.places:
            place = self.places[place_id]
            place.update_place_data(new_place_data)
            self.save(place)
            return True
        return False

    def delete(self, place_id):
        """Deletes an existing place."""
        if place_id in self.places:
            del self.places[place_id]
            return True
        return False

    def setUp(self):
        self.repository = PlaceRepository()
        self.place1 = Place("Address 1", "City ID 1", 1.234, 5.678, "Host ID 1", 3, 2, 100, 4, [1, 2, 3])
        self.place2 = Place("Address 2", "City ID 2", 3.456, 7.890, "Host ID 2", 4, 3, 150, 6, [4, 5, 6])
        self.repository.save(self.place1)
        self.repository.save(self.place2)
