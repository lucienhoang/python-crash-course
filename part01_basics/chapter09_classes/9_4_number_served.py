class Restaurant:
    """Model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name.title()}.")
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type} cuisine.")

    def set_number_served(self, value):
        self.number_served = value

    def increment_number_served(self, value):
        self.number_served += value


my_restaurant = Restaurant("Lucy Diner", "Vietnamese")

my_restaurant.describe_restaurant()
print(f"Number of customers served: {my_restaurant.number_served}")

print("---")
my_restaurant.number_served = 23
print(f"Number of customers served: {my_restaurant.number_served}")

# The restaurant's name is Lucy Diner.
# Lucy Diner serves Vietnamese cuisine.
# Number of customers served: 0
# ---
# Number of customers served: 23

print("---")
my_restaurant.set_number_served(43)
print(f"Number of customers served: {my_restaurant.number_served}")

# Number of customers served: 43

print("---")
my_restaurant.increment_number_served(20)
print(f"Number of customers served: {my_restaurant.number_served}")

# Number of customers served: 63
