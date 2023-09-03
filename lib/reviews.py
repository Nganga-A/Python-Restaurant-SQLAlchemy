from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')
    
    # represent the class instances
    def __repr__(self):
        return (f"Customer({self.customer_id}) | Restaurant({self.restaurant_id}) | start-rating({self.star_rating}) |"
                f" {self.description}: {self.star_rating} stars\n")


    def review_customer(self):
        # Return the Customer instance for this review
        return self.customer

    def review_restaurant(self):
        # Return the Restaurant instance for this review
        return self.restaurant

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."
