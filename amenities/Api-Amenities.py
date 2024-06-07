#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///amenities.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Importez le modèle Amenities du code précédent

@app.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = Amenities.query.all()
    result = []
    for amenity in amenities:
        amenity_data = {
            'id': amenity.id,
            'features': amenity.features,
            'wifi': amenity.wifi,
            'pools': amenity.pools,
            'catalog': amenity.catalog
        }
        result.append(amenity_data)
    return jsonify(result)

@app.route('/amenities', methods=['POST'])
def add_amenity():
    data = request.get_json()
    new_amenity = Amenities(features=data['features'], wifi=data['wifi'], pools=data['pools'], catalog=data['catalog'])
    db.session.add(new_amenity)
    db.session.commit()
    return jsonify({'message': 'Amenity added successfully'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
