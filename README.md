HBnB Evolution Project
Welcome to the HBnB Evolution project! This project is inspired by AirBnB and aims to create a web application using Python and Flask.

Table of Contents
Overview
Project Structure
UML Diagram
Installation
Usage
API Endpoints
Testing
Dockerization
Contributing
License
Overview
The HBnB Evolution project is designed to help you learn how to build a web application from scratch. You will create a web application with the following components:

Sketching with UML: Designing the architecture using Unified Modeling Language (UML).
Testing Our Logic: Creating tests for the API and business logic.
Building the API: Implementing the API using Flask.
File-Based Data Storage: Starting with a file-based system for data storage.
Packaging with Docker: Containerizing the application using Docker.
Project Structure
The project is organized into the following layers:

Services Layer: Handles all the requests and responses.
Business Logic Layer: Processes and makes decisions.
Persistence Layer: Manages data storage, initially file-based.
Key entities in our data model include Places, Users, Reviews, Amenities, Country, and City.

UML Diagram
Here is a UML diagram representing the core entities and their relationships:


Entities:

Place
Attributes: id, name, description, address, city_id, latitude, longitude, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenities, reviews, created_at, updated_at
User
Attributes: id, email, password, first_name, last_name, created_at, updated_at
Review
Attributes: id, place_id, user_id, rating, comment, created_at, updated_at
Amenity
Attributes: id, name, created_at, updated_at
Country
Attributes: code, name
City
Attributes: id, name, country_code, created_at, updated_at
Installation
Clone the repository:

bash
Copier le code
git clone https://github.com/yourusername/holbertonschool-hbnb.git
cd holbertonschool-hbnb
Create a virtual environment and activate it:

bash
Copier le code
python3 -m venv venv
source venv/bin/activate
Install the dependencies:

bash
Copier le code
pip install -r requirements.txt
Usage
Start the Flask application:

bash
Copier le code
flask run
The API will be available at http://127.0.0.1:5000.

API Endpoints
User Management
POST /users: Create a new user.
GET /users: Retrieve a list of all users.
GET /users/{user_id}: Retrieve details of a specific user.
PUT /users/{user_id}: Update an existing user.
DELETE /users/{user_id}: Delete a user.
Country and City Management
GET /countries: Retrieve all pre-loaded countries.
GET /countries/{country_code}: Retrieve details of a specific country.
GET /countries/{country_code}/cities: Retrieve all cities in a specific country.
POST /cities: Create a new city.
GET /cities: Retrieve all cities.
GET /cities/{city_id}: Retrieve details of a specific city.
PUT /cities/{city_id}: Update an existing city.
DELETE /cities/{city_id}: Delete a specific city.
Amenity Management
POST /amenities: Create a new amenity.
GET /amenities: Retrieve a list of all amenities.
GET /amenities/{amenity_id}: Retrieve detailed information about a specific amenity.
PUT /amenities/{amenity_id}: Update an existing amenity.
DELETE /amenities/{amenity_id}: Delete a specific amenity.
Place Management
POST /places: Create a new place.
GET /places: Retrieve a list of all places.
GET /places/{place_id}: Retrieve detailed information about a specific place.
PUT /places/{place_id}: Update an existing place.
DELETE /places/{place_id}: Delete a specific place.
Review Management
POST /places/{place_id}/reviews: Create a new review for a specified place.
GET /users/{user_id}/reviews: Retrieve all reviews written by a specific user.
GET /places/{place_id}/reviews: Retrieve all reviews for a specific place.
GET /reviews/{review_id}: Retrieve detailed information about a specific review.
PUT /reviews/{review_id}: Update an existing review.
DELETE /reviews/{review_id}: Delete a specific review.
Testing
To run the unit tests, use the following command:

bash
Copier le code
python -m unittest discover tests
Dockerization
To containerize the application:

Build the Docker image:

bash
Copier le code
docker build -t hbnb-evolution .
Run the Docker container:

bash
Copier le code
docker run -p 5000:5000 -v $(pwd)/data:/app/data --env PORT=5000 hbnb-evolution
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License.


