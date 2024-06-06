#!/usr/bin/python3
""" test unittest for the class user"""


import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(email="test@example.com", password="1234", first_name="John", last_name="Doe")

    def test_get_email(self):
        self.assertEqual(self.user.get_email(), "test@example.com")

    def test_get_password(self):
        self.assertEqual(self.user.get_password(), "1234")

    def test_get_first_name(self):
        self.assertEqual(self.user.get_first_name(), "John")

    def test_get_last_name(self):
        self.assertEqual(self.user.get_last_name(), "Doe")

    def test_set_email(self):
        self.user.set_email("new_email@example.com")
        self.assertEqual(self.user.get_email(), "new_email@example.com")

    def test_set_password(self):
        self.user.set_password("5678")
        self.assertEqual(self.user.get_password(), "5678")

    def test_set_first_name(self):
        self.user.set_first_name("Jane")
        self.assertEqual(self.user.get_first_name(), "Jane")

    def test_set_last_name(self):
        self.user.set_last_name("Smith")
        self.assertEqual(self.user.get_last_name(), "Smith")

    def test_verify_password_correct(self):
        self.assertTrue(self.user.verify_password("1234"))

    def test_verify_password_incorrect(self):
        self.assertFalse(self.user.verify_password("5678"))

    """def test_set_invalid_email(self):
        with self.assertRaises(ValueError):
            self.user.set_email("invalid_email")

    #def test_set_invalid_password(self):
        with self.assertRaises(ValueError):
            self.user.set_password("")

    def test_set_invalid_first_name(self):
        with self.assertRaises(ValueError):
            self.user.set_first_name("")

    def test_set_invalid_last_name(self):
        with self.assertRaises(ValueError):
            self.user.set_last_name("")"""

if __name__ == "__main__":
    unittest.main()
