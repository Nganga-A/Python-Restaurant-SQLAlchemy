from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Customer, Restaurant, Review, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurants.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Customer).delete()
    session.query(Review).delete()
    session.query(Restaurant).delete()
    fake = Faker()

    # ------------------------ Populate customer table --------------------------
    customers = []
    for i in range(10):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(customer)
        session.commit()
        customers.append(customer)


    # ----------------------- Populate restaurants table -----------------------
    restaurants = []
    for i in range(10):
        restaurant = Restaurant(
            name=fake.unique.name(),
            price=random.randint(4000,10000)
        )
        session.add(restaurant)
        session.commit()
        restaurants.append(restaurant)

    # ------------------------ Populate reviews table ----------------------------
    reviews = []
    for restaurant in restaurants:
        for i in range(random.randint(1,10)):
            customer = random.choice(customers)
            review = Review(
                restaurant_id=restaurant.id,
                star_rating=random.randint(1, 10),
                customer_id=customer.id
            )
            #checks if the current restaurant is not already associated with the customer in order to ensure the customer doesnt review the same restaurant multiple times
            if restaurant not in customer.restaurants:
                customer.reviews.append(review)
                session.commit()

    session.close()