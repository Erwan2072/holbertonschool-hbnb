#!/usr/bin/python3
# API for managing reviews

from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager

api = Namespace('reviews', description='Operations related to reviews')
data_manager = DataManager()

# Model definition for a Review
review_model = api.model('Review', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'place_id': fields.Integer(required=True, description='Place ID'),
    'rating': fields.Integer(required=True, description='Rating'),
    'comment': fields.String(description='Comment')
})

@api.route('/')
class Reviews(Resource):
    @api.marshal_list_with(review_model)
    def get(self):
        """Fetch all reviews."""
        return data_manager.get_all_reviews()

    @api.expect(review_model)
    @api.response(201, 'Review created successfully')
    @api.response(400, 'Invalid request')
    def post(self):
        """Create a new review."""
        new_review_data = request.json
        review_id = data_manager.save_review(new_review_data)
        return {'message': 'Review created successfully', 'review_id': review_id}, 201

@api.route('/<int:review_id>')
class ReviewResource(Resource):
    @api.marshal_with(review_model)
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Fetch a review by its ID."""
        review_data = data_manager.get_review(review_id)
        if review_data:
            return review_data
        else:
            api.abort(404, "Review not found")

    @api.response(204, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete an existing review."""
        if data_manager.delete_review(review_id):
            return '', 204
        else:
            api.abort(404, "Review not found")

    @api.expect(review_model)
    @api.response(204, 'Review updated successfully')
    @api.response(400, 'Invalid request')
    @api.response(404, 'Review not found')
    def put(self, review_id):
        """Update an existing review."""
        new_review_data = request.json
        if data_manager.update_review(review_id, new_review_data):
            return '', 204
        else:
            api.abort(404, "Review not found")
