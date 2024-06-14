# HBnB Evolution Project

Welcome to the HBnB Evolution project! This project is inspired by AirBnB and aims to create a web application using Python and Flask.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [UML Diagram](#uml-diagram)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Dockerization](#dockerization)
- [Contributing](#contributing)
- [License](#license)

## Overview

The HBnB Evolution project is designed to help you learn how to build a web application from scratch. You will create a web application with the following components:

1. **Sketching with UML**: Designing the architecture using Unified Modeling Language (UML).
2. **Testing Our Logic**: Creating tests for the API and business logic.
3. **Building the API**: Implementing the API using Flask.
4. **File-Based Data Storage**: Starting with a file-based system for data storage.
5. **Packaging with Docker**: Containerizing the application using Docker.

## Project Structure

The project is organized into the following layers:

1. **Services Layer**: Handles all the requests and responses.
2. **Business Logic Layer**: Processes and makes decisions.
3. **Persistence Layer**: Manages data storage, initially file-based.

Key entities in our data model include Places, Users, Reviews, Amenities, Country, and City.

## UML Diagram

Here is a UML diagram representing the core entities and their relationships:

<img src ="https://github.com/Erwan2072/holbertonschool-hbnb/blob/main/ulm%20modified%20test.png">

**Entities**:

- **Place**
  - Attributes: id, name, description, address, city_id, latitude, longitude, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenities, reviews, created_at, updated_at
- **User**
  - Attributes: id, email, password, first_name, last_name, created_at, updated_at
- **Review**
  - Attributes: id, place_id, user_id, rating, comment, created_at, updated_at
- **Amenity**
  - Attributes: id, name, created_at, updated_at
- **Country**
  - Attributes: code, name
- **City**
  - Attributes: id, name, country_code, created_at, updated_at

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Erwan2072/holbertonschool-hbnb.git
   cd holbertonschool-hbnb
   ```

2. Create a virtual environment and activate it:

```
python3 -m venv venv
source venv/bin/activate

```
3. Install the dependencies:

```
pip install -r requirements.txt
```
## Usage

1. Start the Flask application:
```
flask run

```
2. The API will be available at http://127.0.0.1:5000.

## API Endpoints

### User Management
. POST /users: Create a new user.
. GET /users: Retrieve a list of all users.
. GET /users/{user_id}: Retrieve details of a specific user.
. PUT /users/{user_id}: Update an existing user.
. DELETE /users/{user_id}: Delete a user.

### Country and City Management
. GET /countries: Retrieve all pre-loaded countries.
. GET /countries/{country_code}: Retrieve details of a specific country.
. GET /countries/{country_code}/cities: Retrieve all cities in a specific country.
. POST /cities: Create a new city.
. GET /cities: Retrieve all cities.
. GET /cities/{city_id}: Retrieve details of a specific city.
. PUT /cities/{city_id}: Update an existing city.
. DELETE /cities/{city_id}: Delete a specific city.

### Amenity Management
. POST /amenities: Create a new amenity.
. GET /amenities: Retrieve a list of all amenities.
. GET /amenities/{amenity_id}: Retrieve detailed information about a specific amenity.
. PUT /amenities/{amenity_id}: Update an existing amenity.
. DELETE /amenities/{amenity_id}: Delete a specific amenity.

### Place Management
. POST /places: Create a new place.
. GET /places: Retrieve a list of all places.
. GET /places/{place_id}: Retrieve detailed information about a specific place.
. PUT /places/{place_id}: Update an existing place.
. DELETE /places/{place_id}: Delete a specific place.

### Review Management
. POST /places/{place_id}/reviews: Create a new review for a specified place.
. GET /users/{user_id}/reviews: Retrieve all reviews written by a specific user.
. GET /places/{place_id}/reviews: Retrieve all reviews for a specific place.
. GET /reviews/{review_id}: Retrieve detailed information about a specific review.
. PUT /reviews/{review_id}: Update an existing review.
. DELETE /reviews/{review_id}: Delete a specific review.

## Testing

To run the unit tests, use the following command:
```
python -m unittest discover tests

```

## Dockerization

To containerize the application:

1. Build the Docker image:
```
docker build -t hbnb-evolution .

```

2. Run the Docker container:

```
docker run -p 8001:8000 -v $(pwd)/data:/app/data --env PORT=8000 holbertonschool-hbnb

```

### Contributing
Marc Cornabas     [Grilindor](https://github.com/Grilindor)
Antonin Paillasse [Antonin-crypto](https://github.com/Antonin-crypto)
Erwan lebreton    [@Erwan2072](https://github.com/Erwan2072)

And our SWE we love :heart: Axel Goré :heart:
