class Restaurant:
    """Model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of restaurant is {self.restaurant_name.title()}.")
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type} cuisine.")


my_restaurant = Restaurant("Lucy Dinner", "Viet food")

my_restaurant.describe_restaurant()
print(f"Number of customers have been served: {my_restaurant.number_served}")

print("---")
my_restaurant.number_served = 23
print(f"Number of customers have been served: {my_restaurant.number_served}")

# The name of restaurant is Lucy Dinner.
# Lucy Dinner serves Viet food cuisine.
# Number of customers have been served: 0
# ---
# Number of customers have been served: 23
