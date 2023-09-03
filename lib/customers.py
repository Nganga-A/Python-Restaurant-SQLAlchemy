from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship('Review', back_populates='customer')
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')
    
    # represent the class instances
    def __repr__(self):
        return f'{self.id}: {self.last_name}, {self.first_name}\n'

    def customer_reviews(self):
        # Return a collection of all the reviews that the Customer has left
        return self.reviews

    def customer_restaurants(self):
        # Return a collection of all the restaurants that the Customer has reviewed
        return self.restaurants

    def full_name(self):
        # Return the full name of the customer, with the first name and last name concatenated, Western style
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        # Return the restaurant instance that has the highest star rating from this customer
        reviews = sorted(self.reviews, key=lambda r: r.star_rating, reverse=True)
        if reviews:
            return reviews[0].restaurant

    def add_review(self, restaurant, rating):
        # Create a new review for the restaurant with the given rating
        new_review = Review(
            restaurant_id=restaurant.id,
            customer_id=self.id,
            star_rating=rating
        )
        session.add(new_review)
        session.commit()
        return new_review

    def delete_reviews(self, restaurant):
        # Remove all reviews by this customer for a specific restaurant
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()
        print(f'{self.first_name}\'s reviews for \'{restaurant.name} restaurant\' have been successfully deleted!')