from models import session

class RestaurantMethods:
    def __init__(self, restaurant):
        self.restaurant = restaurant

        # represent the class instances
    def __repr__(self):
        return f'{self.restaurant.name} Restaurant - Price: ${self.restaurant.price}.00\n'

    def restaurant_reviews(self):
        # Return a collection of all the reviews for this restaurant
        return self.restaurant.reviews

    def restaurant_customers(self):
        # Return a collection of all the customers who reviewed the restaurant
        return self.restaurant.customers

    @classmethod
    def fanciest_restaurant(cls):
        # Return the restaurant instance with the highest price
        return session.query(cls).order_by(cls.restaurant.price.desc()).first()

    def all_reviews(self):
        # Return a list of strings with all the reviews for this restaurant
        reviews = []
        for review in self.restaurant.reviews:
            reviews.append(f"Review for {self.restaurant.name} by {review.customer.full_name()}: {review.star_rating} stars.")
        return reviews
