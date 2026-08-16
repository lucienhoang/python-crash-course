class Restaurant:
    """Model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name.title()}.")
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print("\tThe restaurant is open!")


my_restaurant = Restaurant("Lucy Diner", "Vietnamese")

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# Lucy Diner
# Vietnamese
# The restaurant's name is Lucy Diner.
# Lucy Diner serves Vietnamese cuisine.
#         The restaurant is open!
