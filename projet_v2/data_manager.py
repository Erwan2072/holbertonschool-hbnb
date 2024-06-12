#!/usr/bin/python3
"""Data manager for the application."""

from persistence.amenity_repository import AmenityRepository
from persistence.city_repository import CityRepository
from persistence.country_repository import CountryRepository
from persistence.place_repository import PlaceRepository
from persistence.review_repository import ReviewRepository
from persistence.user_repository import UserRepository
from model.amenity import Amenity
from model.city import City
from model.country import Country
from model.place import Place
from model.review import Review
from model.user import User


class DataManager:
    """Class to manage CRUD operations for various entities."""

    def __init__(self):
        """Initialize repositories for all entities."""
        self.place_repository = PlaceRepository()
        self.user_repository = UserRepository()
        self.review_repository = ReviewRepository()
        self.amenity_repository = AmenityRepository()
        self.country_repository = CountryRepository()
        self.city_repository = CityRepository()

    # Methods for Place
    def save_place(self, place_data):
        """
        Save a new place to the repository.

        Args:
            place_data (dict): Data for the new place.

        Returns:
            str: The ID of the saved place.
        """
        place = Place(**place_data)
        self.place_repository.save(place)
        return place.place_id

    def get_place(self, place_id):
        """
        Retrieve a place by its ID.

        Args:
            place_id (str): The ID of the place.

        Returns:
            Place: The retrieved place object.
        """
        return self.place_repository.get(place_id)

    def update_place(self, place_id, new_data):
        """
        Update a place with new data.

        Args:
            place_id (str): The ID of the place to update.
            new_data (dict): The new data for the place.

        Returns:
            Place: The updated place object.
        """
        return self.place_repository.update(place_id, new_data)

    def delete_place(self, place_id):
        """
        Delete a place by its ID.

        Args:
            place_id (str): The ID of the place to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        return self.place_repository.delete(place_id)

    def get_all_places(self):
        """
        Retrieve all places.

        Returns:
            list: A list of all place objects.
        """
        return self.place_repository.get_all()

    # Methods for User
    def save_user(self, user_data):
        """
        Save a new user to the repository.

        Args:
            user_data (dict): Data for the new user.

        Returns:
            str: The ID of the saved user.
        """
        user = User(**user_data)
        self.user_repository.save(user)
        return user.user_id

    def get_user(self, user_id):
        """
        Retrieve a user by its ID.

        Args:
            user_id (str): The ID of the user.

        Returns:
            User: The retrieved user object.
        """
        return self.user_repository.get(user_id)

    def update_user(self, user_id, new_data):
        """
        Update a user with new data.

        Args:
            user_id (str): The ID of the user to update.
            new_data (dict): The new data for the user.

        Returns:
            User: The updated user object.
        """
        return self.user_repository.update(user_id, new_data)

    def delete_user(self, user_id):
        """
        Delete a user by its ID.

        Args:
            user_id (str): The ID of the user to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        return self.user_repository.delete(user_id)

    def get_all_users(self):
        """
        Retrieve all users.

        Returns:
            list: A list of all user objects.
        """
        return self.user_repository.get_all()

    # Methods for Review
    def save_review(self, review_data):
        """
        Save a new review to the repository.

        Args:
            review_data (dict): Data for the new review.

        Returns:
            str: The ID of the saved review.
        """
        review = Review(**review_data)
        self.review_repository.save(review)
        return review.review_id

    def get_review(self, review_id):
        """
        Retrieve a review by its ID.

        Args:
            review_id (str): The ID of the review.

        Returns:
            Review: The retrieved review object.
        """
        return self.review_repository.get(review_id)

    def update_review(self, review_id, new_data):
        """
        Update a review with new data.

        Args:
            review_id (str): The ID of the review to update.
            new_data (dict): The new data for the review.

        Returns:
            Review: The updated review object.
        """
        return self.review_repository.update(review_id, new_data)

    def delete_review(self, review_id):
        """
        Delete a review by its ID.

        Args:
            review_id (str): The ID of the review to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        return self.review_repository.delete(review_id)

    def get_all_reviews(self):
        """
        Retrieve all reviews.

        Returns:
            list: A list of all review objects.
        """
        return self.review_repository.get_all()

    # Methods for Amenity
    def save_amenity(self, amenity_data):
        """
        Save a new amenity to the repository.

        Args:
            amenity_data (dict): Data for the new amenity.

        Returns:
            str: The ID of the saved amenity.
        """
        amenity = Amenity(**amenity_data)
        self.amenity_repository.save(amenity)
        return amenity.amenity_id

    def get_amenity(self, amenity_id):
        """
        Retrieve an amenity by its ID.

        Args:
            amenity_id (str): The ID of the amenity.

        Returns:
            Amenity: The retrieved amenity object.
        """
        return self.amenity_repository.get(amenity_id)

    def update_amenity(self, amenity_id, new_data):
        """
        Update an amenity with new data.

        Args:
            amenity_id (str): The ID of the amenity to update.
            new_data (dict): The new data for the amenity.

        Returns:
            Amenity: The updated amenity object.
        """
        return self.amenity_repository.update(amenity_id, new_data)

    def delete_amenity(self, amenity_id):
        """
        Delete an amenity by its ID.

        Args:
            amenity_id (str): The ID of the amenity to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        return self.amenity_repository.delete(amenity_id)

    def get_all_amenities(self):
        """
        Retrieve all amenities.

        Returns:
            list: A list of all amenity objects.
        """
        return self.amenity_repository.get_all()

    # Methods for Country
    def save_country(self, country_data):
        """
        Save a new country to the repository.

        Args:
            country_data (dict): Data for the new country.

        Returns:
            str: The ID of the saved country.
        """
        country = Country(**country_data)
        self.country_repository.save(country)
        return country.country_id

    def get_country(self, country_id):
        """
        Retrieve a country by its ID.

        Args:
            country_id (str): The ID of the country.

        Returns:
            Country: The retrieved country object.
        """
        return self.country_repository.get(country_id)

    def update_country(self, country_id, new_data):
        """
        Update a country with new data.

        Args:
            country_id (str): The ID of the country to update.
            new_data (dict): The new data for the country.

        Returns:
            Country: The updated country object.
        """
        return self.country_repository.update(country_id, new_data)

    def delete_country(self, country_id):
        """
        Delete a country by its ID.

        Args:
            country_id (str): The ID of the country to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        return self.country_repository.delete(country_id)

    def get_all_countries(self):
        """
        Retrieve all countries.

        Returns:
            list: A list of all country objects.
        """
        return self.country_repository.get_all()

    # Methods for City
    def save_city(self, city_data):
        """
        Save a new city to the repository.

        Args:
            city_data (dict): Data for the new city.

        Returns:
            str: The ID of the saved city.
        """
        city = City(**city_data)
        self.city_repository.save(city)
        return city.city_id

    def get_city(self, city_id):
        """
        Retrieve a city by its ID.

        Args:
            city_id (str): The ID of the city.

        Returns:
            City: The retrieved city object.
        """
        return self.city_repository.get(city_id)

    def update_city(self, city_id, new_data):
        """
        Update a city with new data.

        Args:
            city_id (str): The ID of the city to update.
            new_data (dict): The new data for the city.

        Returns:
            City: The updated city object.
        """
        return self.city_repository.update(city_id, new_data)

    def delete_city(self, city_id):
        """
        Delete a city by its ID.

        Args:
            city_id (str): The ID of the city to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        return self.city_repository.delete(city_id)

    def get_all_cities(self):
        """
        Retrieve all cities.

        Returns:
            list: A list of all city objects.
        """
        return self.city_repository.get_all()
