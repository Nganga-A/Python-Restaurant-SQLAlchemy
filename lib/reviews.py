from models import Review

class ReviewMethods:
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
