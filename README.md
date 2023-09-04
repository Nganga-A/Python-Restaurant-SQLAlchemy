# Python-Restaurant-SQLAlchemy ![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
A simple review system for restaurants, customers and their reviews

## Overview
This project is a Python-based application for managing restaurant reviews. It utilizes SQLAlchemy to interact with a SQLite database to store information about restaurants, customers, and reviews.

## Features
-Add and view restaurant information.
-Add and view customer details.
-Leave reviews for restaurants.
-View the highest-rated restaurant for each customer.
-Display all reviews for a specific restaurant.
-Delete reviews by a customer for a particular restaurant.

## Topics
-SQLAlchemy Migrations

-SQLAlchemy Relationships

-Class and Instance Methods

-SQLAlchemy Querying

## Project Composition
We have three models: `Restaurant`, `Review`, and `Customer`.
For our purposes, a `Restaurant` has many `Review` s, a `Customer` has many
`Review` s, and a `Review` belongs to a `Restaurant` and to a `Customer`.
`Restaurant` - `Customer` is a many to many relationship.

```
project_folder/
    ├── models.py              # Define database models
    ├── seeds.py               # Seed data for testing
    ├── main.py                # Main application logic
    ├── restaurant.db          # Database configuration and session management
    ├── customers.py           # Implement Customer class methods
    ├── restaurants.py         # Implement Restaurant class methods
    ├── reviews.py             # Implement Review class methods

```

# Getting Started

## Project Setup

1. Clone the repository
```
git clone git@github.com:Nganga-A/Python-Restaurant-SQLAlchemy.git
```

2. Install required dependencies
```
cd into the project directory
```

3. Run the main script 

## Example Usage
```python
#!/usr/bin/env python3

from models import *
from restaurants import RestaurantMethods
from customers import CustomerMethods
from reviews import ReviewMethods

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    # import ipdb; ipdb.set_trace()

    '''----------------------------------- R E T A U R A N T -------------------------------------------'''
    restaurant1 = session.query(Restaurant).first()

    # Create an instance of RestaurantMethods
    restaurant_methods = RestaurantMethods(restaurant1)

    # return details of all the restaurant instance reviews
    print('\n-------------------------ALL REVIEWS-------------------------')
    print(restaurant_methods.all_reviews())

    print()
    print('\n------------------------- RESTAURANT SECTION ------------------------')
    print('------------------------- Restaurant One -----------------------------')
    print(restaurant_methods)

    # return all the restaurant instance reviews
    print("\n-------------------- Restaurant's Review --------------------")
    print(restaurant_methods.restaurant_reviews())

    # return all the customers who have reviewed this restaurant
    print("\n-------------------- Restaurant's Customers --------------------")
    print(restaurant_methods.restaurant_customers())

    print('\n------------------------- Fanciest Restaurant -------------------------')
    # returns the fanciest(most-expensive) restaurant of all the restaurants
    print(restaurant_methods.fanciest_restaurant())



    
    '''------------------------------------ C U S T O M E R ---------------------------------------------'''
    customer1 = session.query(Customer).first()
    customer_methods = CustomerMethods(customer1)
    
    print()
    print('\n------------------------- CUSTOMER SECTION ------------------------')
    print('------------------------ Customer One ---------------------------')
    print(customer_methods)

    print("\n------------------------ Customer's Reviews ------------------------")
    # returns the customer reviews
    print(customer_methods.customer_reviews)

    print("\n-------------------- Customer's Reviewed Restaurants --------------------")
    # returns the customer reviews
    print(customer_methods.customer_restaurants)

    print("\n-------------------------- Customer's Full Name -------------------------")
    # return customer full_name
    print(customer_methods.full_name)

    print('\n------------------------- Favorite Restaurant -------------------------')
    # return restaurant with the highest review for this customer
    print(customer_methods.favorite_restaurant)

    print('\n------------------------------ Add Review -----------------------------')
    # add review and return it
    print(customer_methods.add_review(restaurant1, 8))

    print('\n-------------------------- Delete Review ----------------------------')
    # delete reviews that belong to specific restaurants
    customer_methods.delete_reviews(restaurant1)




    '''----------------------------------- R E V I E W ------------------------------------------------'''
    review1 = session.query(Review).first()
    review_methods = ReviewMethods(review1)

    print()
    print('\n------------------------ Review SECTION ------------------------')
    print('------------------------ Review One ----------------------------')
    print(review_methods)

    print("\n-------------------- Review's Owner(customer) --------------------")
    # return customer
    print(review_methods.review_customer())

    print("\n-------------------- Review's Target(restaurant) --------------------")
    # return restaurant
    print(review_methods.review_restaurant())

    print('\n--------------------------- Full Review ---------------------------')
    # return full review details
    print(review_methods.full_review())

```
## Results from Example Usage
```python


-------------------------ALL REVIEWS-------------------------
Review for Victoriastad Restaurant by Danielle Reynolds: 4 stars.
Review for Victoriastad Restaurant by Lisa Wilson: 10 stars.
Review for Victoriastad Restaurant by Paul Johnson: 7 stars.
Review for Victoriastad Restaurant by Ronald Smith: 9 stars.
Review for Victoriastad Restaurant by Kevin Bryan: 1 stars.
Review for Victoriastad Restaurant by Kayla Kim: 8 stars.
Review for Victoriastad Restaurant by Wendy Johnson: 2 stars.


------------------------- RESTAURANT SECTION ------------------------
------------------------- Restaurant One -----------------------------
Victoriastad Restaurant - Price: $8241.00


-------------------- Restaurant's Review --------------------
Review by Danielle Reynolds: 4 stars.
Review by Lisa Wilson: 10 stars.
Review by Paul Johnson: 7 stars.
Review by Ronald Smith: 9 stars.
Review by Kevin Bryan: 1 stars.
Review by Kayla Kim: 8 stars.
Review by Wendy Johnson: 2 stars.

-------------------- Restaurant's Customers --------------------

2: Danielle, Reynolds
10: Lisa, Wilson
4: Paul, Johnson
5: Ronald, Smith
9: Kevin, Bryan
6: Kayla, Kim
7: Wendy, Johnson

------------------------- Fanciest Restaurant -------------------------
Millerburgh Restaurant - Price: $8367.00


------------------------- CUSTOMER SECTION ------------------------
------------------------ Customer One ---------------------------
1: Ramirez, Stephanie


------------------------ Customer's Reviews ------------------------
Review for Millerburgh: 4 stars.
Review for Millerburgh: 10 stars.
Review for Leetown: 9 stars.

-------------------- Customer's Reviewed Restaurants --------------------
Millerburgh - Price: $8367.00
Leetown - Price: $4688.00

-------------------------- Customer's Full Name -------------------------
Stephanie Ramirez

------------------------- Favorite Restaurant -------------------------
Millerburgh Restaurant - Price: $8367.00

------------------------------ Add Review -----------------------------
Review for Victoriastad by Stephanie Ramirez: 8 stars.

-------------------------- Delete Review ----------------------------
Stephanie's reviews for 'Victoriastad restaurant' have been successfully deleted!


------------------------ Review SECTION ------------------------
------------------------ Review One ----------------------------
 Review for Victoriastad by Danielle Reynolds: 4 stars.

-------------------- Review's Owner(customer) --------------------
Danielle Reynolds

-------------------- Review's Target(restaurant) --------------------
Victoriastad Restaurant - Price: $8241.00

--------------------------- Full Review ---------------------------
Review for Victoriastad Restaurant - Price: $8241.00 Restaurant by Danielle Reynolds: 4 stars

```

## Contributions

Contributions are welcome! Please open an issue or pull request for any improvements or bug fixes.


## License

This project is licensed under the [MIT License](LICENSE).

## Author

Created by [Abed Nganga Njuguna ](https://github.com/Nganga-A)