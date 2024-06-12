#!/usr/bin/python3
# Persistence for countries

from model.country import Country
from persistence.ipersistence_manager import IPersistenceManager

class CountryRepository(IPersistenceManager):
    """Class for managing the persistence of countries."""
    def __init__(self):
        self.countries = {}
        self.next_id = 1

    def save(self, country):
        """Saves a country."""
        if not hasattr(country, 'country_id'):
            country.country_id = self.next_id
            self.next_id += 1
        self.countries[country.country_id] = country

    def get(self, country_id):
        """Fetches a country."""
        return self.countries.get(country_id)

    def get_all(self):
        """Fetches all countries."""
        return list(self.countries.values())

    def update(self, country_id, new_country_data):
        """Updates an existing country."""
        if country_id in self.countries:
            country = self.countries[country_id]
            for key, value in new_country_data.items():
                setattr(country, key, value)
            self.save(country)
            return True
        return False

    def delete(self, country_id):
        """Deletes an existing country."""
        if country_id in self.countries:
            del self.countries[country_id]
            return True
        return False
