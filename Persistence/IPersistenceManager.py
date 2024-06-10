#!/usr/bin/env python3


from abc import ABC, abstractmethod
from models import User, Place, City, Country


class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        pass


class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {
            'User': {},
            'Place': {},
            'Country': {},
            'City': {},
        }

    def save(self, entity):
        # Logique pour sauvegarder l'entité dans le stockage
        entity_type = type(entity).__name__
        entity_id = getattr(entity, f'{entity_type.lower()}_id')

        # Validate entity type
        if entity_type not in self.storage:
            raise ValueError(f"Unsupported entity type: {entity_type}")

        self.storage[entity_type][entity_id] = entity

        # Sauvegarder les relations si nécessaire
        if entity_type == 'Country':
            for city in entity.cities:
                self.save(city)

    def get(self, entity_id, entity_type):
        # Logique pour récupérer une entité basée sur l'ID et le type
        if entity_type not in self.storage:
            raise ValueError(f"Unsupported entity type: {entity_type}")
        return self.storage.get(entity_type, {}).get(entity_id)

    def update(self, entity):
        # Logique pour mettre à jour une entité dans le stockage
        entity_type = type(entity).__name__
        entity_id = getattr(entity, f'{entity_type.lower()}_id')

        # Validate entity type
        if entity_type not in self.storage:
            raise ValueError(f"Unsupported entity type: {entity_type}")

        if entity_id in self.storage[entity_type]:
            self.storage[entity_type][entity_id] = entity
        else:
            raise KeyError(f"{entity_type} with id {entity_id} doe not exist.")

        if entity_type == 'Country':
            for city in entity.cities:
                self.update(city)

    def delete(self, entity_id, entity_type):
        # Logique pour supprimer une entité du stockage

        # Validate entity type
        if entity_type not in self.storage:
            raise ValueError(f"Unsupported entity type: {entity_type}")

        if entity_id in self.storage.get(entity_type, {}):
            if entity_type == 'Country':
                country = self.storage[entity_type][entity_id]
                for city in country.cities:
                    if city.city_id in self.storage['City']:
                        del self.storage['City'][city.city_id]
            elif entity_type == 'City':
                for country in self.storage['Country'].values():
                    country.cities = [city for city in country.cities
                                      if city.city_id != entity_id]
            del self.storage[entity_type][entity_id]
        else:
            raise KeyError(f"{entity_type} with id {entity_id} doe not exist.")
