#!/usr/bin/env python3
"""
class for cherch of country and city
"""


from data_country_city import european_countries, cities_dict


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

# Test de la classe Country_city avec des données d'entrée
"""
try:
    test_city = Country_city("France", "Paris")
    print("Country:", test_city._Country_city__country)
    print("City:", test_city._Country_city__city)
except Exception as e:
    print("An error occurred:", e)
"""


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
        if self.__get_country not in european_countries:
            european_countries.append(self.__get_country)

        # Update the cities_dict with the new country if added
        if self.__get_country not in cities_dict:
            cities_dict[self.__get_country] = [self.__get_city]
        else:
            cities_dict[self.__get_country].append(self.__get_city)
