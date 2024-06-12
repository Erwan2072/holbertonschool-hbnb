#!/usr/bin/python3
# Persistence for cities

from model.city import City
from persistence.ipersistence_manager import IPersistenceManager

class CityRepository(IPersistenceManager):
    """Class for managing the persistence of cities."""
    def __init__(self):
        self.cities = {}
        self.next_id = 1

    def save(self, city):
        """Saves a city."""
        if not hasattr(city, 'city_id'):
            city.city_id = self.next_id
            self.next_id += 1
        self.cities[city.city_id] = city

    def get(self, city_id):
        """Fetches a city."""
        return self.cities.get(city_id)

    def get_all(self):
        """Fetches all cities."""
        return list(self.cities.values())

    def update(self, city_id, new_city_data):
        """Updates an existing city."""
        if city_id in self.cities:
            city = self.cities[city_id]
            for key, value in new_city_data.items():
                setattr(city, key, value)
            self.save(city)
            return True
        return False

    def delete(self, city_id):
        """Deletes an existing city."""
        if city_id in self.cities:
            del self.cities[city_id]
            return True
        return False
