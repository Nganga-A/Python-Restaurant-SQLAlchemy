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

## Project Composition

project_folder/
    ├── models.py          # Define database models
    ├── seeds.py           # Seed data for testing
    ├── main.py             # Main application logic
    ├── database.py        # Database configuration and session management
    ├── customer_methods.py  # Implement Customer class methods
    ├── restaurant_methods.py  # Implement Restaurant class methods
    ├── review_methods.py  # Implement Review class methods
