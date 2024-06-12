#!/usr/bin/python3
# Persistence Interface

from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    """Interface for defining persistence manager methods."""

    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def get(self, entity_id):
        pass

    @abstractmethod
    def update(self, entity_id, new_data):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass

    @abstractmethod
    def get_all(self):
        pass
