import unittest
from models import User, Place, City, Country
from IPersistenceManager import DataManager

class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.data_manager = DataManager()

        self.user = User(user_id=1, name="Alice", email="alice@example.com")
        self.user2 = User(user_id=2, name="Bob", email="bob@example.com")
        self.place = Place(place_id=1, name="Central Park", location="NYC")
        self.place2 = Place(place_id=2, name="Eiffel Tower", location="Paris")
        self.city = City(city_id=1, name="Paris", population=2140000)
        self.city2 = City(city_id=2, name="Lyon", population=500000)
        self.city3 = City(city_id=3, name="Marseille", population=861635)
        self.country = Country(country_id=1, name="France", population=67000000)
        self.country2 = Country(country_id=2, name="USA", population=331000000)

    def test_save_and_get_user(self):
        self.data_manager.save(self.user)
        retrieved_user = self.data_manager.get(1, 'User')
        self.assertEqual(retrieved_user.name, "Alice")
        self.assertEqual(retrieved_user.email, "alice@example.com")

    def test_save_and_get_place(self):
        self.data_manager.save(self.place)
        retrieved_place = self.data_manager.get(1, 'Place')
        self.assertEqual(retrieved_place.name, "Central Park")
        self.assertEqual(retrieved_place.location, "NYC")

    def test_save_and_get_city(self):
        self.data_manager.save(self.city)
        retrieved_city = self.data_manager.get(1, 'City')
        self.assertEqual(retrieved_city.name, "Paris")
        self.assertEqual(retrieved_city.population, 2140000)

    def test_save_and_get_country(self):
        self.country.add_city(self.city)
        self.data_manager.save(self.country)
        retrieved_country = self.data_manager.get(1, 'Country')
        retrieved_city = self.data_manager.get(1, 'City')

        self.assertEqual(retrieved_country.name, "France")
        self.assertEqual(len(retrieved_country.cities), 1)
        self.assertEqual(retrieved_country.cities[0].name, "Paris")
        self.assertEqual(retrieved_city.name, "Paris")

    def test_update_user(self):
        self.data_manager.save(self.user)
        self.user.name = "Alice Smith"
        self.data_manager.update(self.user)
        updated_user = self.data_manager.get(1, 'User')
        self.assertEqual(updated_user.name, "Alice Smith")

    def test_delete_user(self):
        self.data_manager.save(self.user)
        self.data_manager.delete(1, 'User')
        deleted_user = self.data_manager.get(1, 'User')
        self.assertIsNone(deleted_user)

    def test_delete_country_with_cities(self):
        self.country.add_city(self.city)
        self.data_manager.save(self.country)
        self.data_manager.delete(1, 'Country')
        deleted_country = self.data_manager.get(1, 'Country')
        deleted_city = self.data_manager.get(1, 'City')
        self.assertIsNone(deleted_country)
        self.assertIsNone(deleted_city)

    # Tests supplémentaires
    def test_save_and_get_multiple_users(self):
        self.data_manager.save(self.user)
        self.data_manager.save(self.user2)
        retrieved_user1 = self.data_manager.get(1, 'User')
        retrieved_user2 = self.data_manager.get(2, 'User')
        self.assertEqual(retrieved_user1.name, "Alice")
        self.assertEqual(retrieved_user2.name, "Bob")

    def test_update_country_with_cities(self):
        self.country.add_city(self.city)
        self.data_manager.save(self.country)
        self.city.population = 2200000
        self.data_manager.update(self.country)
        updated_city = self.data_manager.get(1, 'City')
        self.assertEqual(updated_city.population, 2200000)

    def test_delete_non_existent_entity(self):
        with self.assertRaises(RuntimeError) as context:
            self.data_manager.delete(99, 'User')
        self.assertIn('User with id 99 does not exist.', str(context.exception))

    def test_save_and_delete_city_with_country(self):
        self.country.add_city(self.city)
        self.country.add_city(self.city2)
        self.data_manager.save(self.country)
        self.data_manager.delete(2, 'City')
        deleted_city = self.data_manager.get(2, 'City')
        self.assertIsNone(deleted_city)
        remaining_country = self.data_manager.get(1, 'Country')
        self.assertEqual(len(remaining_country.cities), 1)

    def test_delete_all_entities(self):
        self.data_manager.save(self.user)
        self.data_manager.save(self.place)
        self.data_manager.save(self.city)
        self.data_manager.save(self.country)
        self.data_manager.delete(1, 'User')
        self.data_manager.delete(1, 'Place')
        self.data_manager.delete(1, 'City')
        self.data_manager.delete(1, 'Country')
        self.assertIsNone(self.data_manager.get(1, 'User'))
        self.assertIsNone(self.data_manager.get(1, 'Place'))
        self.assertIsNone(self.data_manager.get(1, 'City'))
        self.assertIsNone(self.data_manager.get(1, 'Country'))

    def test_add_city_to_existing_country(self):
        self.data_manager.save(self.country)
        self.data_manager.save(self.city)
        self.country.add_city(self.city)
        self.data_manager.update(self.country)
        updated_country = self.data_manager.get(1, 'Country')
        self.assertEqual(len(updated_country.cities), 1)
        self.assertEqual(updated_country.cities[0].name, "Paris")

    def test_update_cities_in_country(self):
        self.country.add_city(self.city)
        self.data_manager.save(self.country)
        self.city.name = "New Paris"
        self.data_manager.update(self.city)
        updated_city = self.data_manager.get(1, 'City')
        updated_country = self.data_manager.get(1, 'Country')
        self.assertEqual(updated_city.name, "New Paris")
        self.assertEqual(updated_country.cities[0].name, "New Paris")

    def test_manage_multiple_countries_and_cities(self):
        self.country.add_city(self.city)
        self.country2.add_city(self.city2)
        self.data_manager.save(self.country)
        self.data_manager.save(self.country2)
        self.assertEqual(len(self.data_manager.get(1, 'Country').cities), 1)
        self.assertEqual(len(self.data_manager.get(2, 'Country').cities), 1)

    def test_delete_city_before_country(self):
        self.country.add_city(self.city)
        self.data_manager.save(self.country)
        self.data_manager.delete(1, 'City')
        self.assertIsNone(self.data_manager.get(1, 'City'))
        self.data_manager.delete(1, 'Country')
        self.assertIsNone(self.data_manager.get(1, 'Country'))

    def test_delete_user_and_place_linked_to_city(self):
        self.data_manager.save(self.city)
        self.data_manager.save(self.user)
        self.data_manager.save(self.place)
        self.data_manager.delete(1, 'User')
        self.data_manager.delete(1, 'Place')
        self.assertIsNone(self.data_manager.get(1, 'User'))
        self.assertIsNone(self.data_manager.get(1, 'Place'))

    def test_save_and_get_user_with_same_id(self):
        self.data_manager.save(self.user)
        user_with_same_id = User(user_id=1, name="Charlie", email="charlie@example.com")
        self.data_manager.save(user_with_same_id)
        retrieved_user = self.data_manager.get(1, 'User')
        self.assertEqual(retrieved_user.name, "Charlie")
        self.assertEqual(retrieved_user.email, "charlie@example.com")




if __name__ == '__main__':
    unittest.main()
