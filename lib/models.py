#Lets define the SQLAlchemy models
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# base class for declarative models
Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('Review', back_populates='restaurant')    #one-to-many relationship between a restaurant and its reviews
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants') #many-to-many relationship between a restaurants and its customers
    #reviews serving as a secondary association table.
    def __repr__(self):
        return f'{self.name} Restaurant - Price: ${self.price}.00'



class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id')) #Foreign key relationship with Restaurant
    customer_id = Column(Integer, ForeignKey('customers.id'))      # Foreign key relationship with Customer
    restaurant = relationship('Restaurant', back_populates='reviews') #one-to-many relationship between restaurant and reviews
    customer = relationship('Customer', back_populates='reviews') #one-to-many relationship between customer and reviews

    def __repr__(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."



class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)  
    first_name = Column(String)              
    last_name = Column(String)              
    restaurants = relationship("Restaurant", secondary='reviews', back_populates='customers')
    
    def __repr__(self):
        return f'{self.id}: {self.last_name}, {self.first_name}'

