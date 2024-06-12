#!/usr/bin/python3
# API for managing reviews

from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager

ns = Namespace('reviews', description='Operations related to reviews')
data_manager = DataManager()

# Model definition for a Review
review_model = ns.model('Review', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'place_id': fields.Integer(required=True, description='Place ID'),
    'rating': fields.Integer(required=True, description='Rating'),
    'comment': fields.String(description='Comment')
})

@ns.route('/')
class Reviews(Resource):
    @ns.marshal_list_with(review_model)
    def get(self):
        """Fetch all reviews."""
        return data_manager.get_all_reviews()

    @ns.expect(review_model)
    @ns.response(201, 'Review created successfully')
    @ns.response(400, 'Invalid request')
    def post(self):
        """Create a new review."""
        new_review_data = request.json
        review_id = data_manager.save_review(new_review_data)
        return {'message': 'Review created successfully', 'review_id': review_id}, 201

@ns.route('/<int:review_id>')
class ReviewResource(Resource):
    @ns.marshal_with(review_model)
    @ns.response(404, 'Review not found')
    def get(self, review_id):
        """Fetch a review by its ID."""
        review_data = data_manager.get_review(review_id)
        if review_data:
            return review_data
        else:
            ns.abort(404, "Review not found")

    @ns.response(204, 'Review deleted successfully')
    @ns.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete an existing review."""
        if data_manager.delete_review(review_id):
            return '', 204
        else:
            ns.abort(404, "Review not found")

    @ns.expect(review_model)
    @ns.response(204, 'Review updated successfully')
    @ns.response(400, 'Invalid request')
    @ns.response(404, 'Review not found')
    def put(self, review_id):
        """Update an existing review."""
        new_review_data = request.json
        if data_manager.update_review(review_id, new_review_data):
            return '', 204
        else:
            ns.abort(404, "Review not found")