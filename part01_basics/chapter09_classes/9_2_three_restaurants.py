class Restaurant:
    """Model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThe name of restaurant is {self.restaurant_name.title()}.")
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print("\tThe restaurant is open!")


my_restaurant = Restaurant("Lucy Dinner", "Viet food")
dung_restaurant = Restaurant("Dung Com Hen", "Viet food")
laurence_restaurant = Restaurant("The Laurence station", "France food")

my_restaurant.describe_restaurant()
dung_restaurant.describe_restaurant()
laurence_restaurant.describe_restaurant()

# The name of restaurant is Lucy Dinner.
# Lucy Dinner serves Viet food cuisine.

# The name of restaurant is Dung Com Hen.
# Dung Com Hen serves Viet food cuisine.

# The name of restaurant is The Laurence Station.
# The Laurence Station serves France food cuisine.
