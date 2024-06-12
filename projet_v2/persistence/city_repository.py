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
        if not isinstance(city, City):
            raise ValueError("Object is not an instance of City")

        if city.city_id is None:
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
        city = self.cities.get(city_id)
        if city:
            city.update_from_dict(new_city_data)
            return True
        return False

    def delete(self, city_id):
        """Deletes an existing city."""
        if city_id in self.cities:
            del self.cities[city_id]
            return True
        return False
