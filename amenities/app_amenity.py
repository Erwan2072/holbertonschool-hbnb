#!/usr/bin/python3

from flask import Flask
from api_amenity import amenity_api

app = Flask(__name__)

# Register the amenity API blueprint
app.register_blueprint(amenity_api)

if __name__ == '__main__':
    app.run(debug=True)
