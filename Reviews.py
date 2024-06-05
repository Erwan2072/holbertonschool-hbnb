#!/usr/bin/env python3
"""HBnB Evolution: Part 1"""

class Review:
    """
    A class to represent a review with feedback and rating.

    Attributes:
        feedbacks (str): The feedback provided in the review.
        rating (str): The rating provided in the review.
    """

    def __init__(self, feedbacks: str, rating: str):
        """
        Constructs all the necessary attributes for the review object.

        Args:
            feedbacks (str): The feedback provided in the review.
            rating (str): The rating provided in the review.
        """
        self.feedbacks = feedbacks
        self.rating = rating

    @property
    def feedbacks(self):
        return self._feedbacks

    @feedbacks.setter
    def feedbacks(self, feedbacks: str):
        if not isinstance(feedbacks, str) or not feedbacks.strip():
            raise ValueError("Feedbacks must be a non-empty string")
        self._feedbacks = feedbacks

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating: str):
        if not isinstance(rating, str) or not rating.strip():
            raise ValueError("Rating must be a non-empty string")
        self._rating = rating

    def __str__(self):
        """
        Returns a string representation of the review.

        Returns:
            str: A string containing the feedback and rating.
        """
        return "Feedbacks: {}, Rating: {}".format(self.feedbacks, self.rating)
