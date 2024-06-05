class User:
    def __init__(self, email, password, first_name, last_name):
        self._email = email
        self._password = password
        self._first_name = first_name
        self._last_name = last_name

    # Getters
    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    # Setters
    def set_email(self, email):
        self._email = email

    def set_password(self, password):
        self._password = password

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    # Method to verify password
    def verify_password(self, password):
        return self._password == password
