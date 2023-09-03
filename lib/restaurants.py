from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('Review', back_populates='restaurant')
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')

        # represent the class instances
    def __repr__(self):
        return f'{self.name} Restaurant - Price: ${self.price}.00\n'

    def restaurant_reviews(self):
        # Return a collection of all the reviews for this restaurant
        return self.reviews

    def restaurant_customers(self):
        # Return a collection of all the customers who reviewed the restaurant
        return self.customers

    @classmethod
    def fanciest_restaurant(cls):
        # Return the restaurant instance with the highest price
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        # Return a list of strings with all the reviews for this restaurant
        reviews = []
        for review in self.reviews:
            reviews.append(f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars.")
        return reviews
