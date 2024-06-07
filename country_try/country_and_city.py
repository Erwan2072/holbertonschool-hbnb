#!/usr/bin/env python3
"""
class for cherch of country and city
"""


from data_country_city import european_countries, cities_dict
from data_country_city import european_countries_check, city_ceck

class Country_city:
    """ """
    def __init__(self, country = "", city = ""):
        if not isinstance(country, str):
            raise TypeError("Country must be a string.")
        if country not in european_countries:
            raise ValueError("This country is not in the list \
                             of European countries.")

        self.__country = country
        self.__city = city

        if not isinstance(city, str):
            raise TypeError("City must be a string.")
        if self.__country in cities_dict:
            available_cities = cities_dict[self.__country]
            if self.__city not in available_cities:
                raise ValueError("This city is not in the list of cities\
                                  for the selected country.")


class get_Country_city:
    """
    class who get country and city and add it to the dictionnary
    and the list if it's already in there
    """
    def __init__(self, get_country, get_city):
        if not type(get_country, str):
            raise TypeError("Country must be a string.")
        if not type(get_city, str):
            raise TypeError("City must be a string.")

        # Capitalize the country name
        self.__get_country = get_country.capitalize()
        self.__get_city = get_city

        # Check if the country is in the list of European countries
        if self.__get_country not in european_countries\
              and self.__get_country in european_countries_check:
            european_countries.append(self.__get_country)

        # Update the cities_dict with the new country if added
        if self.__get_country not in cities_dict:
            cities_dict[self.__get_country] = [self.__get_city]
        else:
            cities_dict[self.__get_country].append(self.__get_city)


