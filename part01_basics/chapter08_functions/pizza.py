# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):  # Python packs the arguments into a tuple
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza("pepperoni")
make_pizza("mushrooms", "green pepper", "extra cheese")

# Making a pizza with the following toppings:
# - pepperoni

# Making a pizza with the following toppings:
# - mushrooms
# - green pepper
# - extra cheese
