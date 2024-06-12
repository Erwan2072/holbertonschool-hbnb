#!/usr/bin/python3
"""Model for representing reviews."""

class Review:
    """Class representing a review."""
    def __init__(self, user_id, place_id, rating, comment):
        self.review_id = None
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment

    def to_dict(self):
        """Returns the review data as a dictionary."""
        return {
            'review_id': self.review_id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': self.rating,
            'comment': self.comment
        }
