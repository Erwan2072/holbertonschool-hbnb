#!/usr/bin/env python3v


class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class Place:
    def __init__(self, place_id, name, location):
        self.place_id = place_id
        self.name = name
        self.location = location

class City:
    def __init__(self, city_id, name, population, country=None):
        self.city_id = city_id
        self.name = name
        self.population = population
        self.country = country

class Country:
    def __init__(self, country_id, name, population):
        self.country_id = country_id
        self.name = name
        self.population = population
        self.cities = []

    def add_city(self, city):
        if city not in self.cities:
            self.cities.append(city)
            city.country = self
