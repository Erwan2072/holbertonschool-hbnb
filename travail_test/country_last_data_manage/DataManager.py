#!/usr/bin/env python3

import json
import os
from datetime import datetime
from models_city import City
from models_country import Country
from IPersistenceManager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self, city_file='cities.json', country_file='countries.json'):
        self.city_file = city_file
        self.country_file = country_file
        self.load_data()

    def load_data(self):
        self.cities = self._load_from_file(self.city_file, City)
        self.countries = self._load_from_file(self.country_file, Country)

    def _load_from_file(self, file_path, entity_class):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
                return [entity_class(**item) for item in data]
        return []

    def _save_to_file(self, file_path, data):
        with open(file_path, 'w') as f:
            json.dump([item.__dict__ for item in data], f)

    def save(self, entity):
        if isinstance(entity, City):
            self.cities.append(entity)
            self._save_to_file(self.city_file, self.cities)
        elif isinstance(entity, Country):
            self.countries.append(entity)
            self._save_to_file(self.country_file, self.countries)

    def get(self, entity_id, entity_type):
        if entity_type == 'city':
            return next((city for city in self.cities if city.id == entity_id), None)
        elif entity_type == 'country':
            return next((country for country in self.countries if country.code == entity_id), None)

    def update(self, entity):
        if isinstance(entity, City):
            index = next((i for i, city in enumerate(self.cities) if city.id == entity.id), None)
            if index is not None:
                self.cities[index] = entity
                self._save_to_file(self.city_file, self.cities)
        elif isinstance(entity, Country):
            index = next((i for i, country in enumerate(self.countries) if country.code == entity.code), None)
            if index is not None:
                self.countries[index] = entity
                self._save_to_file(self.country_file, self.countries)

    def delete(self, entity_id, entity_type):
        if entity_type == 'city':
            self.cities = [city for city in self.cities if city.id != entity_id]
            self._save_to_file(self.city_file, self.cities)
        elif entity_type == 'country':
            self.countries = [country for country in self.countries if country.code != entity_id]
            self._save_to_file(self.country_file, self.countries)
