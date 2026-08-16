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


class IceCreamStand(Restaurant):
    """Model an Ice cream stand of Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["mango", "banana", "coconut"]

    def display_flavors(self):
        for flavor in self.flavors:
            print(f"   -{flavor}")


my_ice_cream = IceCreamStand("Luci", "Vietnamese")
print("My ice cream flavor:")
my_ice_cream.display_flavors()

# My ice cream flavor:
#    -mango
#    -banana
#    -coconut


# Restaurant
#     ↓
# "Every restaurant has a name and cuisine type."

# IceCreamStand
#     ↓
# "An ice cream stand is a restaurant,
#  but it also has ice cream flavors."
