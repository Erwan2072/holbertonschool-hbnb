#!/usr/bin/env python3

from flask import Flask, request, jsonify
from persistence import Review, Session

app = Flask(__name__)


@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    if request.method == 'POST':
        data = request.json
        new_review = Review(feedbacks=data['feedbacks'], rating=data['rating'])

        session = Session()
        session.add(new_review)
        session.commit()
        session.close()

        return jsonify({'message': 'Review added successfully'}), 201
    else:
        session = Session()
        reviews = session.query(Review).all()
        session.close()

        result = [{'feedbacks': review.feedbacks, 'rating': review.rating}
                  for review in reviews]
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
