#Lets define the SQLAlchemy models
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref, declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///restaurants.db') #creates a SQLAlchemy engine that connects to our db
Session = sessionmaker(bind=engine) #creates a Session class to interact with the database and is bound to the engine you created
session = Session()
Base = declarative_base()
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


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id')) #Foreign key relationship with Restaurant
    customer_id = Column(Integer, ForeignKey('customers.id'))      # Foreign key relationship with Customer
    restaurant = relationship('Restaurant', back_populates='reviews') #one-to-many relationship between restaurant and reviews
    customer = relationship('Customer', back_populates='reviews') #one-to-many relationship between customer and reviews


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)  
    first_name = Column(String)              
    last_name = Column(String)              
    reviews = relationship('Review', back_populates='customer')
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')
