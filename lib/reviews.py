from models import Review

class ReviewMethods:
    def __init__(self,review):
        self.review = review

    # represent the class instances
    def __repr__(self):
        return (f"Customer({self.review.customer}) | Restaurant({self.review.restaurant}) | star-rating({self.review} stars) |")

    def review_customer_name(self):
        return self.review.customer.full_name

    def review_rating(self):
        return self.review           

    def review_customer(self):
        # Return the Customer instance for this review
        return self.customer

    def review_restaurant(self):
        # Return the Restaurant instance for this review
        return self.restaurant

    def full_review(self):
        return f"Review for {self.review.restaurant.name} Restaurant by {self.review.customer.full_name}: {self.review.star_rating} stars."
